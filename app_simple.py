"""
简化版Flask测试应用
"""

from flask import Flask, render_template, jsonify
import os

# 设置环境变量
os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['PYTHONUTF8'] = '1'
os.environ['PYTHONUNBUFFERED'] = '1'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test-secret-key'

@app.route('/')
def index():
    return jsonify({
        'message': 'BettaFish 微博舆情分析系统',
        'status': 'running',
        'engines': [
            'InsightEngine - 洞察引擎',
            'MediaEngine - 媒体引擎',
            'QueryEngine - 查询引擎',
            'ReportEngine - 报告引擎',
            'ForumEngine - 论坛引擎',
            'MindSpider - 心智蜘蛛',
            'SentimentAnalysisModel - 情感分析模型'
        ]
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    print("=" * 50)
    print("🐟 BettaFish 微博舆情分析系统启动中...")
    print("📍 访问地址: http://localhost:5000")
    print("🔍 健康检查: http://localhost:5000/health")
    print("=" * 50)

    app.run(host='0.0.0.0', port=5000, debug=True)