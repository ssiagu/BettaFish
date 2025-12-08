# QueryEngine (查询引擎)

> [首页](../CLAUDE.md) > QueryEngine

## 模块概述

QueryEngine是BettaFish项目的舆情查询引擎，专注于新闻和舆情信息的深度搜索与分析。该模块集成Tavily搜索API，提供多种新闻搜索工具，支持实时新闻获取、历史新闻查询、图片搜索等功能，特别适合用于舆情监控、新闻研究和事件追踪。

### 主要功能
- 新闻搜索：支持基础和深度新闻搜索
- 时效性查询：24小时、一周内的最新新闻
- 历史追溯：按日期范围搜索历史新闻
- 图片搜索：查找与新闻相关的图片资源
- AI智能总结：自动生成新闻摘要和分析

## 核心类和接口

### 1. DeepSearchAgent
查询引擎的深度搜索代理类。

**主要方法：**
- `research(query: str, save_report: bool = True) -> str`: 执行深度研究
- `execute_search_tool(tool_name: str, query: str, **kwargs) -> TavilyResponse`: 执行搜索工具

### 2. TavilyNewsAgency
Tavily新闻搜索客户端，提供多种专用搜索工具。

**搜索工具：**
- `basic_search_news(query: str, max_results: int = 7)`: 基础新闻搜索
- `deep_search_news(query: str) -> TavilyResponse`: 深度新闻分析
- `search_news_last_24_hours(query: str) -> TavilyResponse`: 24小时新闻
- `search_news_last_week(query: str) -> TavilyResponse`: 本周新闻
- `search_images_for_news(query: str) -> TavilyResponse`: 新闻图片搜索
- `search_news_by_date(query: str, start_date: str, end_date: str) -> TavilyResponse`: 按日期搜索

### 3. 响应数据结构
- `TavilyResponse`: Tavily API响应封装
- `SearchResult`: 网页搜索结果（包含发布日期）
- `ImageResult`: 图片搜索结果

## 目录结构

```
QueryEngine/
├── __init__.py              # 模块入口
├── agent.py                 # DeepSearchAgent主类
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
│   └── search.py          # Tavily搜索工具
└── utils/                   # 工具函数模块
    ├── __init__.py
    ├── config.py           # 配置管理
    └── text_processing.py  # 文本处理
```

## 主要文件功能介绍

### agent.py
- **功能**: DeepSearchAgent主类实现
- **职责**: 整合所有查询功能，实现完整的深度搜索流程
- **特性**:
  - 支持6种不同的新闻搜索工具
  - 智能日期格式验证
  - 自动参数处理和错误处理

### tools/search.py
- **功能**: Tavily新闻搜索工具的核心实现
- **职责**: 提供多种专用新闻搜索工具
- **搜索策略**:
  - 基础搜索：快速、通用的新闻搜索
  - 深度搜索：全面的深度分析
  - 时效性搜索：最新动态获取
  - 历史搜索：指定日期范围

### 状态管理
与其他引擎共享相同的状态管理结构，确保一致性。

## 依赖关系

### 内部依赖
- utils: 配置管理和文本处理工具
- retry_helper: API重试机制

### 外部依赖
- loguru: 日志记录
- tavily-python: Tavily API客户端
- pydantic: 数据验证
- python-dotenv: 环境变量管理

### API依赖
- Tavily Search API

## 使用示例

### 基础使用
```python
from QueryEngine import DeepSearchAgent, create_agent

# 使用默认配置创建代理
agent = create_agent()

# 执行深度研究
report = agent.research("2024年人工智能技术发展动态")
print(report)
```

