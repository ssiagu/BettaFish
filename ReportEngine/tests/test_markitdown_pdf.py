"""
测试 MarkItDown PDF 渲染器
"""

import os
import sys

# 添加项目根路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

from ReportEngine.renderers.markitdown_pdf_renderer import MarkItDownPDFRenderer, render_pdf
from loguru import logger

def test_basic_pdf():
    """测试基本 PDF 生成功能"""
    print("=" * 60)
    print("测试 MarkItDown PDF 渲染器")
    print("=" * 60)

    renderer = MarkItDownPDFRenderer()

    # 测试内容
    test_content = """
# BettaFish 系统测试报告

## 系统概述

BettaFish 是一个基于多智能体架构的微博舆情分析系统，提供以下核心功能：

1. **免费搜索功能** - 使用 DuckDuckGo，无需付费 API
2. **AI 智能总结** - 集成 LLM 生成智能摘要
3. **PDF 导出功能** - 基于 MarkItDown，无需系统依赖

## 技术架构

### 搜索引擎
- DuckDuckGo 搜索
- 自动回退机制
- AI 总结集成

### PDF 生成
- MarkItDown 库
- 无 GTK 依赖
- 支持 Markdown

## 测试结果

| 功能 | 状态 | 说明 |
|------|------|------|
| 免费搜索 | ✅ 正常 | 已实现并测试 |
| AI 总结 | ✅ 正常 | 使用 glm-4.5v 模型 |
| PDF 导出 | ✅ 测试中 | MarkItDown 方案 |

> 这是一个无需安装系统依赖的解决方案，非常适合在受限环境中使用。
    """

    try:
        # 生成 PDF
        output_path = renderer.render_to_pdf(
            content=test_content,
            title="BettaFish 测试报告",
            output_path="./test_markitdown_output.pdf"
        )

        print(f"\n✅ PDF 生成成功！")
        print(f"文件路径: {output_path}")

        # 检查文件是否存在
        import os
        if os.path.exists(output_path):
            file_size = os.path.getsize(output_path)
            print(f"文件大小: {file_size} 字节")
            return True
        else:
            print("❌ 文件未生成")
            return False

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_simple_markdown():
    """测试简单 Markdown 转换"""
    print("\n" + "=" * 60)
    print("测试简单 Markdown 转换")
    print("=" * 60)

    try:
        from markitdown import MarkItDown
        md = MarkItDown()

        simple_md = "# Hello\n\nThis is a **test**."
        result = md.convert(simple_md)

        print("转换结果:")
        print(result.text_content[:200] + "...")

        return True
    except Exception as e:
        print(f"转换失败: {e}")
        return False

if __name__ == "__main__":
    # 测试 MarkItDown 基本功能
    print("\n1. 测试 MarkItDown 基本功能...")
    if test_simple_markdown():
        print("✅ MarkItDown 基本功能正常")
    else:
        print("❌ MarkItDown 基本功能异常")

    # 测试 PDF 生成
    print("\n2. 测试 PDF 生成功能...")
    if test_basic_pdf():
        print("\n✅ 所有测试通过！")
    else:
        print("\n❌ PDF 生成测试失败")