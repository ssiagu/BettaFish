# MediaEngine (媒体引擎)

> [首页](../CLAUDE.md) > MediaEngine

## 模块概述

MediaEngine是BettaFish项目的媒体搜索引擎，专门提供多模态搜索能力。该模块集成了Bocha AI搜索和安思派AI搜索，能够处理文本、图片、结构化数据等多种媒体类型的搜索请求，并支持实时新闻、股票、天气等特定领域的结构化信息查询。

### 主要功能
- 多模态搜索：支持网页、图片、AI总结的混合搜索
- 结构化数据查询：天气、股票、汇率等模态卡数据
- 时效性搜索：24小时、一周内的最新信息
- AI智能总结：自动生成搜索结果的智能摘要
- 追问建议：基于搜索结果提供相关问题

## 核心类和接口

### 1. DeepSearchAgent
媒体搜索代理的主类，整合所有媒体搜索功能。

**主要方法：**
- `research(query: str, save_report: bool = True) -> str`: 执行深度媒体研究
- `execute_search_tool(tool_name: str, query: str, **kwargs) -> BochaResponse`: 执行搜索工具
- `_validate_date_format(date_str: str) -> bool`: 验证日期格式

### 2. BochaMultimodalSearch
Bocha AI搜索的多模态客户端。

**搜索工具：**
- `comprehensive_search(query: str) -> BochaResponse`: 全面搜索
- `search_for_structured_data(query: str) -> BochaResponse`: 结构化数据查询
- `web_search_only(query: str) -> BochaResponse`: 纯网页搜索
- `search_last_24_hours(query: str) -> BochaResponse`: 24小时搜索
- `search_last_week(query: str) -> BochaResponse`: 一周搜索

### 3. AnspireAISearch
安思派AI搜索客户端。

### 4. 响应数据结构
- `BochaResponse`: Bocha API响应封装
- `AnspireResponse`: 安思派API响应封装
- `WebpageResult`: 网页搜索结果
- `ImageResult`: 图片搜索结果
- `ModalCardResult`: 模态卡结构化数据

## 目录结构

```
MediaEngine/
├── __init__.py              # 模块入口
├── agent.py                 # DeepSearchAgent和AnspireSearchAgent主类
├── llms/                    # LLM客户端模块
│   ├── __init__.py
│   └── base.py             # LLM客户端基类
├── nodes/                   # 处理节点模块
│   ├── __init__.py
│   ├── base_node.py        # 节点基类
│   ├── formatting_node.py  # 格式化节点
│   ├── report_structure_node.py  # 报告结构节点
│   ├── search_node.py      # 搜索节点
│   └── summary_node.py     # 总结节点
├── prompts/                 # 提示词模块
│   ├── __init__.py
│   └── prompts.py         # 各种提示词定义
├── state/                   # 状态管理模块
│   ├── __init__.py
│   └── state.py           # 状态数据结构
├── tools/                   # 搜索工具模块
│   ├── __init__.py
│   └── search.py          # Bocha和安思派搜索工具
└── utils/                   # 工具函数模块
    ├── __init__.py
    ├── config.py           # 配置管理
    └── text_processing.py  # 文本处理
```

## 主要文件功能介绍

### agent.py
- **功能**: DeepSearchAgent和AnspireSearchAgent主类实现
- **职责**: 整合所有媒体搜索模块，实现完整的深度搜索流程
- **特性**:
  - 支持Bocha多模态搜索
  - 支持安思派AI搜索
  - 智能工具选择和参数处理

### tools/search.py
- **功能**: Bocha和安思派搜索工具的核心实现
- **职责**: 提供多种专用搜索工具
- **搜索类型**:
  - 全面搜索（comprehensive_search）
  - 结构化数据查询（search_for_structured_data）
  - 纯网页搜索（web_search_only）
  - 时效性搜索（24小时、一周）

### 状态管理
与InsightEngine共享相同的状态管理结构，确保一致性。

## 依赖关系

### 内部依赖
- utils: 配置管理和文本处理工具
- retry_helper: API重试机制

### 外部依赖
- loguru: 日志记录
- requests: HTTP请求
- pydantic: 数据验证
- python-dotenv: 环境变量管理

