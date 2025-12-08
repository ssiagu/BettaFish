# ReportEngine (报告引擎)

> [首页](../CLAUDE.md) > ReportEngine

## 模块概述

ReportEngine是BettaFish项目的核心报告生成引擎，负责将InsightEngine、MediaEngine、QueryEngine三个子引擎的分析结果和论坛讨论内容整合成结构化的HTML报告。该模块采用节点式处理流程，通过模板选择、布局设计、章节生成、IR装订和HTML渲染等多个步骤，生成专业的分析报告。

### 主要功能
- 智能模板选择：根据内容自动选择最合适的报告模板
- 动态布局生成：智能设计报告结构和页面布局
- 章节内容生成：基于LLM的智能章节写作
- IR装订验证：确保报告结构完整性和一致性
- 多格式渲染：支持HTML和PDF输出
- 图表处理：自动生成和优化图表

## 核心类和接口

### 1. ReportAgent
报告生成代理的主类，是整个报告生成流程的总调度中心。

**主要方法：**
- `generate_report(input_data: Dict[str, Any]) -> str`: 生成完整报告
- `initialize_report(input_files: Dict[str, str]) -> None`: 初始化报告生成
- `check_input_ready() -> Dict[str, Any]`: 检查输入是否准备就绪
- `get_report_state() -> ReportState`: 获取当前报告状态

### 2. FileCountBaseline
文件数量基准管理器，用于跟踪各引擎的输出文件。

**主要方法：**
- `initialize_baseline(directories: Dict[str, str]) -> Dict[str, int]`: 初始化文件基准
- `check_new_files(directories: Dict[str, str]) -> Dict[str, Any]`: 检查新增文件
- `get_latest_files(directories: Dict[str, str]) -> Dict[str, str]`: 获取最新文件

### 3. 处理节点（Nodes）
基于节点式的报告生成流程。

**节点类型：**
- `TemplateSelectionNode`: 模板选择节点
- `DocumentLayoutNode`: 文档布局节点
- `WordBudgetNode`: 篇幅规划节点
- `ChapterGenerationNode`: 章节生成节点

### 4. 核心组件（Core）
报告生成的核心功能组件。

**组件说明：**
- `ChapterStorage`: 章节存储管理
- `DocumentComposer`: 文档组合器
- `TemplateSection`: 模板节定义

### 5. 渲染器（Renderers）
多格式输出渲染器。

**渲染器类型：**
- `HTMLRenderer`: HTML渲染器
- `PDFRenderer`: PDF渲染器
- `ChartToSVG`: 图表转换器
- `MathToSVG`: 数学公式转换器

## 目录结构

```
ReportEngine/
├── __init__.py                    # 模块入口
├── agent.py                      # ReportAgent主类
├── core/                         # 核心功能模块
│   ├── __init__.py
│   ├── chapter_storage.py       # 章节存储
│   ├── document_composer.py     # 文档组合
│   ├── template_parser.py       # 模板解析
│   └── stitcher.py              # IR装订器
├── ir/                           # IR验证模块
│   ├── __init__.py
│   ├── validator.py             # 验证器
│   └── schema.py                # IR模式定义
├── llms/                         # LLM客户端模块
│   ├── __init__.py
│   └── base.py                  # LLM客户端基类
├── nodes/                        # 处理节点模块
│   ├── __init__.py
│   ├── base_node.py             # 节点基类
│   ├── template_selection_node.py # 模板选择节点
│   ├── document_layout_node.py  # 文档布局节点
│   ├── word_budget_node.py      # 篇幅规划节点
│   └── chapter_generation_node.py # 章节生成节点
├── prompts/                      # 提示词模块
│   ├── __init__.py
│   └── prompts.py               # 各种提示词定义
├── renderers/                    # 渲染器模块
│   ├── assets/                  # 静态资源
│   │   └── fonts/               # 字体文件
│   ├── libs/                    # 渲染库
│   ├── __init__.py
│   ├── html_renderer.py         # HTML渲染器
│   ├── pdf_renderer.py          # PDF渲染器
│   ├── chart_to_svg.py          # 图表转换
│   └── math_to_svg.py           # 数学公式转换
├── report_template/              # 报告模板目录
├── scripts/                      # 脚本工具
│   ├── __init__.py
│   ├── export_to_pdf.py         # PDF导出脚本
│   ├── chart_repair_api.py      # 图表修复API
│   ├── chart_validator.py       # 图表验证
│   ├── json_parser.py           # JSON解析器
│   ├── pdf_layout_optimizer.py  # PDF布局优化
│   └── dependency_check.py      # 依赖检查
├── state/                        # 状态管理模块
│   ├── __init__.py
│   └── state.py                 # 报告状态管理
└── utils/                        # 工具函数模块
    ├── __init__.py
    └── config.py                # 配置管理
```

## 主要文件功能介绍

### agent.py
- **功能**: ReportAgent主类实现
- **职责**: 报告生成的总调度中心
- **特性**:
  - 协调三个分析引擎的数据输入
  - 管理报告生成的完整生命周期
  - 提供Web接口支持

### core/chapter_storage.py
- **功能**: 章节内容存储和管理
- **职责**: 保存和检索生成的章节内容
- **特性**:
  - 支持多种存储格式
  - 版本控制和增量更新
  - 章节内容验证

