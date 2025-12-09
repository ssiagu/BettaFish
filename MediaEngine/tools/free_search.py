"""
免费搜索工具集 (DuckDuckGo + AI总结)

版本: 1.0
创建日期: 2025-12-08

此脚本实现了免费的搜索功能，使用DuckDuckGo作为搜索源，
并集成了系统现有的LLM来生成AI总结，以替代付费的Anspire API。

主要特性:
- 完全免费：使用DuckDuckGo搜索，无API限制
- AI总结：集成系统LLM生成智能总结
- 接口兼容：保持与AnspireAISearch相同的接口
- 自动降级：当LLM不可用时返回纯搜索结果

主要工具:
- comprehensive_search: 执行全面搜索并生成AI总结
- search_last_24_hours: 获取24小时内最新信息
- search_last_week: 获取过去一周的主要报道
"""

import os
import sys
from typing import List, Dict, Any, Optional
from loguru import logger

# 添加utils目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
utils_dir = os.path.join(root_dir, 'utils')
if utils_dir not in sys.path:
    sys.path.append(utils_dir)

# 导入现有的数据结构
from dataclasses import dataclass, field
from .search import WebpageResult, AnspireResponse

# 尝试导入LLM客户端
try:
    from ..llms.base import LLMClient
    LLM_AVAILABLE = True
except ImportError:
    logger.warning("LLM客户端不可用，将返回不带总结的搜索结果")
    LLM_AVAILABLE = False

# 导入配置管理
try:
    from config import settings
    CONFIG_AVAILABLE = True
except ImportError:
    logger.warning("配置管理不可用，将使用环境变量")
    CONFIG_AVAILABLE = False

try:
    from ddgs import DDGS
    DDGS_AVAILABLE = True
except ImportError:
    logger.error("请安装ddgs库: pip install ddgs")
    DDGS_AVAILABLE = False


