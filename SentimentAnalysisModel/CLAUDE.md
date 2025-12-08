# SentimentAnalysisModel (情感分析模型)

> [首页](../CLAUDE.md) > SentimentAnalysisModel

## 模块概述

SentimentAnalysisModel是BettaFish项目的情感分析核心模块，提供多种情感分析模型和方法。该模块包含多个子模块，涵盖从传统机器学习方法到深度学习模型的完整情感分析解决方案，特别针对中文社交媒体文本进行了优化。

### 主要功能
- 多模型支持：贝叶斯、SVM、XGBoost、LSTM、BERT等
- 多语言分析：支持22种语言的情感分析
- 微调优化：针对微博等社交媒体的特定微调模型
- 主题检测：结合情感分析和主题检测
- 批量处理：支持大规模文本批量分析

## 核心子模块

### 1. WeiboMultilingualSentiment (多语言情感分析)
基于多语言预训练模型，支持22种语言的情感分析。

**特性：**
- 支持5级情感分类（非常负面到非常正面）
- 基于Transformer架构
- 自动模型下载和本地缓存
- 实时情感分析

**主要文件：**
- `predict.py`: 预测主程序
- `model/`: 模型存储目录

### 2. WeiboSentiment_MachineLearning (机器学习方法)
集合多种传统机器学习方法的情感分析实现。

**支持模型：**
- **朴素贝叶斯 (Bayes)**: 基于概率的经典方法
- **支持向量机 (SVM)**: 基于最大间隔分类器
- **XGBoost**: 梯度提升树方法
- **LSTM**: 长短期记忆网络
- **BERT**: 基于预训练的深度学习模型

**主要文件：**
- `predict.py`: 统一预测接口
- `bayes_train.py`: 贝叶斯模型训练
- `svm_train.py`: SVM模型训练
- `lstm_train.py`: LSTM模型训练
- `bert_train.py`: BERT模型训练
- `base_model.py`: 模型基类

### 3. WeiboSentiment_Finetuned (微调模型)
针对微博等中文社交媒体的专门微调模型。

**子模块：**
- **BertChinese-Lora**: BERT中文模型+LoRA微调
- **GPT2-Lora**: GPT-2模型+LoRA微调
- **GPT2-AdapterTuning**: GPT-2模型+适配器调优

**特点：**
- 参数高效微调 (PEFT)
- 适配社交媒体语言风格
- 保留预训练知识的同时适应新任务

### 4. BertTopicDetection_Finetuned (BERT主题检测)
结合情感分析和主题检测的混合模型。

**功能：**
- 主题识别和分类
- 情感-主题关联分析
- 多标签主题检测

### 5. WeiboSentiment_SmallQwen (小型Qwen模型)
基于轻量化Qwen模型的情感分析实现。

**特点：**
- 模型体积小，推理速度快
- 保持良好分析精度
- 适合边缘部署

## 目录结构

```
SentimentAnalysisModel/
├── WeiboMultilingualSentiment/        # 多语言情感分析
│   ├── predict.py                    # 预测程序
│   └── model/                        # 模型目录
├── WeiboSentiment_MachineLearning/    # 机器学习方法
│   ├── predict.py                    # 统一预测接口
│   ├── base_model.py                 # 模型基类
│   ├── bayes_train.py                # 贝叶斯训练
│   ├── svm_train.py                  # SVM训练
│   ├── lstm_train.py                 # LSTM训练
│   ├── bert_train.py                 # BERT训练
│   ├── data/                         # 数据目录
│   │   └── weibo2018/               # 微博2018数据集
│   └── model/                        # 训练好的模型
├── WeiboSentiment_Finetuned/          # 微调模型
│   ├── BertChinese-Lora/            # BERT+LoRA
│   ├── GPT2-Lora/                   # GPT-2+LoRA
│   └── GPT2-AdapterTuning/          # GPT-2+适配器
├── BertTopicDetection_Finetuned/      # BERT主题检测
│   ├── train.py                     # 训练程序
│   ├── predict.py                   # 预测程序
│   └── dataset/                     # 数据集
└── WeiboSentiment_SmallQwen/          # 小型Qwen模型
    ├── dataset/                     # 数据集
    └── model/                       # 模型文件
```

## 主要类和接口

### SentimentPredictor
统一的情感分析预测器，支持加载和使用多种模型。

**主要方法：**
- `load_model(model_type: str, model_path: str)`: 加载指定模型
- `load_all_models(model_dir: str)`: 加载所有可用模型
- `predict_single(text: str, model_type: str)`: 单文本预测
- `predict_batch(texts: List[str], model_type: str)`: 批量预测
- `ensemble_predict(text: str)`: 集成预测（多模型投票）

### 基础模型类
所有模型都继承自 `BaseModel`，提供统一接口：
- `train(X_train, y_train)`: 训练模型
- `predict(text)`: 预测情感
- `predict_proba(text)`: 预测概率分布
- `save_model(path)`: 保存模型
- `load_model(path)`: 加载模型

## 依赖关系

### 深度学习框架
- torch: PyTorch深度学习框架
- transformers: Hugging Face Transformers库
- keras: Keras深度学习库（部分模型）

### 机器学习库
- scikit-learn: 传统机器学习算法
- xgboost: XGBoost实现
- numpy: 数值计算
- pandas: 数据处理

### 文本处理
- jieba: 中文分词
- re: 正则表达式
- nltk: 自然语言处理工具

## 使用示例

### 基础情感分析
```python
from WeiboMultilingualSentiment.predict import main

# 使用交互式预测
main()  # 将启动交互式命令行界面
```

