# BettaFish 使用指南

## 概述

BettaFish 是一个基于多智能体架构的微博舆情分析系统，提供洞察发现、媒体分析、信息查询和报告生成等核心功能。本指南将帮助您了解并使用系统的主要功能。

---

## 🆓 免费搜索功能

### 功能概述

BettaFish 已成功集成了免费搜索功能，使用 DuckDuckGo 作为搜索源，并支持 AI 智能总结。

### 主要特性
- ✅ **完全免费**：使用 DuckDuckGo 搜索，无 API 限制
- ✅ **AI 智能总结**：集成系统 LLM 生成智能总结
- ✅ **接口兼容**：保持与 AnspireAISearch 相同的接口
- ✅ **自动切换**：当没有搜索 API key 时自动启用
- ✅ **已修复**：解决了 Streamlit 应用阻止免费搜索的问题

### ✅ 已解决的问题

#### 问题：Media Agent 报错 "请在您的环境变量中设置BOCHA_WEB_SEARCH_API_KEY或ANSPIRE_API_KEY"

**原因**：Streamlit 应用在创建 Agent 前强制检查搜索 API 密钥，阻止了免费搜索模式的执行。

**解决方案**：
1. 修改了 `SingleEngineApp/media_engine_streamlit_app.py`
2. 移除了强制要求搜索 API 密钥的错误检查
3. 添加了免费搜索模式的支持
4. 当没有搜索 API 密钥时，自动切换到 DuckDuckGo 免费搜索

**修改后的行为**：
- 有 Bocha API 密钥 → 使用 Bocha 搜索
- 有 Anspire API 密钥 → 使用 Anspire 搜索
- 都没有 → **自动使用免费搜索模式**，显示警告信息

### 使用方法

系统会自动检测搜索 API 密钥：
- **有 API 密钥**：使用对应的付费搜索
- **无 API 密钥**：自动切换到免费搜索模式（DuckDuckGo + AI总结）

### AI 总结配置

免费搜索使用以下 LLM 配置（优先级顺序）：
1. `MEDIA_ENGINE_API_KEY` - MediaEngine 的 LLM
2. `MINDSPIDER_API_KEY` - MindSpider 的 LLM

当前配置示例：
```env
# 优先配置（您已经配置好了）
MEDIA_ENGINE_API_KEY=b944b906bac346cba84441d45355f88e.JHUZZkzlomZRd8rC
MEDIA_ENGINE_BASE_URL=https://open.bigmodel.cn/api/paas/v4/
MEDIA_ENGINE_MODEL_NAME=glm-4.5v
```

### 测试结果

```python
# 测试查询示例
queries = [
    "人工智能最新发展",
    "今天北京天气",
    "Python编程技巧"
]

# 成功返回：
- 每个查询找到 5 个搜索结果
- AI 总结生成成功（使用 glm-4.5v 模型）
- 响应时间：20-30秒（包含AI处理）
```

### 环境变量配置

在 `.env` 文件中：
```env
# 搜索工具配置（可选，不配置会自动使用免费模式）
SEARCH_TOOL_TYPE=AnspireAPI  # 保持这个值，系统会自动切换

# 搜索 API 密钥（可选，二选一或都不配置）
# BOCHA_WEB_SEARCH_API_KEY=your_bocha_key
# ANSPIRE_API_KEY=your_anspire_key

# 确保 LLM 配置存在（用于AI总结，必须配置）
MEDIA_ENGINE_API_KEY=b944b906bac346cba84441d45355f88e.JHUZZkzlomZRd8rC
MEDIA_ENGINE_BASE_URL=https://open.bigmodel.cn/api/paas/v4/
MEDIA_ENGINE_MODEL_NAME=glm-4.5v
```

---

## 📄 PDF 导出功能

### 功能概述

BettaFish 现在支持基于 Microsoft MarkItDown 库的 PDF 导出功能，这是一个轻量级、无需系统依赖的解决方案。

