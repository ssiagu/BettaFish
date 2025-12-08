# MindSpider (心智蜘蛛)

> [首页](../CLAUDE.md) > MindSpider

## 模块概述

MindSpider是BettaFish项目的数据采集核心，包含两个主要功能模块：BroadTopicExtraction（广度话题提取）和DeepSentimentCrawling（深度情感爬取）。该模块负责从各大社交媒体和新闻平台采集数据，进行话题提取和情感分析，为其他引擎提供原始数据支持。

### 主要功能
- 广度话题提取：从新闻源提取热门话题
- 深度情感爬取：多平台社交媒体数据采集
- 数据存储管理：统一的数据存储和管理
- 多平台支持：支持小红书、抖音、快手、B站、微博、贴吧、知乎等平台

## 核心类和接口

### 1. BroadTopicExtraction模块
#### NewsCollector
新闻收集器，负责从多个新闻源收集今日新闻。

**主要方法：**
- `collect_news() -> List[Dict]`: 收集新闻数据
- `get_news_by_source(source: str) -> List[Dict]`: 按来源获取新闻

#### TopicExtractor
话题提取器，使用NLP技术从新闻中提取热门话题。

**主要方法：**
- `extract_topics(news_list: List[Dict]) -> List[str]`: 提取话题
- `analyze_topic_trend(topic: str) -> Dict`: 分析话题趋势

#### DatabaseManager
数据库管理器，负责话题数据的存储和检索。

**主要方法：**
- `save_topics(topics: List[str])`: 保存话题
- `get_hot_topics(days: int = 7) -> List[str]`: 获取热门话题

### 2. DeepSentimentCrawling模块
#### MediaCrawler
媒体爬虫基类，定义了爬虫的通用接口和流程。

**主要方法：**
- `start()`: 启动爬虫
- `create_crawler(platform: str) -> AbstractCrawler`: 创建平台爬虫

#### 平台爬虫类
支持多个平台的专门爬虫：
- `XiaoHongShuCrawler`: 小红书爬虫
- `DouYinCrawler`: 抖音爬虫
- `KuaishouCrawler`: 快手爬虫
- `BilibiliCrawler`: B站爬虫
- `WeiboCrawler`: 微博爬虫
- `TieBaCrawler`: 贴吧爬虫
- `ZhihuCrawler`: 知乎爬虫

## 目录结构

```
MindSpider/
├── BroadTopicExtraction/          # 广度话题提取模块
│   ├── main.py                   # 主程序入口
│   ├── get_today_news.py         # 新闻收集器
│   ├── topic_extractor.py        # 话题提取器
│   └── database_manager.py       # 数据库管理器
├── DeepSentimentCrawling/         # 深度情感爬取模块
│   └── MediaCrawler/             # 媒体爬虫系统
│       ├── main.py              # 爬虫主程序
│       ├── base/                # 基础类和接口
│       ├── cache/               # 缓存系统
│       ├── cmd_arg/             # 命令行参数
│       ├── config/              # 配置管理
│       ├── constant/            # 常量定义
│       ├── database/            # 数据库操作
│       ├── libs/                # 工具库
│       ├── media_platform/      # 各平台爬虫实现
│       │   ├── bilibili/        # B站爬虫
│       │   ├── douyin/          # 抖音爬虫
│       │   ├── kuaishou/        # 快手爬虫
│       │   ├── tieba/           # 贴吧爬虫
│       │   ├── weibo/           # 微博爬虫
│       │   ├── xhs/             # 小红书爬虫
│       │   └── zhihu/           # 知乎爬虫
│       └── tools/               # 工具函数
```

## 主要文件功能介绍

### BroadTopicExtraction/main.py
- **功能**: 话题提取主程序
- **职责**: 整合新闻收集、话题提取和数据存储流程
- **特性**:
  - 命令行工具支持
  - 定时任务功能
  - 结果导出功能

### DeepSentimentCrawling/MediaCrawler/main.py
- **功能**: 媒体爬虫主程序
- **职责**: 爬虫工厂和主流程控制
- **特性**:
  - 多平台支持
  - 异步爬取
  - 可配置爬取策略

### media_platform/各平台爬虫
每个平台爬虫都包含：
- `client.py`: API客户端
- `core.py`: 核心爬取逻辑
- `help.py`: 辅助函数
- `field.py`: 字段映射
- `login.py`: 登录处理
- `exception.py`: 异常定义

## 依赖关系

### 外部依赖
- asyncio: 异步编程支持
- requests: HTTP请求
- beautifulsoup4: HTML解析
- selenium: 浏览器自动化（部分平台）
- playwright: 现代浏览器自动化
- sqlalchemy: ORM数据库操作
- redis: 缓存系统
- pandas: 数据处理

