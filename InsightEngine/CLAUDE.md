# InsightEngine (洞察引擎)

> [首页](../CLAUDE.md) > InsightEngine

## 模块概述

InsightEngine是BettaFish项目的核心洞察引擎，负责深度搜索和智能分析。该模块实现了一个无框架的深度搜索AI代理，能够自动执行多轮搜索、反思和总结，最终生成深度洞察报告。

### 主要功能
- 深度搜索：支持多种搜索策略和数据库查询
- 智能反思：通过反思循环不断优化搜索结果
- 报告生成：自动结构化生成深度分析报告
- 情感分析：集成多语言情感分析能力
- 关键词优化：自动优化搜索关键词以提高搜索质量

## 核心类和接口

### 1. DeepSearchAgent
深度搜索代理的主类，整合所有模块功能。

**主要方法：**
- `research(query: str, save_report: bool = True) -> str`: 执行深度研究
- `execute_search_tool(tool_name: str, query: str, **kwargs) -> DBResponse`: 执行数据库查询工具
- `analyze_sentiment_only(texts: Union[str, List[str]]) -> Dict`: 独立情感分析
- `get_progress_summary() -> Dict`: 获取研究进度

### 2. State (状态管理)
管理整个研究过程的状态信息。

**核心组件：**
- `Search`: 单个搜索结果的状态
- `Research`: 段落研究过程的状态
- `State`: 全局状态管理

### 3. Nodes (处理节点)
基于节点式处理流程的设计模式。

**节点类型：**
- `ReportStructureNode`: 生成报告结构
- `FirstSearchNode`: 执行初始搜索
- `ReflectionNode`: 生成反思搜索
- `FirstSummaryNode`: 生成初始总结
- `ReflectionSummaryNode`: 生成反思总结
- `ReportFormattingNode`: 格式化最终报告

### 4. LLMClient
大语言模型客户端，支持多种模型接口。

## 目录结构

```
InsightEngine/
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
├── tools/                   # 工具模块
│   ├── __init__.py
│   ├── keyword_optimizer.py  # 关键词优化器
│   ├── search.py           # 搜索工具
│   └── sentiment_analyzer.py  # 情感分析器
└── utils/                   # 工具函数模块
    ├── __init__.py
    ├── config.py           # 配置管理
    ├── db.py              # 数据库工具
    └── text_processing.py  # 文本处理
```

## 主要文件功能介绍

### agent.py
- **功能**: DeepSearchAgent主类实现
- **职责**: 整合所有模块，实现完整的深度搜索流程
- **特性**:
  - 支持多轮搜索和反思
  - 集成关键词优化和情感分析
  - 自动生成和保存报告

### state/state.py
- **功能**: 状态管理核心实现
- **职责**: 定义和管理工作流中的各种状态
- **类结构**:
  - `Search`: 搜索结果状态
  - `Research`: 研究过程状态
  - `State`: 全局状态管理

### nodes/base_node.py
- **功能**: 节点基类定义
- **职责**: 提供统一的节点接口和基础功能
- **方法**: `mutate_state()` - 状态转换方法

### tools/keyword_optimizer.py
- **功能**: 关键词优化中间件
- **职责**: 自动优化搜索关键词以提高搜索质量
- **算法**: 使用LLM进行关键词扩展和优化

### tools/sentiment_analyzer.py
- **功能**: 多语言情感分析工具
- **职责**: 对文本进行情感倾向分析
- **支持语言**: 22种语言
- **集成**: WeiboMultilingualSentiment模型

## 依赖关系

### 内部依赖
- MediaEngine: 媒体数据库查询接口
- SentimentAnalysisModel: 情感分析模型

### 外部依赖
- loguru: 日志记录
- pydantic: 数据验证
- requests: HTTP请求
- python-dotenv: 环境变量管理

### 配置依赖
通过 `utils/config.py` 管理所有配置项：
- `INSIGHT_ENGINE_API_KEY`: API密钥
- `INSIGHT_ENGINE_MODEL_NAME`: 模型名称
- `INSIGHT_ENGINE_BASE_URL`: API基础URL
- `OUTPUT_DIR`: 输出目录
- `MAX_REFLECTIONS`: 最大反思次数

## 使用示例

### 基础使用
```python
from InsightEngine import DeepSearchAgent, create_agent

# 方法1: 使用默认配置
agent = create_agent()

# 方法2: 自定义配置
from InsightEngine.utils.config import Settings
config = Settings()
config.INSIGHT_ENGINE_MODEL_NAME = "gpt-4"
agent = DeepSearchAgent(config)

# 执行深度研究
report = agent.research("人工智能在教育领域的应用")
print(report)
```

### 高级使用
```python
# 独立使用搜索工具
response = agent.execute_search_tool(
    tool_name="search_topic_globally",
    query="新能源汽车",
    enable_sentiment=True
)

# 独立情感分析
sentiment_result = agent.analyze_sentiment_only([
    "这款产品真的很棒！",
    "服务态度很差。"
])

# 获取研究进度
progress = agent.get_progress_summary()
print(f"完成进度: {progress['completion_percentage']:.1f}%")
```

## 测试说明

### 单元测试
测试文件位于 `tests/insight_engine/` 目录下：
- `test_agent.py`: DeepSearchAgent测试
- `test_state.py`: 状态管理测试
- `test_nodes.py`: 节点功能测试
- `test_tools.py`: 工具模块测试

### 集成测试
- `test_integration.py`: 端到端集成测试
- `test_search_flow.py`: 搜索流程测试

### 测试运行
```bash
# 运行所有测试
python -m pytest tests/insight_engine/ -v

# 运行特定测试
python -m pytest tests/insight_engine/test_agent.py::test_research -v
```

## 模块特有配置项

### 环境变量配置
在 `.env` 文件中配置：

```bash
# Insight Engine配置
INSIGHT_ENGINE_API_KEY=your_api_key_here
INSIGHT_ENGINE_MODEL_NAME=gpt-4
INSIGHT_ENGINE_BASE_URL=https://api.openai.com/v1

# 搜索限制配置
DEFAULT_SEARCH_TOPIC_GLOBALLY_LIMIT_PER_TABLE=50
DEFAULT_SEARCH_TOPIC_BY_DATE_LIMIT_PER_TABLE=50
DEFAULT_GET_COMMENTS_FOR_TOPIC_LIMIT=200
DEFAULT_SEARCH_TOPIC_ON_PLATFORM_LIMIT=100
DEFAULT_SEARCH_HOT_CONTENT_LIMIT=100

# LLM配置
MAX_SEARCH_RESULTS_FOR_LLM=50
MAX_CONTENT_LENGTH=10000
MAX_REFLECTIONS=2

# 输出配置
OUTPUT_DIR=./insight_engine_reports
SAVE_INTERMEDIATE_STATES=true
```

### 运行时配置
```python
# 动态配置示例
from InsightEngine.utils.config import Settings

config = Settings()
config.MAX_REFLECTIONS = 3  # 增加反思次数
config.SAVE_INTERMEDIATE_STATES = True  # 保存中间状态
```

## 性能优化建议

1. **搜索优化**:
   - 使用关键词优化器减少无效搜索
   - 合理设置搜索限制避免过载

2. **LLM调用优化**:
   - 设置合适的 `MAX_SEARCH_RESULTS_FOR_LLM`
   - 批量处理文本以减少API调用

3. **缓存策略**:
   - 启用搜索结果缓存
   - 保存和复用中间状态

4. **并发控制**:
   - 避免同时执行多个研究任务
   - 合理设置反思迭代次数

---

**Document Signature**: ssiagu
**Last Updated**: 2025-12-08