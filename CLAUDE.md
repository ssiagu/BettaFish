# BettaFish - 微博舆情分析多智能体系统

**项目类型**: 微博舆情分析多智能体系统
**技术栈**: Python 3.11, Flask, Streamlit, Pydantic
**初始化时间**: 2025-12-08 15:52:05
**作者**: ssiagu <ssiagu@gmail.com>

## 🎯 项目概述

BettaFish是一个基于多智能体架构的微博舆情分析系统，提供洞察发现、媒体分析、信息查询和报告生成等核心功能。系统采用微服务架构设计，各引擎模块独立运作又相互配合，支持实时数据处理和智能分析。

## 🏗️ 系统架构

```mermaid
graph TB
    subgraph "前端层"
        A[Flask主应用 app.py] --> B[洞察引擎 Streamlit]
        A --> C[媒体引擎 Streamlit]
        A --> D[查询引擎 Streamlit]
    end

    subgraph "核心引擎层"
        E[InsightEngine<br/>洞察引擎] --> F[Deep Search Agent]
        G[MediaEngine<br/>媒体引擎] --> H[多模态内容处理]
        I[QueryEngine<br/>查询引擎] --> J[Tavily新闻搜索]
        K[ReportEngine<br/>报告引擎] --> L[智能报告生成]
        M[ForumEngine<br/>论坛引擎] --> N[论坛监控]
    end

    subgraph "辅助模块层"
        O[MindSpider<br/>心智蜘蛛] --> P[主题提取]
        O --> Q[情感爬取]
        R[SentimentAnalysisModel<br/>情感分析模型] --> S[BERT主题检测]
        R --> T[多语言情感分析]
    end

    subgraph "基础设施层"
        U[数据库<br/>PostgreSQL/MySQL]
        V[缓存<br/>Redis]
        W[文件存储]
        X[外部API<br/>OpenAI/Kimi/Gemini]
    end

    B --> E
    C --> G
    D --> I
    E --> O
    G --> O
    I --> K
    K --> R
    E --> U
    G --> U
    I --> V
    K --> W
    E --> X
```

## 📦 核心模块索引

### 1. InsightEngine (洞察引擎)
- **路径**: `InsightEngine/`
- **功能**: 深度搜索与智能洞察
- **核心文件**: `agent.py`, `nodes/`, `tools/`, `llms/`
- **导航**: [InsightEngine详细说明](InsightEngine/CLAUDE.md)

### 2. MediaEngine (媒体引擎)
- **路径**: `MediaEngine/`
- **功能**: 多媒体内容处理与分析
- **核心文件**: `agent.py`, `tools/`, `nodes/`
- **导航**: [MediaEngine详细说明](MediaEngine/CLAUDE.md)

### 3. QueryEngine (查询引擎)
- **路径**: `QueryEngine/`
- **功能**: 基于Tavily的新闻搜索与信息检索
- **核心文件**: `agent.py`, `tools/`
- **导航**: [QueryEngine详细说明](QueryEngine/CLAUDE.md)

### 4. ReportEngine (报告引擎)
- **路径**: `ReportEngine/`
- **功能**: 智能报告生成与导出
- **核心文件**: `agent.py`, `flask_interface.py`, `renderers/`
- **导航**: [ReportEngine详细说明](ReportEngine/CLAUDE.md)

### 5. ForumEngine (论坛引擎)
- **路径**: `ForumEngine/`
- **功能**: 论坛监控与LLM托管
- **核心文件**: `monitor.py`, `llm_host.py`
- **导航**: [ForumEngine详细说明](ForumEngine/CLAUDE.md)

### 6. MindSpider (心智蜘蛛)
- **路径**: `MindSpider/`
- **功能**: 主题提取与深度情感爬取
- **核心文件**: `main.py`, `BroadTopicExtraction/`, `DeepSentimentCrawling/`
- **导航**: [MindSpider详细说明](MindSpider/CLAUDE.md)

### 7. SentimentAnalysisModel (情感分析模型)
- **路径**: `SentimentAnalysisModel/`
- **功能**: 多种情感分析算法集成
- **核心模块**: BERT微调、机器学习方法、多语言支持
- **导航**: [SentimentAnalysisModel详细说明](SentimentAnalysisModel/CLAUDE.md)

## 🚀 快速开始