### nodes/
- **功能**: 报告生成的各个处理节点
- **职责**: 按流程顺序处理报告生成任务
- **流程**:
  1. 模板选择 → 2. 布局设计 → 3. 篇幅规划 → 4. 章节写作

### renderers/
- **功能**: 多格式输出渲染
- **职责**: 将报告内容渲染为最终格式
- **支持格式**: HTML、PDF、图表、数学公式

## 依赖关系

### 内部依赖
- InsightEngine: 洞察分析输入
- MediaEngine: 媒体分析输入
- QueryEngine: 查询分析输入
- ForumEngine: 论坛讨论输入

### 外部依赖
- loguru: 日志记录
- jinja2: HTML模板引擎
- weasyprint: PDF渲染
- matplotlib: 图表生成
- sympy: 数学公式处理
- beautifulsoup4: HTML解析
- reportlab: PDF生成

### 系统依赖
- LaTeX: 数学公式渲染（可选）
- wkhtmltopdf: PDF转换（可选）

## 使用示例

### 基础使用
```python
from ReportEngine import ReportAgent, create_agent

# 创建报告代理
agent = create_agent()

# 准备输入数据
input_data = {
    "topic": "人工智能发展报告",
    "insight_report": "path/to/insight_report.md",
    "media_report": "path/to/media_report.md",
    "query_report": "path/to/query_report.md",
    "forum_discussions": "path/to/forum_logs/"
}

# 生成报告
report_path = agent.generate_report(input_data)
print(f"报告已生成: {report_path}")
```

### 高级使用
```python
# 初始化并检查输入
agent.initialize_report(input_data)
status = agent.check_input_ready()

if status['ready']:
    # 获取实时状态
    state = agent.get_report_state()
    print(f"当前进度: {state.get_progress_percentage():.1f}%")

    # 生成报告
    report_path = agent.generate_report()
else:
    print(f"等待输入: {status['missing_engines']}")
```

### 使用Flask接口
```python
from ReportEngine.flask_interface import create_app

app = create_app()

# 启动Web服务
if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

## 测试说明

### 单元测试
测试文件位于ReportEngine内部：
- `test_chart_validator.py`: 图表验证测试
- `test_json_parser.py`: JSON解析测试

### 集成测试
- `test_report_generation.py`: 端到端报告生成测试
- `test_node_flow.py`: 节点流程测试

### 测试运行
```bash
# 运行内部测试
python -m pytest ReportEngine/ -v

# 运行特定测试
python -m pytest ReportEngine/test_chart_validator.py -v
```

## 模块特有配置项

### 环境变量配置
在 `.env` 文件中配置：

```bash
# 报告引擎配置
REPORT_ENGINE_API_KEY=your_report_engine_api_key
REPORT_ENGINE_MODEL_NAME=gpt-4
REPORT_ENGINE_BASE_URL=https://api.openai.com/v1

# 输出配置
REPORT_OUTPUT_DIR=./final_reports
REPORT_TEMPLATE_DIR=./ReportEngine/report_template

# PDF渲染配置
PDF_ENGINE=weasyprint  # 或 wkhtmltopdf
ENABLE_LATEX=true     # 启用LaTeX数学公式

# 渲染配置
MAX_CHART_SIZE=1920x1080
CHART_DPI=300
MATH_FORMULA_RENDER=true

# 性能配置
MAX_CONCURRENT_CHAPTERS=3
CHUNK_SIZE=1000
ENABLE_CACHING=true
```

### 报告模板配置
在 `report_template/` 目录下：
- 报告模板JSON配置文件
- HTML样式文件
- 自定义CSS和JavaScript

## 报告生成流程

1. **输入准备**
   - 检查三个引擎的输出文件
   - 加载论坛讨论内容
   - 验证输入完整性

2. **模板选择**
   - 分析主题和内容
   - 选择合适的报告模板
   - 初始化报告结构

3. **布局设计**
   - 设计章节层次结构
   - 规划内容分布
   - 确定视觉风格

4. **篇幅规划**
   - 计算各章节字数
   - 平衡内容权重
   - 优化阅读体验

5. **章节生成**
   - 并行生成各章节内容
   - 智能整合多方信息
   - 确保内容连贯性

6. **装订渲染**
   - 验证报告完整性
   - 渲染为HTML格式
   - 生成PDF版本（可选）

## 性能优化建议

1. **生成优化**:
   - 启用章节并行生成
   - 使用内容缓存减少重复计算
   - 优化LLM调用频率

2. **渲染优化**:
   - 预编译模板和样式
   - 压缩图片和图表
   - 使用增量渲染

3. **存储优化**:
   - 清理临时文件
   - 压缩历史报告
   - 实现增量更新

4. **系统优化**:
   - 合理设置并发数
   - 监控内存使用
   - 优化PDF生成参数

## 故障处理

### 常见问题
1. **内容生成失败**
   - 检查LLM API配置
   - 验证输入数据格式
   - 重试失败的章节

2. **渲染错误**
   - 确认依赖库安装
   - 检查模板语法
   - 验证图片路径

3. **性能问题**
   - 减少并发数量
   - 优化图表尺寸
   - 使用缓存机制

---

**Document Signature**: ssiagu
**Last Updated**: 2025-12-08