### 使用机器学习模型
```python
from WeiboSentiment_MachineLearning.predict import SentimentPredictor

# 创建预测器
predictor = SentimentPredictor()

# 加载所有模型
predictor.load_all_models()

# 单文本预测
text = "今天天气真好，心情愉快！"
result = predictor.predict_single(text)
print(f"预测结果: {result}")

# 批量预测
texts = ["这家餐厅很棒", "服务态度差", "味道一般"]
results = predictor.predict_batch(texts)
```

### 使用特定模型
```python
from WeiboSentiment_MachineLearning.bayes_train import BayesModel

# 加载贝叶斯模型
model = BayesModel()
model.load_model('./model/bayes_model.pkl')

# 预测
text = "这个产品真的很不错"
prediction = model.predict(text)
confidence = model.predict_proba(text)
```

### 微调模型使用
```python
from WeiboSentiment_Finetuned.BertChinese_Lora.predict import predict

# 使用微调的BERT模型
text = "这家店的服务态度太好了"
result = predict(text)
print(f"情感: {result['label']}, 置信度: {result['confidence']}")
```

## 训练新模型

### 训练脚本使用
```bash
# 训练贝叶斯模型
python WeiboSentiment_MachineLearning/bayes_train.py

# 训练SVM模型
python WeiboSentiment_MachineLearning/svm_train.py

# 训练LSTM模型
python WeiboSentiment_MachineLearning/lstm_train.py

# 训练BERT模型
python WeiboSentiment_MachineLearning/bert_train.py
```

### 自定义数据训练
```python
from WeiboSentiment_MachineLearning.bert_train import BertModel_Custom

# 创建BERT模型
model = BertModel_Custom('bert-base-chinese')

# 准备数据
train_texts = ["文本1", "文本2", ...]
train_labels = [0, 1, ...]  # 0:负面, 1:正面

# 训练
model.train(train_texts, train_labels)

# 保存模型
model.save_model('./my_bert_model')
```

## 模型性能对比

| 模型 | 准确率 | 召回率 | F1分数 | 训练时间 | 推理速度 |
|------|--------|--------|--------|----------|----------|
| 贝叶斯 | 0.82 | 0.80 | 0.81 | 快 | 最快 |
| SVM | 0.85 | 0.83 | 0.84 | 中等 | 快 |
| XGBoost | 0.87 | 0.86 | 0.86 | 中等 | 中等 |
| LSTM | 0.89 | 0.88 | 0.88 | 慢 | 慢 |
| BERT | 0.92 | 0.91 | 0.91 | 最慢 | 中等 |
| 多语言BERT | 0.90 | 0.89 | 0.89 | 最慢 | 中等 |

## 测试说明

### 单元测试
```python
# 测试模型加载
def test_model_loading():
    predictor = SentimentPredictor()
    predictor.load_model('bayes', './model/bayes_model.pkl')
    assert 'bayes' in predictor.models

# 测试预测功能
def test_prediction():
    model = BayesModel()
    model.load_model('./model/bayes_model.pkl')
    result = model.predict("很高兴")
    assert result in [0, 1]  # 0:负面, 1:正面
```

### 性能测试
```bash
# 批量测试性能
python -m pytest tests/SentimentAnalysisModel/test_performance.py -v
```

## 模块特有配置项

### 环境变量配置
```bash
# 模型路径配置
MODEL_BASE_PATH=./models
DOWNLOAD_MODELS=true

# GPU配置
CUDA_VISIBLE_DEVICES=0
USE_GPU=true

# 推理配置
MAX_SEQUENCE_LENGTH=512
BATCH_SIZE=32
CONFIDENCE_THRESHOLD=0.5

# 多语言模型配置
MULTILINGUAL_MODEL=tabularisai/multilingual-sentiment-analysis
SUPPORTED_LANGUAGES=zh,en,es,ar,ja,ko
```

### 模型配置文件
各子模块都有独立的配置文件：
- `config_bert.json`: BERT模型配置
- `config_lstm.json`: LSTM模型配置
- `data_config.json`: 数据预处理配置

## 模型优化建议

### 提升准确率
1. **数据增强**: 使用回译、同义词替换等技术
2. **特征工程**: 结合词向量、句法分析等特征
3. **模型融合**: 多模型集成预测
4. **领域适应**: 针对特定领域进行微调

### 提升推理速度
1. **模型量化**: 使用INT8量化减少模型大小
2. **模型剪枝**: 移除不重要的模型参数
3. **蒸馏学习**: 使用大模型指导小模型
4. **缓存机制**: 缓存常见查询结果

### 部署优化
1. **批处理**: 批量处理提升吞吐量
2. **异步处理**: 使用异步I/O
3. **负载均衡**: 多实例部署
4. **边缘计算**: 部署到边缘设备

## 扩展开发

### 添加新模型
```python
from WeiboSentiment_MachineLearning.base_model import BaseModel

class CustomModel(BaseModel):
    def __init__(self):
        super().__init__()
        # 初始化自定义模型

    def train(self, X_train, y_train):
        # 实现训练逻辑
        pass

    def predict(self, text):
        # 实现预测逻辑
        pass
```

### 自定义预处理
```python
from WeiboSentiment_MachineLearning.utils import processing

def custom_preprocessing(text):
    # 自定义预处理逻辑
    text = processing(text)  # 使用基础预处理
    # 添加自定义处理步骤
    return text
```

---

**Document Signature**: ssiagu
**Last Updated**: 2025-12-08