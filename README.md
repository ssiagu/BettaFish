<div align="center">

<img src="static/image/logo_compressed.png" alt="BettaFish Logo" width="100%">

<a href="https://trendshift.io/repositories/15286" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15286" alt="666ghj%2FBettaFish | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<a href="https://aihubmix.com/?aff=8Ds9" target="_blank"><img src="./static/image/logo_aihubmix.png" alt="666ghj%2FBettaFish | Trendshift" height="40"/></a>&ensp;
<a href="https://lioncc.ai/" target="_blank"><img src="./static/image/logo_loincc.png" alt="666ghj%2FBettaFish | Trendshift" height="40"/></a>&ensp;
<a href="https://share.302.ai/P66Qe3" target="_blank"><img src="./static/image/logo_302ai.png" alt="666ghj%2FBettaFish | Trendshift" height="40"/></a>

<a href="https://open.anspire.cn/?share_code=3E1FUOUH" target="_blank"><img src="./static/image/logo_anspire.png" alt="666ghj%2FBettaFish | Trendshift" height="50"/></a>

[![GitHub Stars](https://img.shields.io/github/stars/666ghj/BettaFish?style=flat-square)](https://github.com/666ghj/BettaFish/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/666ghj/BettaFish?style=flat-square)](https://github.com/666ghj/BettaFish/watchers)
[![GitHub Forks](https://img.shields.io/github/forks/666ghj/BettaFish?style=flat-square)](https://github.com/666ghj/BettaFish/network)
[![GitHub Issues](https://img.shields.io/github/issues/666ghj/BettaFish?style=flat-square)](https://github.com/666ghj/BettaFish/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/666ghj/BettaFish?style=flat-square)](https://github.com/666ghj/BettaFish/pulls)

[![GitHub License](https://img.shields.io/github/license/666ghj/BettaFish?style=flat-square)](https://github.com/666ghj/BettaFish/blob/main/LICENSE)
[![Version](https://img.shields.io/badge/version-v1.2.1-green.svg?style=flat-square)](https://github.com/666ghj/BettaFish)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)



[English](./README-EN.md) | [中文文档](./README.md)

</div>

## ⚡ 项目概述

“**微舆**” 是一个从0实现的创新型 多智能体 舆情分析系统，帮助大家破除信息茧房，还原舆情原貌，预测未来走向，辅助决策。用户只需像聊天一样提出分析需求，智能体开始全自动分析 国内外30+主流社媒 与 数百万条大众评论。

> “微舆”谐音“微鱼”，BettaFish是一种体型很小但非常好斗、漂亮的鱼，它象征着“小而强大，不畏挑战”

查看系统以“武汉大学舆情”为例，生成的研究报告：[武汉大学品牌声誉深度分析报告](./final_reports/final_report__20250827_131630.html)

查看系统以“武汉大学舆情”为例，一次完整运行的视频：[视频-武汉大学品牌声誉深度分析报告](https://www.bilibili.com/video/BV1TH1WBxEWN/?vd_source=da3512187e242ce17dceee4c537ec7a6#reply279744466833)

不仅仅体现在报告质量上，相比同类产品，我们拥有🚀六大优势：

1. **AI驱动的全域监控**：AI爬虫集群7x24小时不间断作业，全面覆盖微博、小红书、抖音、快手等10+国内外关键社媒。不仅实时捕获热点内容，更能下钻至海量用户评论，让您听到最真实、最广泛的大众声音。

2. **超越LLM的复合分析引擎**：我们不仅依赖设计的5类专业Agent，更融合了微调模型、统计模型等中间件。通过多模型协同工作，确保了分析结果的深度、准度与多维视角。

3. **强大的多模态能力**：突破图文限制，能深度解析抖音、快手等短视频内容，并精准提取现代搜索引擎中的天气、日历、股票等结构化多模态信息卡片，让您全面掌握舆情动态。

4. **Agent“论坛”协作机制**：为不同Agent赋予独特的工具集与思维模式，引入辩论主持人模型，通过“论坛”机制进行链式思维碰撞与辩论。这不仅避免了单一模型的思维局限与交流导致的同质化，更催生出更高质量的集体智能与决策支持。

5. **公私域数据无缝融合**：平台不仅分析公开舆情，还提供高安全性的接口，支持您将内部业务数据库与舆情数据无缝集成。打通数据壁垒，为垂直业务提供“外部趋势+内部洞察”的强大分析能力。

6. **轻量化与高扩展性框架**：基于纯Python模块化设计，实现轻量化、一键式部署。代码结构清晰，开发者可轻松集成自定义模型与业务逻辑，实现平台的快速扩展与深度定制。

**始于舆情，而不止于舆情**。“微舆”的目标，是成为驱动一切业务场景的简洁通用的数据分析引擎。

> 举个例子. 你只需简单修改Agent工具集的api参数与prompt，就可以把他变成一个金融领域的市场分析系统
>
> 附一个比较活跃的L站项目讨论帖：https://linux.do/t/topic/1009280
>
> 查看L站佬友做的测评 [开源项目(微舆)与manus|minimax|ChatGPT对比](https://linux.do/t/topic/1148040)

<div align="center">
<img src="static/image/system_schematic.png" alt="banner" width="800">

告别传统的数据看板，在“微舆”，一切由一个简单的问题开始，您只需像对话一样，提出您的分析需求
</div>

## 🪄 赞助商

LLM模型API赞助：<a href="https://aihubmix.com/?aff=8Ds9" target="_blank"><img src="./static/image/logo_aihubmix.png" alt="666ghj%2FBettaFish | Trendshift" height="40"/></a>

<details>
<summary>有赞助LLM算力福利！编程拼车codecodex.ai；编程算力VibeCodingAPI.ai：</a><span style="margin-left: 10px"><a href="https://codecodex.ai/" target="_blank"><img src="./static/image/logo_loincc.png" alt="666ghj%2FBettaFish | Trendshift" height="40"/></a></summary>

1. 所罗门博客LionCC.ai已更新《BettaFish 微舆系统 - LionCC API 部署配置完全指南》正在二开优化一键部署和云服务器调用方案。
2. VibeCodingapi.ai狮子算力平台已经适配《BettaFish 微舆系统》所有LLM模型含claude code和openai codex和gemini cli编程开发三巨头算力。额度价格，只要一比一（100元等于100美刀额度）
3. Codecodex.ai狮子编程拼车系统，已实现无IP门槛绕过claude code和openai codex封锁，按官方部署教程后切换BASE_URL调用地址和Token key调用密钥即可使用最强编程模型。

所罗门LionCC赞助BettaFish 微舆福利：打开codecodex.ai狮子编程频道扫码加入微信社群，注册VibeCodingapi.ai狮子算力，统一送20刀API额度（仅限前一千名）
</details>

<details>
<summary>按用量付费的企业级AI资源平台，提供市场上全面的AI模型和API，以及多种在线AI应用：</a><span style="margin-left: 10px"><a href="https://share.302.ai/P66Qe3" target="_blank"><img src="./static/image/logo_302ai.png" alt="666ghj%2FBettaFish | Trendshift" height="40"/></a></summary>
<img src="static/image/banner_302ai_ch.jpg" alt="banner">302.AI是一个按用量付费的企业级AI资源平台，提供市场上最新、最全面的AI模型和API，以及多种开箱即用的在线AI应用。
</details>

<details>
<summary>AI联网搜索、文件解析及网页内容抓取等智能体核心能力提供商：</a><span style="margin-left: 10px"><a href="https://open.anspire.cn/?share_code=3E1FUOUH" target="_blank"><img src="./static/image/logo_anspire.png" alt="666ghj%2FBettaFish | Trendshift" height="50"/></a></summary>
安思派开放平台(Anspire Open)是面向智能体时代的领先的基础设施提供商。我们为开发者提供构建强大智能体所需的核心能力栈，现已上线AI联网搜索【多版本，极具竞争力的价格】、文件解析【限免】及网页内容抓取【限免】、云端浏览器自动化（Anspire Browser Agent）【内测】、多轮改写等服务，持续为智能体连接并操作复杂的数字世界提供坚实基础。可无缝集成至Dify、Coze、元器等主流智能体平台。通过透明点数计费体系与模块化设计，为企业提供高效、低成本的定制化支持，加速智能化升级进程。
</details>

## 🏗️ 系统架构

### 整体架构图

BettaFish是一个基于**多智能体架构**的微博舆情分析系统，采用**微服务架构设计**，各引擎模块独立运作又相互配合。

**Insight Agent** 私有数据库挖掘：私有舆情数据库深度分析AI代理

**Media Agent** 多模态内容分析：具备强大多模态能力的AI代理

**Query Agent** 精准信息搜索：具备国内外网页搜索能力的AI代理

**Report Agent** 智能报告生成：内置模板的多轮报告生成AI代理

<div align="center">
<img src="static/image/framework.png" alt="banner" width="800">
</div>

### 技术栈

- **后端**: Python 3.11, Flask (主应用), Streamlit (各引擎UI)
- **数据库**: PostgreSQL/MySQL (媒体数据存储)
- **缓存**: Redis (可选)
- **AI/LLM**: 支持多种LLM API (OpenAI, Kimi, Gemini, DeepSeek等)
- **实时通信**: Socket.IO (WebSocket)
- **部署**: Docker, Docker Compose

### 核心架构层次

```mermaid
graph TB
    subgraph "前端层"
        A[Flask主应用 app.py:5000] --> B[洞察引擎 Streamlit:8501]
        A --> C[媒体引擎 Streamlit:8502]
        A --> D[查询引擎 Streamlit:8503]
    end

    subgraph "API层"
        E[REST API] --> F[WebSocket API]
        F --> G[统一搜索接口]
    end

    subgraph "引擎层"
        H[InsightEngine<br/>洞察引擎]
        I[MediaEngine<br/>媒体引擎]
        J[QueryEngine<br/>查询引擎]
        K[ReportEngine<br/>报告引擎]
        L[ForumEngine<br/>论坛引擎]
    end

    subgraph "工具层"
        M[MindSpider<br/>心智蜘蛛]
        N[SentimentAnalysisModel<br/>情感分析模型]
        O[关键词优化器]
        P[多语言处理]
    end

    subgraph "基础设施层"
        Q[PostgreSQL/MySQL]
        R[Redis缓存]
        S[文件存储]
        T[外部LLM APIs]
    end
```

### 核心引擎模块详解

#### 🔍 InsightEngine (洞察引擎)
- **位置**: `InsightEngine/`
- **核心功能**: 深度搜索与智能洞察
- **主类**: `DeepSearchAgent` (agent.py:41)
- **工作流程**:
  1. `FirstSearchNode`: 执行初始搜索
  2. `FirstSummaryNode`: 生成首次总结
  3. `ReflectionNode`: 反思分析
  4. `ReflectionSummaryNode`: 生成反思总结
  5. `ReportFormattingNode`: 格式化报告
- **特色功能**:
  - 关键词自动优化 (keyword_optimizer.py)
  - 多语言情感分析 (22种语言)
  - 智能聚类算法 (SentenceTransformer)

#### 🎥 MediaEngine (媒体引擎)
- **位置**: `MediaEngine/`
- **核心功能**: 多媒体内容处理与分析
- **主类**: `MediaAgent` (agent.py)
- **特色功能**:
  - 图片/视频内容分析
  - 多模态内容理解
  - 媒体数据挖掘

#### 🔎 QueryEngine (查询引擎)
- **位置**: `QueryEngine/`
- **核心功能**: 基于Tavily的新闻搜索与信息检索
- **主类**: `QueryAgent` (agent.py)
- **特色功能**:
  - 实时新闻搜索
  - Tavily API集成
  - 信息聚合与筛选

#### 📊 ReportEngine (报告引擎)
- **位置**: `ReportEngine/`
- **核心功能**: 智能报告生成与导出
- **主类**: `ReportAgent` (agent.py)
- **Flask接口**: `flask_interface.py`
- **渲染器**: `renderers/`
- **特色功能**:
  - 多格式报告导出 (PDF, HTML, Word)
  - 模板化报告生成
  - 数据可视化

#### 💬 ForumEngine (论坛引擎)
- **位置**: `ForumEngine/`
- **核心功能**: 论坛监控与LLM托管
- **监控器**: `monitor.py`
- **主持人**: `llm_host.py`
- **特色功能**:
  - 实时监控各引擎日志
  - AI主持人智能引导讨论
  - 多引擎协作平台

#### 🕷️ MindSpider (心智蜘蛛)
- **位置**: `MindSpider/`
- **核心功能**: 主题提取与深度情感爬取
- **子模块**:
  - `BroadTopicExtraction/`: 广泛主题提取
  - `DeepSentimentCrawling/`: 深度情感爬取
- **主程序**: `main.py`

### 系统执行流程

#### 启动流程
```python
# app.py 主启动流程
1. Flask应用初始化 (app.py:35)
2. SocketIO异步模式选择 (app.py:39-54)
3. ReportEngine Blueprint注册 (app.py:90-94)
4. 系统组件初始化 (initialize_system_components:286)
   - MindSpider数据库初始化
   - Streamlit子应用启动
   - ForumEngine论坛启动
   - ReportEngine初始化
5. 日志监控线程启动 (monitor_forum_log:449)
```

#### 请求处理流程
```mermaid
sequenceDiagram
    participant Client as 客户端
    participant Flask as Flask主应用
    participant Streamlit as Streamlit应用
    participant Engine as 引擎模块
    participant DB as 数据库
    participant LLM as LLM API

    Client->>Flask: HTTP/WS请求
    Flask->>Streamlit: 转发请求
    Streamlit->>Engine: 调用引擎API
    Engine->>DB: 查询数据
    Engine->>LLM: AI分析请求
    LLM-->>Engine: 返回分析结果
    Engine-->>Streamlit: 处理结果
    Streamlit-->>Flask: 响应数据
    Flask-->>Client: 返回结果
```

#### 搜索分析流程
1. **接收查询**: 通过统一搜索接口接收查询请求
2. **关键词优化**: 使用LLM优化搜索关键词
3. **多引擎并行**: Insight/Media/Query三引擎并行处理
4. **结果聚合**: 收集各引擎搜索结果
5. **智能分析**:
   - 情感分析 (SentimentAnalysisModel)
   - 内容聚类
   - 深度洞察生成
6. **报告生成**: ReportEngine生成最终报告
7. **实时推送**: 通过WebSocket推送结果

### API接口体系

#### REST API (app.py)
- **系统管理**:
  - `GET /api/system/status` - 获取系统状态
  - `POST /api/system/start` - 启动系统
  - `POST /api/system/shutdown` - 关闭系统
  - `GET /api/status` - 获取所有应用状态

- **应用控制**:
  - `POST /api/start/<app_name>` - 启动指定应用
  - `POST /api/stop/<app_name>` - 停止指定应用
  - `GET /api/output/<app_name>` - 获取应用输出

- **搜索与分析**:
  - `POST /api/search` - 统一搜索接口
  - `GET /api/forum/log` - 获取论坛日志
  - `POST /api/forum/log/history` - 获取历史日志

- **配置管理**:
  - `GET /api/config` - 获取配置
  - `POST /api/config` - 更新配置

#### WebSocket API (Socket.IO)
- **连接事件**:
  - `connect` - 客户端连接
  - `request_status` - 请求状态更新
  - `console_output` - 控制台输出推送
  - `forum_message` - 论坛消息推送
  - `status_update` - 状态更新推送

#### Streamlit API端口
- InsightEngine: 8601
- MediaEngine: 8602
- QueryEngine: 8603

### 数据流转机制

#### 日志系统
- **日志目录**: `logs/`
- **日志文件**:
  - `insight.log` - 洞察引擎日志
  - `media.log` - 媒体引擎日志
  - `query.log` - 查询引擎日志
  - `forum.log` - 论坛日志

#### 监控机制
ForumEngine实时监控各引擎的SummaryNode输出，提取关键信息并通过AI主持人促进讨论。

#### 状态管理
- 全局状态锁 (system_state_lock:243)
- 进程状态追踪 (processes:516)
- WebSocket实时状态同步

### 配置体系

#### 配置文件结构 (config.py)
- **Flask服务器配置**: HOST, PORT
- **数据库配置**: DB_DIALECT, DB_HOST, DB_PORT等
- **LLM API配置**: 各引擎的API_KEY, BASE_URL, MODEL_NAME
- **搜索工具配置**: TAVILY_API_KEY, BOCHA_API_KEY等
- **搜索限制配置**: 各类DEFAULT_*_LIMIT参数

#### 环境变量加载
- 优先级: 当前工作目录.env > 项目根目录.env
- 使用Pydantic Settings进行管理
- 支持运行时动态更新

### 系统特色功能

1. **多智能体协作**: 5个独立引擎协同工作
2. **实时监控论坛**: ForumEngine提供AI主持的讨论环境
3. **智能聚类分析**: 使用ML算法优化搜索结果
4. **多语言支持**: 支持22种语言的情感分析
5. **灵活的LLM集成**: 支持多种LLM API提供商
6. **完整报告系统**: 自动生成多格式分析报告

### 性能优化措施

1. **异步处理**: 使用gevent/eventlet提升并发性能
2. **懒加载**: 聚类模型等大模型懒加载
3. **缓存机制**: 配置缓存、搜索结果缓存
4. **资源管理**: 自动清理、超时控制
5. **并发控制**: 避免同时执行多个重任务

### 一次完整分析流程

| 步骤 | 阶段名称 | 主要操作 | 参与组件 | 循环特性 |
|------|----------|----------|----------|----------|
| 1 | 用户提问 | Flask主应用接收查询 | Flask主应用 | - |
| 2 | 并行启动 | 三个Agent同时开始工作 | Query Agent、Media Agent、Insight Agent | - |
| 3 | 初步分析 | 各Agent使用专属工具进行概览搜索 | 各Agent + 专属工具集 | - |
| 4 | 策略制定 | 基于初步结果制定分块研究策略 | 各Agent内部决策模块 | - |
| 5-N | **循环阶段** | **论坛协作 + 深度研究** | **ForumEngine + 所有Agent** | **多轮循环** |
| 5.1 | 深度研究 | 各Agent基于论坛主持人引导进行专项搜索 | 各Agent + 反思机制 + 论坛引导 | 每轮循环 |
| 5.2 | 论坛协作 | ForumEngine监控Agent发言并生成主持人引导 | ForumEngine + LLM主持人 | 每轮循环 |
| 5.3 | 交流融合 | 各Agent根据讨论调整研究方向 | 各Agent + forum_reader工具 | 每轮循环 |
| N+1 | 结果整合 | Report Agent收集所有分析结果和论坛内容 | Report Agent | - |
| N+2 | IR中间表示 | 动态选择模板和样式，多轮生成元数据，装订为IR中间表示 | Report Agent + 模板引擎 | - |
| N+3 | 报告生成 | 分块进行质量检测，基于IR渲染成交互式 HTML 报告 | Report Agent + 装订引擎 | - |

### 项目代码结构树

```
BettaFish/
├── QueryEngine/                            # 国内外新闻广度搜索Agent
│   ├── agent.py                            # Agent主逻辑，协调搜索与分析流程
│   ├── llms/                               # LLM接口封装
│   ├── nodes/                              # 处理节点：搜索、格式化、总结等
│   ├── tools/                              # 国内外新闻搜索工具集
│   ├── utils/                              # 工具函数
│   ├── state/                              # 状态管理
│   ├── prompts/                            # 提示词模板
│   └── ...
├── MediaEngine/                            # 强大的多模态理解Agent
│   ├── agent.py                            # Agent主逻辑，处理视频/图片等多模态内容
│   ├── llms/                               # LLM接口封装
│   ├── nodes/                              # 处理节点：搜索、格式化、总结等
│   ├── tools/                              # 多模态搜索工具集
│   ├── utils/                              # 工具函数
│   ├── state/                              # 状态管理
│   ├── prompts/                            # 提示词模板
│   └── ...
├── InsightEngine/                          # 私有数据库挖掘Agent
│   ├── agent.py                            # Agent主逻辑，协调数据库查询与分析
│   ├── llms/                               # LLM接口封装
│   │   └── base.py                         # 统一的OpenAI兼容客户端
│   ├── nodes/                              # 处理节点：搜索、格式化、总结等
│   │   ├── base_node.py                    # 基础节点类
│   │   ├── search_node.py                  # 搜索节点
│   │   ├── formatting_node.py              # 格式化节点
│   │   ├── report_structure_node.py        # 报告结构节点
│   │   └── summary_node.py                 # 总结节点
│   ├── tools/                              # 数据库查询和分析工具集
│   │   ├── keyword_optimizer.py            # Qwen关键词优化中间件
│   │   ├── search.py                       # 数据库操作工具集（话题搜索、评论获取等）
│   │   └── sentiment_analyzer.py           # 情感分析集成工具
│   ├── utils/                              # 工具函数
│   │   ├── config.py                       # 配置管理
│   │   ├── db.py                           # SQLAlchemy异步引擎与只读查询封装
│   │   └── text_processing.py              # 文本处理工具
│   ├── state/                              # 状态管理
│   │   └── state.py                        # Agent状态定义
│   ├── prompts/                            # 提示词模板
│   │   └── prompts.py                      # 各类提示词
│   └── __init__.py
├── ReportEngine/                           # 多轮报告生成Agent
│   ├── agent.py                            # 总调度器：模板选择→布局→篇幅→章节→渲染
│   ├── flask_interface.py                  # Flask/SSE入口，管理任务排队与流式事件
│   ├── llms/                               # OpenAI兼容LLM封装
│   │   └── base.py                         # 统一的流式/重试客户端
│   ├── core/                               # 核心功能：模板解析、章节存储、文档装订
│   │   ├── template_parser.py              # Markdown模板切片与slug生成
│   │   ├── chapter_storage.py              # 章节run目录、manifest与raw流写入
│   │   └── stitcher.py                     # Document IR装订器，补齐锚点/元数据
│   ├── ir/                                 # 报告中间表示（IR）契约与校验
│   │   ├── schema.py                       # 块/标记Schema常量定义
│   │   └── validator.py                    # 章节JSON结构校验器
│   ├── nodes/                              # 全流程推理节点
│   │   ├── base_node.py                    # 节点基类+日志/状态钩子
│   │   ├── template_selection_node.py      # 模板候选收集与LLM筛选
│   │   ├── document_layout_node.py         # 标题/目录/主题设计
│   │   ├── word_budget_node.py             # 篇幅规划与章节指令生成
│   │   └── chapter_generation_node.py      # 章节级JSON生成+校验
│   ├── prompts/                            # 提示词库与Schema说明
│   │   └── prompts.py                      # 模板选择/布局/篇幅/章节提示词
│   ├── renderers/                          # IR渲染器
│   │   ├── html_renderer.py                # Document IR→交互式HTML
│   │   ├── pdf_renderer.py                 # HTML→PDF导出（WeasyPrint）
│   │   ├── pdf_layout_optimizer.py         # PDF布局优化器
│   │   └── chart_to_svg.py                 # 图表转SVG工具
│   ├── state/                              # 任务/元数据状态模型
│   │   └── state.py                        # ReportState与序列化工具
│   ├── utils/                              # 配置与辅助工具
│   │   ├── config.py                       # Pydantic Settings与打印助手
│   │   ├── dependency_check.py             # 依赖检查工具
│   │   ├── json_parser.py                  # JSON解析工具
│   │   ├── chart_validator.py              # 图表校验工具
│   │   └── chart_repair_api.py             # 图表修复API
│   ├── report_template/                    # Markdown模板库
│   │   ├── 企业品牌声誉分析报告.md
│   │   └── ...
│   └── __init__.py
├── ForumEngine/                            # 论坛引擎：Agent协作机制
│   ├── monitor.py                          # 日志监控和论坛管理核心
│   ├── llm_host.py                         # 论坛主持人LLM模块
│   └── __init__.py
├── MindSpider/                             # 社交媒体爬虫系统
│   ├── main.py                             # 爬虫主程序入口
│   ├── config.py                           # 爬虫配置文件
│   ├── BroadTopicExtraction/               # 话题提取模块
│   │   ├── main.py                         # 话题提取主程序
│   │   ├── database_manager.py             # 数据库管理器
│   │   ├── get_today_news.py               # 今日新闻获取
│   │   └── topic_extractor.py              # 话题提取器
│   ├── DeepSentimentCrawling/              # 深度舆情爬取模块
│   │   ├── main.py                         # 深度爬取主程序
│   │   ├── keyword_manager.py              # 关键词管理器
│   │   ├── platform_crawler.py             # 平台爬虫管理
│   │   └── MediaCrawler/                   # 社媒爬虫核心
│   │       ├── main.py
│   │       ├── config/                     # 各平台配置
│   │       ├── media_platform/             # 各平台爬虫实现
│   │       └── ...
│   └── schema/                             # 数据库结构定义
│       ├── db_manager.py                   # 数据库管理器
│       ├── init_database.py                # 数据库初始化脚本
│       ├── mindspider_tables.sql           # 数据库表结构SQL
│       ├── models_bigdata.py               # 大规模媒体舆情表的SQLAlchemy映射
│       └── models_sa.py                    # DailyTopic/Task等扩展表ORM模型
├── SentimentAnalysisModel/                 # 情感分析模型集合
│   ├── WeiboSentiment_Finetuned/           # 微调BERT/GPT-2模型
│   │   ├── BertChinese-Lora/               # BERT中文LoRA微调
│   │   │   ├── train.py
│   │   │   ├── predict.py
│   │   │   └── ...
│   │   └── GPT2-Lora/                      # GPT-2 LoRA微调
│   │       ├── train.py
│   │       ├── predict.py
│   │       └── ...
│   ├── WeiboMultilingualSentiment/         # 多语言情感分析
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── ...
│   ├── WeiboSentiment_SmallQwen/           # 小参数Qwen3微调
│   │   ├── train.py
│   │   ├── predict_universal.py
│   │   └── ...
│   └── WeiboSentiment_MachineLearning/     # 传统机器学习方法
│       ├── train.py
│       ├── predict.py
│       └── ...
├── SingleEngineApp/                        # 单独Agent的Streamlit应用
│   ├── query_engine_streamlit_app.py       # QueryEngine独立应用
│   ├── media_engine_streamlit_app.py       # MediaEngine独立应用
│   └── insight_engine_streamlit_app.py     # InsightEngine独立应用
├── query_engine_streamlit_reports/         # QueryEngine单应用运行输出
├── media_engine_streamlit_reports/         # MediaEngine单应用运行输出
├── insight_engine_streamlit_reports/       # InsightEngine单应用运行输出
├── templates/                              # Flask前端模板
│   └── index.html                          # 主界面HTML
├── static/                                 # 静态资源
│   └── image/                              # 图片资源
│       ├── logo_compressed.png
│       ├── framework.png
│       └── ...
├── logs/                                   # 运行日志目录
├── final_reports/                          # 最终生成的报告文件
│   ├── ir/                                 # 报告IR JSON文件
│   └── *.html                              # 最终HTML报告
├── utils/                                  # 通用工具函数
│   ├── forum_reader.py                     # Agent间论坛通信工具
│   ├── github_issues.py                    # 统一生成GitHub Issue链接与错误提示
│   └── retry_helper.py                     # 网络请求重试机制工具
├── tests/                                  # 单元测试与集成测试
│   ├── run_tests.py                        # pytest入口脚本
│   ├── test_monitor.py                     # ForumEngine监控单元测试
│   ├── test_report_engine_sanitization.py  # ReportEngine安全性测试
│   └── ...
├── app.py                                  # Flask主应用入口
├── config.py                               # 全局配置文件
├── .env.example                            # 环境变量示例文件
├── docker-compose.yml                      # Docker多服务编排配置
├── Dockerfile                              # Docker镜像构建文件
├── requirements.txt                        # Python依赖包清单
├── regenerate_latest_pdf.py                # PDF重新生成工具脚本
├── report_engine_only.py                   # Report Engine命令行版本
├── README.md                               # 中文说明文档
├── README-EN.md                            # 英文说明文档
├── CONTRIBUTING.md                         # 中文贡献指南
├── CONTRIBUTING-EN.md                      # 英文贡献指南
└── LICENSE                                 # GPL-2.0开源许可证
```

## 🚀 快速开始（Docker）

### 1. 启动项目

复制一份 `.env.example` 文件，命名为 `.env` ，并按需配置 `.env` 文件中的环境变量

执行以下命令在后台启动所有服务：

```bash
docker compose up -d
```

> **注：镜像拉取速度慢**，在原 `docker-compose.yml` 文件中，我们已经通过**注释**的方式提供了备用镜像地址供您替换

### 2. 配置说明

#### 数据库配置（PostgreSQL）

请按照以下参数配置数据库连接信息，也支持Mysql可自行修改：

| 配置项 | 填写值 | 说明 |
| :--- | :--- | :--- |
| `DB_HOST` | `db` | 数据库服务名称 (对应 `docker-compose.yml` 中的服务名) |
| `DB_PORT` | `5432` | 默认 PostgreSQL 端口 |
| `DB_USER` | `bettafish` | 数据库用户名 |
| `DB_PASSWORD` | `bettafish` | 数据库密码 |
| `DB_NAME` | `bettafish` | 数据库名称 |
| **其他** | **保持默认** | 数据库连接池等其他参数请保持默认设置。 |

#### 大模型配置

> 我们所有 LLM 调用使用 OpenAI 的 API 接口标准

在完成数据库配置后，请正常配置**所有大模型相关的参数**，确保系统能够连接到您选择的大模型服务。

完成上述所有配置并保存后，系统即可正常运行。

## 🔧 源码启动指南

> 如果你是初次学习一个Agent系统的搭建，可以从一个非常简单的demo开始：[Deep Search Agent Demo](https://github.com/666ghj/DeepSearchAgent-Demo)

### 环境要求

- **操作系统**: Windows、Linux、MacOS
- **Python版本**: 3.9+
- **Conda**: Anaconda或Miniconda
- **数据库**: PostgreSQL（推荐）或MySQL
- **内存**: 建议2GB以上

### 1. 创建环境

#### 如果使用Conda

```bash
# 创建conda环境
conda create -n your_conda_name python=3.11
conda activate your_conda_name
```

#### 如果使用uv

```bash
# 创建uv环境
uv venv --python 3.11 # 创建3.11环境
```

### 2. 安装 PDF 导出所需系统依赖（可选）

这部分有详细的配置说明：[配置所需依赖](./static/Partial%20README%20for%20PDF%20Exporting/README.md)

### 3. 安装依赖包

> 如果跳过了步骤2，weasyprint库可能无法安装，PDF功能可能无法正常使用。

```bash
# 基础依赖安装
pip install -r requirements.txt

# uv版本命令（更快速安装）
uv pip install -r requirements.txt
# 如果不想使用本地情感分析模型（算力需求很小，默认安装cpu版本），可以将该文件中的"机器学习"部分注释掉再执行指令
```

### 4. 安装Playwright浏览器驱动

```bash
# 安装浏览器驱动（用于爬虫功能）
playwright install chromium
```

### 5. 配置LLM与数据库

复制一份项目根目录 `.env.example` 文件，命名为 `.env`

编辑 `.env` 文件，填入您的API密钥（您也可以选择自己的模型、搜索代理，详情见根目录.env.example文件内或根目录config.py中的说明）：

```yml
# ====================== 数据库配置 ======================
# 数据库主机，例如localhost 或 127.0.0.1
DB_HOST=your_db_host
# 数据库端口号，默认为3306
DB_PORT=3306
# 数据库用户名
DB_USER=your_db_user
# 数据库密码
DB_PASSWORD=your_db_password
# 数据库名称
DB_NAME=your_db_name
# 数据库字符集，推荐utf8mb4，兼容emoji
DB_CHARSET=utf8mb4
# 数据库类型postgresql或mysql
DB_DIALECT=postgresql
# 数据库不需要初始化，执行app.py时会自动检测

# ====================== LLM配置 ======================
# 您可以更改每个部分LLM使用的API，只要兼容OpenAI请求格式都可以
# 配置文件内部给了每一个Agent的推荐LLM，初次部署请先参考推荐设置

# Insight Agent
INSIGHT_ENGINE_API_KEY=
INSIGHT_ENGINE_BASE_URL=
INSIGHT_ENGINE_MODEL_NAME=

# Media Agent
...
```

### 6. 启动系统

#### 6.1 完整系统启动（推荐）

```bash
# 在项目根目录下，激活conda环境
conda activate your_conda_name

# 启动主应用即可
python app.py
```

uv 版本启动命令 
```bash
# 在项目根目录下，激活uv环境
.venv\Scripts\activate

# 启动主应用即可
python app.py
```

> 注1：一次运行终止后，streamlit app可能结束异常仍然占用端口，此时搜索占用端口的进程kill掉即可

> 注2：数据爬取需要单独操作，见6.3指引

访问 http://localhost:5000 即可使用完整系统

#### 6.2 单独启动某个Agent

```bash
# 启动QueryEngine
streamlit run SingleEngineApp/query_engine_streamlit_app.py --server.port 8503

# 启动MediaEngine  
streamlit run SingleEngineApp/media_engine_streamlit_app.py --server.port 8502

# 启动InsightEngine
streamlit run SingleEngineApp/insight_engine_streamlit_app.py --server.port 8501
```

#### 6.3 爬虫系统单独使用

这部分有详细的配置文档：[MindSpider使用说明](./MindSpider/README.md)

<div align="center">
<img src="MindSpider\img\example.png" alt="banner" width="600">

MindSpider 运行示例
</div>

```bash
# 进入爬虫目录
cd MindSpider

# 项目初始化
python main.py --setup

# 运行话题提取（获取热点新闻和关键词）
python main.py --broad-topic

# 运行完整爬虫流程
python main.py --complete --date 2024-01-20

# 仅运行话题提取
python main.py --broad-topic --date 2024-01-20

# 仅运行深度爬取
python main.py --deep-sentiment --platforms xhs dy wb
```

#### 6.4 命令行报告生成工具

该工具会跳过三个分析引擎的运行阶段，直接读取它们的最新日志文件，并在无需 Web 界面的情况下生成综合报告（同时省略文件增量校验步骤）。通常用于对报告生成结果不满意、需要快速重试的场景，或在调试 Report Engine 时启用。

```bash
# 基本使用（自动从文件名提取主题）
python report_engine_only.py

# 指定报告主题
python report_engine_only.py --query "土木工程行业分析"

# 跳过PDF生成（即使系统支持）
python report_engine_only.py --skip-pdf

# 显示详细日志
python report_engine_only.py --verbose

# 查看帮助信息
python report_engine_only.py --help
```

**功能说明：**

1. **自动检查依赖**：程序会自动检查PDF生成所需的系统依赖，如果缺失会给出安装提示
2. **获取最新文件**：自动从三个引擎目录（`insight_engine_streamlit_reports`、`media_engine_streamlit_reports`、`query_engine_streamlit_reports`）获取最新的分析报告
3. **文件确认**：显示所有选择的文件名、路径和修改时间，等待用户确认（默认输入 `y` 继续，输入 `n` 退出）
4. **直接生成报告**：跳过文件增加审核程序，直接调用Report Engine生成综合报告
5. **自动保存文件**：
   - HTML报告保存到 `final_reports/` 目录
   - PDF报告（如果有依赖）保存到 `final_reports/pdf/` 目录
   - 文件命名格式：`final_report_{主题}_{时间戳}.html/pdf`

**注意事项：**

- 确保三个引擎目录中至少有一个包含`.md`报告文件
- 命令行工具与Web界面相互独立，不会相互影响
- PDF生成需要安装系统依赖，详见上文"安装 PDF 导出所需系统依赖"部分

## ⚙️ 高级配置（已过时，已经统一为项目根目录.env文件管理，其他子agent自动继承根目录配置）

### 代码执行细节

#### Flask应用初始化细节
```python
# app.py 核心初始化代码
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Dedicated-to-creating-a-concise-and-versatile-public-opinion-analysis-platform'

# 异步模式智能选择
try:
    import gevent
    async_mode = 'gevent'
except ImportError:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        async_mode = 'threading'

socketio = SocketIO(app, cors_allowed_origins="*", async_mode=async_mode)
```

#### 进程管理机制
- 子进程管理字典 (processes:516)
- 输出队列系统 (output_queues:545)
- 健康检查机制 (check_app_status:767)
- 优雅关闭流程 (cleanup_processes_concurrent:833)

#### 日志监控实现
```python
# ForumEngine监控目标
target_node_patterns = [
    'FirstSummaryNode',
    'ReflectionSummaryNode',
    'InsightEngine.nodes.summary_node',
    'MediaEngine.nodes.summary_node',
    'QueryEngine.nodes.summary_node',
    '正在生成首次段落总结',
    '正在生成反思总结',
]
```

### 修改关键参数

#### Agent配置参数

每个Agent都有专门的配置文件，可根据需求调整，下面是部分示例：

```python
# QueryEngine/utils/config.py
class Config:
    max_reflections = 2           # 反思轮次
    max_search_results = 15       # 最大搜索结果数
    max_content_length = 8000     # 最大内容长度
    
# MediaEngine/utils/config.py  
class Config:
    comprehensive_search_limit = 10  # 综合搜索限制
    web_search_limit = 15           # 网页搜索限制
    
# InsightEngine/utils/config.py
class Config:
    default_search_topic_globally_limit = 200    # 全局搜索限制
    default_get_comments_limit = 500             # 评论获取限制
    max_search_results_for_llm = 50              # 传给LLM的最大结果数
```

#### 情感分析模型配置

```python
# InsightEngine/tools/sentiment_analyzer.py
SENTIMENT_CONFIG = {
    'model_type': 'multilingual',     # 可选: 'bert', 'multilingual', 'qwen'等
    'confidence_threshold': 0.8,      # 置信度阈值
    'batch_size': 32,                 # 批处理大小
    'max_sequence_length': 512,       # 最大序列长度
}
```

### 接入不同的LLM模型

支持任意openAI调用格式的LLM提供商，只需要在/config.py中填写对应的KEY、BASE_URL、MODEL_NAME即可。

> 什么是openAI调用格式？下面提供一个简单的例子：
>```python
>from openai import OpenAI
>
>client = OpenAI(api_key="your_api_key", 
>                base_url="https://api.siliconflow.cn/v1")
>
>response = client.chat.completions.create(
>    model="Qwen/Qwen2.5-72B-Instruct",
>    messages=[
>        {'role': 'user', 
>         'content': "推理模型会给市场带来哪些新的机会"}
>    ],
>)
>
>complete_response = response.choices[0].message.content
>print(complete_response)
>```

### 更改情感分析模型

系统集成了多种情感分析方法，可根据需求选择：

#### 1. 多语言情感分析

```bash
cd SentimentAnalysisModel/WeiboMultilingualSentiment
python predict.py --text "This product is amazing!" --lang "en"
```

#### 2. 小参数Qwen3微调

```bash
cd SentimentAnalysisModel/WeiboSentiment_SmallQwen
python predict_universal.py --text "这次活动办得很成功"
```

#### 3. 基于BERT的微调模型

```bash
# 使用BERT中文模型
cd SentimentAnalysisModel/WeiboSentiment_Finetuned/BertChinese-Lora
python predict.py --text "这个产品真的很不错"
```

#### 4. GPT-2 LoRA微调模型

```bash
cd SentimentAnalysisModel/WeiboSentiment_Finetuned/GPT2-Lora
python predict.py --text "今天心情不太好"
```

#### 5. 传统机器学习方法

```bash
cd SentimentAnalysisModel/WeiboSentiment_MachineLearning
python predict.py --model_type "svm" --text "服务态度需要改进"
```

### 接入自定义业务数据库

#### 1. 修改数据库连接配置

```python
# config.py 中添加您的业务数据库配置
BUSINESS_DB_HOST = "your_business_db_host"
BUSINESS_DB_PORT = 3306
BUSINESS_DB_USER = "your_business_user"
BUSINESS_DB_PASSWORD = "your_business_password"
BUSINESS_DB_NAME = "your_business_database"
```

#### 2. 创建自定义数据访问工具

```python
# InsightEngine/tools/custom_db_tool.py
class CustomBusinessDBTool:
    """自定义业务数据库查询工具"""
    
    def __init__(self):
        self.connection_config = {
            'host': config.BUSINESS_DB_HOST,
            'port': config.BUSINESS_DB_PORT,
            'user': config.BUSINESS_DB_USER,
            'password': config.BUSINESS_DB_PASSWORD,
            'database': config.BUSINESS_DB_NAME,
        }
    
    def search_business_data(self, query: str, table: str):
        """查询业务数据"""
        # 实现您的业务逻辑
        pass
    
    def get_customer_feedback(self, product_id: str):
        """获取客户反馈数据"""
        # 实现客户反馈查询逻辑
        pass
```

#### 3. 集成到InsightEngine

```python
# InsightEngine/agent.py 中集成自定义工具
from .tools.custom_db_tool import CustomBusinessDBTool

class DeepSearchAgent:
    def __init__(self, config=None):
        # ... 其他初始化代码
        self.custom_db_tool = CustomBusinessDBTool()
    
    def execute_custom_search(self, query: str):
        """执行自定义业务数据搜索"""
        return self.custom_db_tool.search_business_data(query, "your_table")
```

### 自定义报告模板

#### 1. 在Web界面中上传

系统支持上传自定义模板文件（.md或.txt格式），可在生成报告时选择使用。

#### 2. 创建模板文件

在 `ReportEngine/report_template/` 目录下创建新的模板，我们的Agent会自行选用最合适的模板。

## 免费搜索替代方案分析报告

       1. 搜索引擎API方案

       Google Custom Search API

       - 免费额度：100次/天（免费层级），$5/1000次的付费层级        
       - API调用难度：中等（需要API密钥，有使用配额）
       - 中文支持：优秀，原生中文搜索支持
       - 数据质量：高，Google搜索结果质量好
       - 实时性：实时更新，索引速度快
       - 法律合规性：✅ 良好，Google在合规方面做得较好
       - 适合度：⭐⭐⭐⭐⭐ 适合作为主要搜索引擎补充

       Bing Search API

       - 免费额度：1000次/月（免费层级），付费层级更高
       - API调用难度：中等（Azure密钥配置）
       - 中文支持：良好，对中文内容支持不错
       - 数据质量：中高，Bing搜索质量持续改进
       - 实时性：良好，更新频率适中
       - 法律合规性：✅ 良好，微软合规要求严格
       - 适合度：⭐⭐⭐⭐⭐ 适合作为备选搜索引擎

       SearxNG（开源）

       - 免费额度：无限制（自托管，硬件限制）
       - API调用难度：高（需要自建和维护服务器）
       - 中文支持：中等（取决于后端搜索引擎）
       - 数据质量：中低（聚合多个搜索结果，质量参差不齐）
       - 实时性：一般，取决于聚合的搜索引擎
       - 法律合规性：✅ 优秀，开源透明，无商业限制
       - 适合度：⭐⭐⭐ 自建技术门槛高，但长期成本低

       2. 社交媒体专用API方案

       微博开放平台API

       - 免费额度：有限制（具体额度不公开，通常较低）
       - API调用难度：高（需要企业资质审核）
       - 中文支持：❌ 仅限官方内容，难以获取用户生成内容
       - 数据质量：中低，官方数据有限
       - 实时性：良好，官方更新及时
       - 法律合规性：❌ 个人开发者难以获得资质
       - 适合度：⭐ 不适合独立开发者

       B站开放API

       - 免费额度：100-300次/分钟
       - API调用难度：中等（需要OAuth认证）
       - 中文支持：❌ 仅限官方接口，爬虫策略受限
       - 数据质量：中低，数据获取受限
       - 实时性：良好，但API限制严格
       - 法律合规性：❌ 违规使用可能被封禁
       - 适合度：⭐⭐ 技术可行但风险较高

       知乎开放API

       - 免费额度：100-200请求/小时
       - API调用难度：高（需要中国身份认证）
       - 中文支持：❌ 个人开发者难以注册
       - 数据质量：高，但获取难度大
       - 实时性：良好，但官方API限制多
       - 法律合规性：❌ 对海外开发者不友好
       - 适合度：⭐ 不适合海外团队

       Reddit API

       - 免费额度：100次/天（2025年新限制）
       - API调用难度：中等（OAuth认证，PRAW库支持）
       - 中文支持：❌ 主要是英文内容
       - 数据质量：中高，但英文为主
       - 实时性：良好，更新及时
       - 法律合规性：✅ 允许API使用
       - 适合度：⭐⭐ 适合国际化内容补充

       3. 其他解决方案

       RSS聚合搜索

       - 免费额度：无限制（取决于RSS源数量）
       - API调用难度：低（feedparser等库成熟）
       - 中文支持：✅ 优秀，支持中文RSS
       - 数据质量：中高，取决于RSS源质量
       - 实时性：一般，依赖RSS更新频率
       - 法律合规性：✅ RSS为公开内容，合法使用
       - 适合度：⭐⭐⭐⭐✨ 推荐作为内容源补充

       Telegram Bot API

       - 免费额度：30消息/秒/用户，无总量限制
       - API调用难度：低（成熟API，官方文档完善）
       - 中文支持：✅ 优秀，支持中文频道
       - 数据质量：中高，内容质量取决于频道质量
       - 实时性：优秀，几乎实时推送
       - 法律合规性：✅ 合法使用，但需遵守平台规则
       - 适合度：⭐⭐⭐⭐ 适合特定内容监控

       Scrapy框架

       - 免费额度：无限制（自己控制）
       - API调用难度：高（需要处理反爬、验证码等）
       - 中文支持：✅ 优秀，支持中文编码
       - 数据质量：高，但需要大量维护工作
       - 实时性：一般，受限于爬取频率
       - 法律合规性：❌ 侵权风险高，尤其在国内网站
       - 适合度：⭐⭐ 技术可行但法律风险高

       🎯 推荐集成方案

       方案一：混合API架构（推荐）

       主引擎组合：
       1. Bing Search API (1000次/月免费) - 主要搜索引擎
       2. RSS聚合 - 补充内容源
       3. Telegram Bot API - 特定频道监控

       优点：
       - 免费额度充足，覆盖主要需求
       - 技术实现难度适中
       - 法律合规性良好
       - 数据源多样化

       方案二：自建SearxNG + RSS

       自建组件：
       1. SearxNG实例 - 搜索引擎聚合
       2. RSS聚合器 - 新闻和博客
       3. 定时爬虫（合规网站）- 补充数据

       优点：
       - 零成本运行
       - 数据完全可控
       - 长期维护成本低

       方案三：开源替代方案

       开源组件：
       1. DuckDuckGo Instant Answer API
       2. Wikipedia API
       3. NewsAPI.org (有免费层级)
       4. 国内开源数据源（如：今日热榜API）

       🚀 实施建议

       1. 短期实施（1-2周）：
         - 集成Bing Search API和RSS聚合
         - 测试数据质量和覆盖率
       2. 中期扩展（1-2月）：
         - 添加Telegram频道监控
         - 实现RSS源自动发现和添加
       3. 长期优化（3-6月）：
         - 考虑自建SearxNG实例
         - 开发专用的中文搜索引擎插件

       ⚠️ 注意事项

       1. API调用策略：
         - 实现请求缓存，减少API调用
         - 使用异步请求提高效率
         - 设置合理的重试机制
       2. 数据质量保证：
         - 多源数据交叉验证
         - 实现去重和质量评分
         - 建立数据清洗流程
       3. 法律合规性：
         - 遵守各平台API使用条款
         - 尊重robots.txt协议
         - 合理控制请求频率

       这个方案既考虑了免费限制，又确保了系统的稳定性和扩展性，     
       特别适合BettaFish项目的舆情分析需求。

## 🤝 贡献指南

我们欢迎所有形式的贡献！

**请阅读以下贡献指南：**  
- [CONTRIBUTING.md](./CONTRIBUTING.md)

## 🦖 下一步开发计划

现在系统只完成了"三板斧"中的前两步，即：输入要求->详细分析，还缺少一步预测，直接将他继续交给LLM是不具有说服力的。

<div align="center">
<img src="static/image/banner_compressed.png" alt="banner" width="800">
</div>

目前我们经过很长一段时间的爬取收集，拥有了大量全网话题热度随时间、爆点等的变化趋势热度数据，已经具备了可以开发预测模型的条件。我们团队将运用时序模型、图神经网络、多模态融合等预测模型技术储备于此，实现真正基于数据驱动的舆情预测功能。

## ⚠️ 免责声明

**重要提醒：本项目仅供学习、学术研究和教育目的使用**

1. **合规性声明**：
   - 本项目中的所有代码、工具和功能均仅供学习、学术研究和教育目的使用
   - 严禁将本项目用于任何商业用途或盈利性活动
   - 严禁将本项目用于任何违法、违规或侵犯他人权益的行为

2. **爬虫功能免责**：
   - 项目中的爬虫功能仅用于技术学习和研究目的
   - 使用者必须遵守目标网站的robots.txt协议和使用条款
   - 使用者必须遵守相关法律法规，不得进行恶意爬取或数据滥用
   - 因使用爬虫功能产生的任何法律后果由使用者自行承担

3. **数据使用免责**：
   - 项目涉及的数据分析功能仅供学术研究使用
   - 严禁将分析结果用于商业决策或盈利目的
   - 使用者应确保所分析数据的合法性和合规性

4. **技术免责**：
   - 本项目按"现状"提供，不提供任何明示或暗示的保证
   - 作者不对使用本项目造成的任何直接或间接损失承担责任
   - 使用者应自行评估项目的适用性和风险

5. **责任限制**：
   - 使用者在使用本项目前应充分了解相关法律法规
   - 使用者应确保其使用行为符合当地法律法规要求
   - 因违反法律法规使用本项目而产生的任何后果由使用者自行承担

**请在使用本项目前仔细阅读并理解上述免责声明。使用本项目即表示您已同意并接受上述所有条款。**

## 📄 许可证

本项目采用 [GPL-2.0许可证](LICENSE)。详细信息请参阅LICENSE文件。

## 🎉 支持与联系

### 获取帮助

常见问题解答：https://github.com/666ghj/BettaFish/issues/185

- **项目主页**：[GitHub仓库](https://github.com/666ghj/BettaFish)
- **问题反馈**：[Issues页面](https://github.com/666ghj/BettaFish/issues)
- **功能建议**：[Discussions页面](https://github.com/666ghj/BettaFish/discussions)

### 联系方式

- 📧 **邮箱**：hangjiang@bupt.edu.cn

### 商务合作

- **企业定制开发**
- **大数据服务**
- **学术合作**
- **技术培训**

## 👥 贡献者

感谢以下优秀的贡献者们：

[![Contributors](https://contrib.rocks/image?repo=666ghj/BettaFish)](https://github.com/666ghj/BettaFish/graphs/contributors)

## 🌟 加入官方交流群

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=欢迎加入我们的技术交流QQ群！&fontSize=40&fontAlignY=35&desc=扫描下方二维码加入群聊&descAlignY=55" alt="欢迎加入我们的技术交流QQ群！" style="width:60%; max-width:900px; display:block; margin:0 auto;">
  <img src="static/image/QQ_Light_Horizenal.png" alt="BettaFish 技术交流群二维码" style="width:60%; max-width:360px; display:block; margin:20px auto 0;">
</div>

## 📈 项目统计

<a href="https://www.star-history.com/#666ghj/BettaFish&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=666ghj/BettaFish&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=666ghj/BettaFish&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=666ghj/BettaFish&type=date&legend=top-left" />
 </picture>
</a>

![Alt](https://repobeats.axiom.co/api/embed/e04e3eea4674edc39c148a7845c8d09c1b7b1922.svg "Repobeats analytics image")

---

## 📐 架构设计总结

BettaFish的架构设计体现了现代AI应用的**微服务**、**多智能体**、**实时交互**等特点：

### 核心设计原则
1. **模块化设计**: 各引擎独立部署，高内聚低耦合
2. **异步处理**: 基于WebSocket的实时通信与异步任务处理
3. **可扩展性**: 支持自定义引擎、工具和LLM集成
4. **智能化**: AI主持人促进多智能体协作，提升集体智能

### 技术亮点
- **智能异步模式选择**: 自动选择gevent/eventlet/threading
- **多引擎协同工作**: 通过ForumEngine实现智能协作
- **完整的监控体系**: 实时日志监控与状态同步
- **灵活的配置管理**: 基于Pydantic的动态配置系统

这个架构不仅实现了高效的舆情分析能力，更为未来的功能扩展和性能优化奠定了坚实的基础。