@dataclass
class FreeSearchClient:
    """
    免费搜索客户端，使用DuckDuckGo作为搜索源，
    并可选地使用LLM生成AI总结
    """

    def __init__(self, enable_ai_summary: bool = True):
        """
        初始化客户端

        Args:
            enable_ai_summary: 是否启用AI总结功能
        """
        if not DDGS_AVAILABLE:
            raise ImportError("请先安装 duckduckgo-search: pip install duckduckgo-search")

        self.ddgs = DDGS()
        self.enable_ai_summary = enable_ai_summary and LLM_AVAILABLE
        self.llm_client = None

        if self.enable_ai_summary:
            self._init_llm_client()

    def _init_llm_client(self):
        """初始化LLM客户端"""
        try:
            # 优先使用配置管理系统
            if CONFIG_AVAILABLE:
                api_key = settings.MEDIA_ENGINE_API_KEY or settings.MINDSPIDER_API_KEY
                base_url = settings.MEDIA_ENGINE_BASE_URL or settings.MINDSPIDER_BASE_URL
                model_name = settings.MEDIA_ENGINE_MODEL_NAME or settings.MINDSPIDER_MODEL_NAME or "gpt-3.5-turbo"
            else:
                # 回退到环境变量
                api_key = os.getenv("MEDIA_ENGINE_API_KEY") or os.getenv("MINDSPIDER_API_KEY")
                base_url = os.getenv("MEDIA_ENGINE_BASE_URL") or os.getenv("MINDSPIDER_BASE_URL")
                model_name = os.getenv("MEDIA_ENGINE_MODEL_NAME") or os.getenv("MINDSPIDER_MODEL_NAME", "gpt-3.5-turbo")

            if api_key:
                self.llm_client = LLMClient(
                    api_key=api_key,
                    base_url=base_url,
                    model_name=model_name
                )
                logger.info(f"LLM客户端已初始化，使用模型: {model_name}")
            else:
                logger.warning("未找到LLM API密钥，将使用无总结模式")
                self.enable_ai_summary = False
        except Exception as e:
            logger.error(f"LLM客户端初始化失败: {e}")
            self.enable_ai_summary = False

    def comprehensive_search(self, query: str, max_results: int = 10) -> AnspireResponse:
        """
        执行全面搜索并生成AI总结

        Args:
            query: 搜索查询
            max_results: 最大结果数

        Returns:
            AnspireResponse: 包含搜索结果和可选AI总结的响应
        """
        return self._search_with_summary(query, max_results, time_filter=None)

    def search_last_24_hours(self, query: str, max_results: int = 10) -> AnspireResponse:
        """
        搜索24小时内的最新信息

        Args:
            query: 搜索查询
            max_results: 最大结果数

        Returns:
            AnspireResponse: 包含搜索结果和可选AI总结的响应
        """
        return self._search_with_summary(query, max_results, time_filter='d')

    def search_last_week(self, query: str, max_results: int = 10) -> AnspireResponse:
        """
        搜索过去一周的主要报道

        Args:
            query: 搜索查询
            max_results: 最大结果数

        Returns:
            AnspireResponse: 包含搜索结果和可选AI总结的响应
        """
        return self._search_with_summary(query, max_results, time_filter='w')

    def _search_with_summary(self, query: str, max_results: int, time_filter: Optional[str] = None) -> AnspireResponse:
        """
        执行搜索并生成总结的内部方法

        Args:
            query: 搜索查询
            max_results: 最大结果数
            time_filter: 时间过滤器 ('d' for day, 'w' for week)

        Returns:
            AnspireResponse: 搜索响应
        """
        # 执行搜索
        webpages = self._search_duckduckgo(query, max_results, time_filter)

        # 生成响应
        response = AnspireResponse(
            query=query,
            webpages=webpages,
            score=1.0 if webpages else 0.0
        )

        # 如果启用AI总结且有搜索结果，生成总结
        if self.enable_ai_summary and webpages and self.llm_client:
            try:
                answer = self._generate_ai_summary(query, webpages)
                # 为了保持兼容性，我们使用一个特殊的字段来存储总结
                # 在后续处理中可以将这个字段转换为需要的格式
                response.conversation_id = "free_search_" + str(hash(query))
                # 将answer存储在conversation_id的元数据中，或者添加新的属性
                setattr(response, '_ai_answer', answer)
                logger.info(f"已为查询 '{query}' 生成AI总结")
            except Exception as e:
                logger.error(f"生成AI总结失败: {e}")

        return response

    def _search_duckduckgo(self, query: str, max_results: int, time_filter: Optional[str] = None) -> List[WebpageResult]:
        """
        使用DuckDuckGo执行搜索

        Args:
            query: 搜索查询
            max_results: 最大结果数
            time_filter: 时间过滤器

        Returns:
            List[WebpageResult]: 搜索结果列表
        """
        results = []
        try:
            # 构建搜索参数
            search_kwargs = {
                'region': 'wt-wt',
                'safesearch': 'moderate',
                'max_results': max_results
            }

            # 添加时间过滤
            if time_filter:
                search_kwargs['timelimit'] = time_filter

            # 执行搜索
            for result in self.ddgs.text(query, **search_kwargs):
                results.append(WebpageResult(
                    name=result.get('title', ''),
                    url=result.get('href', ''),
                    snippet=result.get('body', ''),
                    display_url=result.get('href', ''),
                    date_last_crawled=result.get('date')
                ))

        except Exception as e:
            logger.error(f"DuckDuckGo搜索失败: {e}")

        return results

    def _generate_ai_summary(self, query: str, webpages: List[WebpageResult]) -> str:
        """
        使用LLM生成搜索结果的AI总结

        Args:
            query: 原始查询
            webpages: 搜索结果列表

        Returns:
            str: AI生成的总结
        """
        if not self.llm_client or not webpages:
            return ""

        # 构建搜索结果文本
        results_text = "\n\n".join([
            f"标题: {wp.name}\n链接: {wp.url}\n摘要: {wp.snippet}"
            for wp in webpages[:5]  # 限制为前5个结果以控制token使用
        ])

        # 构建提示词
        system_prompt = """你是一个专业的信息分析师。请根据搜索结果，为用户提供一个简洁、准确、有用的总结。

总结要求：
1. 概括搜索结果的核心信息
2. 提炼关键要点和见解
3. 保持客观中立
4. 使用中文回复
5. 总结长度控制在200-500字之间"""

        user_prompt = f"""用户查询：{query}

搜索结果：
{results_text}

请根据以上搜索结果，生成一个专业总结："""

        try:
            # 调用LLM生成总结
            response = self.llm_client.invoke(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                temperature=0.3
            )

            return response.strip() if response else ""

        except Exception as e:
            logger.error(f"LLM调用失败: {e}")
            return ""

    def get_ai_answer(self, response: AnspireResponse) -> Optional[str]:
        """
        获取AI生成的总结

        Args:
            response: 搜索响应

        Returns:
            Optional[str]: AI总结文本
        """
        return getattr(response, '_ai_answer', None)


# 为了保持向后兼容，创建一个工厂函数
def create_free_search_client(enable_ai_summary: bool = True) -> FreeSearchClient:
    """
    创建免费搜索客户端的工厂函数

    Args:
        enable_ai_summary: 是否启用AI总结

    Returns:
        FreeSearchClient: 免费搜索客户端实例
    """
    return FreeSearchClient(enable_ai_summary=enable_ai_summary)