### API依赖
- Bocha AI Search API
- Anspire AI Search API

## 使用示例

### 基础使用
```python
from MediaEngine import DeepSearchAgent, create_agent

# 使用默认配置创建代理
agent = create_agent()

# 执行深度研究
report = agent.research("最新的AI技术发展趋势")
print(report)
```

### 使用特定搜索工具
```python
# 全面搜索（包含网页、图片、AI总结）
response = agent.execute_search_tool(
    tool_name="comprehensive_search",
    query="人工智能最新进展"
)

# 结构化数据查询（天气、股票等）
response = agent.execute_search_tool(
    tool_name="search_for_structured_data",
    query="北京今天天气"
)

# 24小时最新搜索
response = agent.execute_search_tool(
    tool_name="search_last_24_hours",
    query="科技新闻"
)
```

### 使用AnspireSearchAgent
```python
from MediaEngine import AnspireSearchAgent

# 创建安思派搜索代理
anspire_agent = AnspireSearchAgent()

# 执行搜索
response = anspire_agent.execute_search_tool(
    tool_name="anspire_search",
    query="机器学习"
)
```

## 测试说明

### 单元测试
测试文件位于 `tests/media_engine/` 目录下：
- `test_agent.py`: DeepSearchAgent测试
- `test_bocha_search.py`: Bocha搜索工具测试
- `test_anspire_search.py`: 安思派搜索测试
- `test_response_parsing.py`: 响应解析测试

### 集成测试
- `test_integration.py`: 端到端集成测试
- `test_multimodal_search.py`: 多模态搜索测试

### 测试运行
```bash
# 运行所有测试
python -m pytest tests/media_engine/ -v

# 运行特定测试
python -m pytest tests/media_engine/test_bocha_search.py::test_comprehensive_search -v
```

## 模块特有配置项

### 环境变量配置
在 `.env` 文件中配置：

```bash
# Bocha AI搜索配置
BOCHA_API_KEY=your_bocha_api_key_here
BOCHA_WEB_SEARCH_API_KEY=your_bocha_web_search_key
BOCHA_BASE_URL=https://api.bocha.cn/v1/ai-search

# 媒体引擎配置
MEDIA_ENGINE_API_KEY=your_media_engine_api_key
MEDIA_ENGINE_MODEL_NAME=gpt-4
MEDIA_ENGINE_BASE_URL=https://api.openai.com/v1

# 输出配置
OUTPUT_DIR=./media_engine_reports
SAVE_INTERMEDIATE_STATES=true

# 搜索限制配置
MAX_SEARCH_RESULTS_FOR_LLM=50
MAX_CONTENT_LENGTH=10000
MAX_REFLECTIONS=2
```

### 支持的模态卡类型
- `weather_china`: 中国天气
- `weather_global`: 全球天气
- `stock`: 股票信息
- `exchange_rate`: 汇率信息
- `baike_pro`: 百度百科
- `medical_common`: 医疗信息

## 性能优化建议

1. **搜索策略优化**:
   - 根据查询类型选择合适的搜索工具
   - 结构化数据查询优先使用模态卡
   - 时效性需求使用24小时或一周搜索

2. **API调用优化**:
   - 合理设置 `MAX_SEARCH_RESULTS_FOR_LLM`
   - 使用纯网页搜索减少响应时间
   - 启用重试机制提高稳定性

3. **缓存策略**:
   - 对结构化数据启用缓存
   - 保存搜索历史避免重复查询

4. **并发控制**:
   - 避免同时进行大量搜索请求
   - 控制API调用频率

## 搜索工具选择指南

| 场景 | 推荐工具 | 说明 |
|------|----------|------|
| 综合信息查询 | comprehensive_search | 返回网页、图片、AI总结 |
| 天气/股票查询 | search_for_structured_data | 直接返回结构化数据 |
| 快速网页搜索 | web_search_only | 不包含AI总结，速度更快 |
| 最新资讯 | search_last_24_hours | 获取24小时内最新信息 |
| 周度总结 | search_last_week | 获取一周内主要报道 |

---

**Document Signature**: ssiagu
**Last Updated**: 2025-12-08