### 主要特点

#### ✅ 无需系统依赖
- 不需要安装 GTK3 Runtime
- 不需要配置复杂的系统路径
- 开箱即用

#### ✅ 简单易用
- 只需安装一个 Python 库：`pip install markitdown`
- 自动回退机制：优先使用 WeasyPrint，回退到 MarkItDown
- 保持原有接口不变

#### ✅ 功能完整
- 支持 Markdown 格式
- 自动优化打印样式
- 支持中文内容
- 支持表格、代码块等元素

### 安装方法

#### 方法一：使用 MarkItDown（推荐，简单快捷）
```bash
pip install markitdown
```

#### 方法二：使用 WeasyPrint（功能更强，需要系统依赖）
1. 安装 WeasyPrint：
   ```bash
   pip install weasyprint
   ```
2. 安装 GTK3 Runtime（Windows）
   - 下载地址：https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
   - 运行安装程序
   - 配置环境变量

### 使用方法

#### 通过 ReportEngine 使用

```python
from ReportEngine import ReportAgent

# 创建报告代理
agent = ReportAgent()

# 生成报告（会自动选择可用的 PDF 渲染器）
report_path = agent.generate_report({
    "topic": "测试主题",
    "content": "报告内容..."
})
```

#### 直接使用 PDF 渲染器

```python
from ReportEngine.renderers import PDFRenderer

# 创建渲染器（自动选择最优方案）
renderer = PDFRenderer()

# 渲染 PDF
pdf_path = renderer.render(content="你的内容", title="报告标题")
```

### 智能选择机制

系统会按以下优先级自动选择 PDF 渲染器：

1. **WeasyPrint**（如果可用）
   - 功能最完整
   - CSS 支持最好
   - 需要系统依赖

2. **MarkItDown**（回退方案）
   - 无系统依赖
   - 轻量级
   - 适合受限环境

3. **占位符**（都不可用时）
   - 提供友好的错误提示
   - 指导安装依赖

### 测试

运行测试脚本验证功能：

```bash
python test_markitdown_pdf.py
```

---

## 🚀 快速开始

### 环境要求
- Python 3.11+
- PostgreSQL/MySQL
- Redis（可选）

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

5. **安装 PDF 导出依赖（可选）**
```bash
# 方法一：使用 MarkItDown（推荐）
pip install markitdown

# 方法二：使用 WeasyPrint（功能更强）
pip install weasyprint
# 然后安装 GTK3 Runtime
```

6. **运行应用**
```bash
python app.py
```

访问 http://localhost:5000 开始使用 BettaFish！

---

## 📊 系统架构

### 核心引擎

1. **InsightEngine（洞察引擎）**
   - 深度搜索与智能洞察
   - 主题提取与趋势分析

2. **MediaEngine（媒体引擎）**
   - 多媒体内容处理与分析
   - 图像、视频内容理解

3. **QueryEngine（查询引擎）**
   - 基于免费搜索的信息检索
   - 实时新闻搜索

4. **ReportEngine（报告引擎）**
   - 智能报告生成与导出
   - 支持 PDF 和 HTML 格式

5. **ForumEngine（论坛引擎）**
   - 论坛监控与讨论分析
   - LLM 托管服务

### 数据流

```
用户输入 → 各引擎处理 → 结果整合 → 报告生成 → 导出PDF/HTML
    ↓
免费搜索 (DuckDuckGo) → AI总结 → 内容分析
```

---

## 💡 使用技巧

### 搜索功能
- 支持自然语言查询
- 自动进行时效性筛选
- AI 总结提供核心信息提炼

### 报告生成
- 支持多种模板选择
- 自动优化布局结构
- 一键导出 PDF

### 性能优化
- 使用缓存减少重复计算
- 并行处理提升效率
- 智能资源管理

---

## ❓ 常见问题

### Q: 免费搜索的质量如何？
A: 使用 DuckDuckGo 搜索源，配合 AI 总结，可以提供高质量的搜索结果。

