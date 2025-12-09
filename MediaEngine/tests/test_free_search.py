"""
测试免费搜索功能
"""

import os
import sys

# 添加项目根路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

# 临时清除环境变量以测试免费搜索
os.environ.pop('ANSPIRE_API_KEY', None)

from MediaEngine.tools.search import AnspireAISearch
from loguru import logger

def test_free_search():
    """测试免费搜索功能"""
    print("=" * 60)
    print("测试免费搜索功能 (DuckDuckGo + AI总结)")
    print("=" * 60)

    try:
        # 创建搜索客户端（应该自动切换到免费模式）
        print("\n1. 初始化搜索客户端...")
        search_client = AnspireAISearch()

        # 测试查询
        test_queries = [
            "人工智能最新发展",
            "今天北京天气",
            "Python编程技巧"
        ]

        for i, query in enumerate(test_queries, 1):
            print(f"\n{i}. 测试查询: {query}")

            # 执行综合搜索
            print("   执行综合搜索...")
            response = search_client.comprehensive_search(query, max_results=5)

            # 显示结果
            print(f"   找到 {len(response.webpages)} 个结果")
            if response.webpages:
                print("   前3个结果:")
                for j, result in enumerate(response.webpages[:3], 1):
                    print(f"     {j}. {result.name[:50]}...")
                    print(f"        {result.url}")

            # 检查AI总结
            if hasattr(response, '_ai_answer'):
                print(f"   AI总结: {response._ai_answer[:100]}...")
            else:
                print("   无AI总结（可能是LLM未配置）")

        print("\n✅ 免费搜索测试完成！")

    except Exception as e:
        logger.error(f"测试失败: {e}")
        print(f"\n❌ 测试失败: {e}")
        return False

    return True

if __name__ == "__main__":
    test_free_search()