### 环境要求
- Python 3.11+
- PostgreSQL/MySQL
- Redis (可选)
- Node.js 16+ (用于前端开发)

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/ssiagu/BettaFish.git
cd BettaFish
```

2. **创建虚拟环境**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **配置环境变量**
```bash
cp .env.example .env
# 编辑 .env 文件，填入必要的API密钥和数据库配置
```

5. **初始化数据库**
```bash
python scripts/init_db.py
```

6. **运行应用**
```bash
python app.py
```

### Docker部署

```bash
# 构建并启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f
```

## 📋 开发指南

### 代码规范
- 使用Python类型提示
- 遵循PEP 8代码风格
- 使用Pydantic进行数据验证
- 异步编程使用async/await模式

### 项目结构说明

```
BettaFish/
├── app.py                      # Flask主应用入口
├── config.py                   # 全局配置管理
├── requirements.txt            # Python依赖列表
├── docker-compose.yml          # Docker编排文件
├── .env.example               # 环境变量模板
├── InsightEngine/             # 洞察引擎
├── MediaEngine/               # 媒体引擎
├── QueryEngine/               # 查询引擎
├── ReportEngine/              # 报告引擎
├── ForumEngine/               # 论坛引擎
├── MindSpider/                # 心智蜘蛛
├── SentimentAnalysisModel/    # 情感分析模型
├── SingleEngineApp/           # 单一引擎应用
├── tests/                     # 测试文件
├── docs/                      # 文档
└── scripts/                   # 工具脚本
```

### 测试指南

```bash
# 运行所有测试
pytest

# 运行特定模块测试
pytest tests/test_insight_engine.py

# 生成覆盖率报告
pytest --cov=InsightEngine tests/
```

## 🔌 API接口说明

### WebSocket接口
- `/socket.io/` - 实时数据推送
- 支持事件类型：
  - `search_progress` - 搜索进度更新
  - `analysis_result` - 分析结果推送
  - `error` - 错误通知

### REST API
- `/api/v1/insight/search` - 洞察搜索
- `/api/v1/media/analyze` - 媒体分析
- `/api/v1/query/search` - 信息查询
- `/api/v1/report/generate` - 报告生成

## 🛠️ 配置说明

### 环境变量配置
```env
# 数据库配置
DATABASE_URL=postgresql://user:password@localhost:5432/bettafish
REDIS_URL=redis://localhost:6379/0

# LLM API配置
OPENAI_API_KEY=your_openai_key
KIMI_API_KEY=your_kimi_key
GEMINI_API_KEY=your_gemini_key

# 搜索API配置
TAVILY_API_KEY=your_tavily_key
BOCHA_API_KEY=your_bocha_key
ANSP_API_KEY=your_ansp_key

# 应用配置
FLASK_ENV=development
DEBUG=True
SECRET_KEY=your_secret_key
```

## 📚 模块开发指南

### 创建新引擎模块

1. 在相应目录创建模块文件夹
2. 实现基础Agent类（继承自BaseAgent）
3. 创建nodes/、tools/、llms/等子模块
4. 编写模块CLAUDE.md文档
5. 添加到主应用注册

### 集成外部工具

1. 在对应引擎的tools/目录创建工具文件
2. 继承BaseTool类
3. 实现必要的异步方法
4. 在agent.py中注册工具

## 🚀 部署指南

### 生产环境部署

1. **服务器要求**
   - CPU: 8核以上
   - 内存: 32GB以上
   - 存储: 100GB SSD
   - 网络: 100Mbps以上

2. **配置优化**
   ```env
   FLASK_ENV=production
   DEBUG=False
   WORKERS=4
   MAX_CONNECTIONS=1000
   ```

3. **使用Nginx反向代理**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location /socket.io/ {
           proxy_pass http://127.0.0.1:5000;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
       }
   }
   ```

### 监控和日志

- 使用ELK Stack进行日志收集
- Prometheus + Grafana进行性能监控
- Sentry进行错误追踪

## 🤝 贡献指南

1. Fork项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 📄 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 📞 联系方式

- **作者**: ssiagu
- **邮箱**: ssiagu@gmail.com
- **项目主页**: https://github.com/ssiagu/BettaFish

---

**最后更新**: 2025-12-08 15:52:05
**文档签名**: ssiagu