### 系统依赖
- Chrome/Chromium: 浏览器驱动
- Redis Server: 缓存服务
- MySQL/PostgreSQL: 数据存储

## 使用示例

### 广度话题提取使用
```python
from BroadTopicExtraction import BroadTopicExtraction

# 创建话题提取实例
with BroadTopicExtraction() as extractor:
    # 收集今日新闻
    news = extractor.news_collector.collect_news()

    # 提取热门话题
    topics = extractor.topic_extractor.extract_topics(news)

    # 保存到数据库
    extractor.db_manager.save_topics(topics)

    # 获取近7天热门话题
    hot_topics = extractor.db_manager.get_hot_topics(days=7)
    print(f"热门话题: {hot_topics}")
```

### 深度情感爬取使用
```python
from DeepSentimentCrawling.MediaCrawler.main import CrawlerFactory

# 创建平台爬虫
crawler = CrawlerFactory.create_crawler("xhs")  # 小红书爬虫

# 配置爬取参数
config = {
    "keyword": "人工智能",
    "max_count": 100,
    "save_path": "./data/xhs_ai"
}

# 启动爬取
asyncio.run(crawler.start())
```

### 命令行使用
```bash
# 话题提取
python MindSpider/BroadTopicExtraction/main.py --mode collect --days 7

# 媒体爬取
python MindSpider/DeepSentimentCrawling/MediaCrawler/main.py --platform xhs --keyword "AI"

# 多平台爬取
python MindSpider/DeepSentimentCrawling/MediaCrawler/main.py --platform all --keywords "科技,创新"
```

## 测试说明

### 单元测试
每个模块都应包含相应的测试文件：
- `test_news_collector.py`: 新闻收集测试
- `test_topic_extractor.py`: 话题提取测试
- `test_crawlers.py`: 爬虫功能测试

### 集成测试
- `test_end_to_end.py`: 端到端流程测试
- `test_data_pipeline.py`: 数据管道测试

### 测试运行
```bash
# 运行所有测试
python -m pytest tests/MindSpider/ -v

# 运行特定模块测试
python -m pytest tests/MindSpider/test_crawlers.py -v
```

## 模块特有配置项

### 环境变量配置
在 `.env` 文件中配置：

```bash
# 数据库配置
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=mindspider

# Redis配置
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

# 爬虫配置
CRAWLER_DELAY=1  # 爬取间隔（秒）
CRAWLER_TIMEOUT=30  # 请求超时（秒）
CRAWLER_RETRY=3  # 重试次数

# 话题提取配置
TOPIC_N_KEYWORDS=10  # 提取关键词数量
TOPIC_MIN_FREQUENCY=5  # 最小词频
```

### 平台特定配置
各平台需要单独的配置文件：
- `xhs_config.py`: 小红书配置
- `dy_config.py`: 抖音配置
- `bili_config.py`: B站配置
- 等...

## 数据流程

### 话题提取流程
1. **新闻收集** → 从多个新闻源获取今日新闻
2. **内容预处理** → 清洗和标准化新闻内容
3. **话题提取** → 使用NLP算法提取关键词和话题
4. **趋势分析** → 分析话题热度和发展趋势
5. **数据存储** → 将结果保存到数据库

### 情感爬取流程
1. **平台登录** → 处理各平台的登录机制
2. **搜索定位** → 根据关键词搜索相关内容
3. **内容抓取** → 提取文本、图片、评论等信息
4. **情感分析** → 对内容进行情感倾向分析
5. **数据存储** → 结构化存储到数据库

## 爬虫策略

### 反爬虫应对
- IP代理池轮换
- 请求头随机化
- 请求频率控制
- 行为模拟（滚动、点击等）
- 验证码识别（集成OCR）

### 数据质量控制
- 内容去重机制
- 数据完整性验证
- 异常内容过滤
- 数据格式标准化

## 性能优化建议

1. **并发优化**:
   - 使用异步IO提升并发能力
   - 合理设置并发数量
   - 实现请求队列管理

2. **缓存策略**:
   - Redis缓存热点数据
   - 实现分布式爬取
   - 避免重复爬取

3. **存储优化**:
   - 批量写入数据库
   - 使用连接池
   - 定期数据清理

4. **监控告警**:
   - 实时监控爬取状态
   - 异常自动告警
   - 性能指标收集

## 注意事项

### 合规性提醒
- 遵守各平台的使用条款
- 控制爬取频率，避免对平台造成负担
- 不得用于商业用途
- 尊重用户隐私和数据保护法规

### 技术风险
- 平台API变更风险
- 反爬虫机制升级风险
- 法律合规风险
- 数据质量风险

---

**Document Signature**: ssiagu
**Last Updated**: 2025-12-08