### 使用特定搜索工具
```python
# 基础新闻搜索
response = agent.execute_search_tool(
    tool_name="basic_search_news",
    query="科技新闻",
    max_results=10
)

# 深度新闻分析
response = agent.execute_search_tool(
    tool_name="deep_search_news",
    query="人工智能伦理讨论"
)

# 24小时最新新闻
response = agent.execute_search_tool(
    tool_name="search_news_last_24_hours",
    query="突发新闻"
)

# 历史新闻搜索
response = agent.execute_search_tool(
    tool_name="search_news_by_date",
    query="奥运会",
    start_date="2024-07-26",
    end_date="2024-08-11"
)

# 新闻图片搜索
response = agent.execute_search_tool(
    tool_name="search_images_for_news",
    query="太空探索"
)
```

## 测试说明

### 单元测试
测试文件位于 `tests/query_engine/` 目录下：
- `test_agent.py`: DeepSearchAgent测试
- `test_tavily_search.py`: Tavily搜索工具测试
- `test_date_validation.py`: 日期验证测试
- `test_response_parsing.py`: 响应解析测试

### 集成测试
- `test_integration.py`: 端到端集成测试
- `test_news_search_flow.py`: 新闻搜索流程测试

### 测试运行
```bash
# 运行所有测试
python -m pytest tests/query_engine/ -v

# 运行特定测试
python -m pytest tests/query_engine/test_tavily_search.py::test_basic_search_news -v
```

## 模块特有配置项

### 环境变量配置
在 `.env` 文件中配置：

```bash
# Tavily API配置
TAVILY_API_KEY=your_tavily_api_key_here

# 查询引擎配置
QUERY_ENGINE_API_KEY=your_query_engine_api_key
QUERY_ENGINE_MODEL_NAME=gpt-4
QUERY_ENGINE_BASE_URL=https://api.openai.com/v1

# 输出配置
OUTPUT_DIR=./query_engine_reports
SAVE_INTERMEDIATE_STATES=true

# 搜索限制配置
MAX_SEARCH_RESULTS_FOR_LLM=50
MAX_CONTENT_LENGTH=10000
MAX_REFLECTIONS=2
```

### 搜索参数配置
```python
# 在代码中配置搜索参数
config = Settings()
config.MAX_SEARCH_RESULTS_FOR_LLM = 20  # 限制传递给LLM的结果数量
```

## 搜索工具选择指南

| 场景 | 推荐工具 | 说明 |
|------|----------|------|
| 日常新闻浏览 | basic_search_news | 快速、通用，最多7条结果 |
| 深度事件分析 | deep_search_news | 全面分析，包含AI摘要，最多20条 |
| 突发事件追踪 | search_news_last_24_hours | 获取24小时内最新动态 |
| 周报/月报 | search_news_last_week | 获取一周内的主要报道 |
| 历史事件研究 | search_news_by_date | 指定日期范围的精确搜索 |
| 图文报道 | search_images_for_news | 查找相关图片资源 |

## 新闻搜索最佳实践

1. **关键词优化**:
   - 使用具体、准确的关键词
   - 包含时间、地点等限定词
   - 使用引号进行精确匹配

2. **时效性考虑**:
   - 突发新闻使用24小时搜索
   - 定期报告使用一周搜索
   - 历史研究使用日期范围搜索

3. **深度分析建议**:
   - 复杂事件使用深度搜索
   - 利用AI摘要快速了解核心信息
   - 结合图片搜索获取更全面信息

4. **结果处理**:
   - 注意验证新闻来源的可靠性
   - 关注发布日期确保信息时效性
   - 对比多个来源获取平衡观点

## 性能优化建议

1. **API调用优化**:
   - 合理设置max_results避免过多数据
   - 使用基础搜索减少响应时间
   - 启用重试机制提高稳定性

2. **缓存策略**:
   - 对历史搜索结果启用缓存
   - 避免短时间内的重复查询
   - 保存重要搜索结果供后续参考

3. **并发控制**:
   - 控制搜索频率避免API限制
   - 批量处理多个查询请求
   - 合理安排搜索任务优先级

---

**Document Signature**: ssiagu
**Last Updated**: 2025-12-08