### Q: PDF 导出需要安装什么？
A: 只需要安装 `markitdown` 库即可，无需系统依赖。

### Q: 如何配置自己的 LLM？
A: 在 `.env` 文件中配置相应的 API_KEY、BASE_URL 和 MODEL_NAME。

### Q: 系统支持哪些语言？
A: 主要支持中文，同时支持英文等多语言内容分析。

---

## 🔧 故障排除

### Media Engine 相关问题

#### 问题：报错 "请在您的环境变量中设置BOCHA_WEB_SEARCH_API_KEY或ANSPIRE_API_KEY"

**状态**：✅ 已解决

**解决方案**：
1. 确保已应用最新代码修改
2. 重启 Media Engine Streamlit 应用
3. 系统会显示警告信息并自动使用免费搜索模式

**验证方法**：
- 查看 Media Engine 界面是否显示警告："未配置搜索API密钥，将使用免费搜索模式"
- 输入查询测试是否正常工作

#### 问题：免费搜索不工作

**排查步骤**：
1. 检查是否安装了必要的依赖：
   ```bash
   pip install duckduckgo-search
   ```
2. 确认 LLM 配置正确（用于 AI 总结）：
   ```env
   MEDIA_ENGINE_API_KEY=your_api_key
   MEDIA_ENGINE_BASE_URL=your_base_url
   MEDIA_ENGINE_MODEL_NAME=your_model_name
   ```
3. 查看日志文件 `logs/media_engine.log` 了解详细错误信息

### 通用问题

#### 问题：应用启动失败

**排查步骤**：
1. 检查 Python 版本（需要 3.11+）
2. 检查依赖是否完整安装：
   ```bash
   pip install -r requirements.txt
   ```
3. 检查 `.env` 文件配置是否正确
4. 查看控制台输出的错误信息

#### 问题：数据库连接失败

**排查步骤**：
1. 确认数据库服务正在运行
2. 检查 `.env` 文件中的数据库配置：
   ```env
   DB_HOST=127.0.0.1
   DB_PORT=5432
   DB_USER=bettafish
   DB_PASSWORD=bettafish123
   DB_NAME=bettafish
   ```
3. 确认数据库用户有足够的权限

#### 问题：LLM API 调用失败

**排查步骤**：
1. 验证 API 密钥是否有效
2. 检查 BASE_URL 是否正确
3. 确认模型名称是否可用
4. 检查网络连接是否正常

### 日志文件位置

- 主应用日志：`logs/app.log`
- Media Engine 日志：`logs/media_engine.log`
- Insight Engine 日志：`logs/insight_engine.log`
- Query Engine 日志：`logs/query_engine.log`
- Forum 日志：`logs/forum.log`

### 获取帮助

如果遇到其他问题，请：
1. 查看相关的日志文件
2. 检查 GitHub Issues 页面
3. 提交新的 Issue 并包含：
   - 错误信息
   - 相关日志
   - 系统环境信息
   - 重现步骤

---

## 📝 更新日志

### 2025-12-08
- ✅ 集成免费搜索功能（DuckDuckGo + AI总结）
- ✅ 新增 MarkItDown PDF 渲染器
- ✅ 实现智能回退机制
- ✅ 无系统依赖的解决方案
- ✅ **修复**：Media Engine 免费搜索模式问题
  - 移除了强制要求搜索 API 密钥的检查
  - 添加了自动切换到免费搜索的支持
  - 优化了用户体验，显示友好的警告信息
- ✅ 新增故障排除章节
  - 添加了常见问题的解决方案
  - 提供了详细的日志文件位置说明
  - 完善了问题排查流程

---

## 📞 技术支持

- **作者**: ssiagu
- **邮箱**: ssiagu@gmail.com
- **项目主页**: https://github.com/ssiagu/BettaFish
- **文档**: 本文档包含完整使用说明

---

**文档签名**: ssiagu
**最后更新**: 2025-12-08