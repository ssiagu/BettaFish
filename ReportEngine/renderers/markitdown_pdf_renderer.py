"""
使用 Microsoft MarkItDown 的 PDF 渲染器

此模块提供了一个无需 GTK 依赖的 PDF 导出解决方案，
使用 MarkItDown 库将 Markdown 转换为 HTML，然后通过浏览器打印为 PDF。
"""

import os
import tempfile
import subprocess
import webbrowser
import time
from pathlib import Path
from typing import Optional, Dict, Any
from loguru import logger
import asyncio

try:
    from markitdown import MarkItDown
    MARKITDOWN_AVAILABLE = True
except ImportError:
    logger.warning("MarkItDown 库未安装，请运行: pip install markitdown")
    MARKITDOWN_AVAILABLE = False


class MarkItDownPDFRenderer:
    """
    基于 MarkItDown 的 PDF 渲染器

    无需 GTK 依赖，通过以下步骤生成 PDF：
    1. 使用 MarkItDown 将内容转换为 HTML
    2. 创建包含打印样式的临时 HTML 文件
    3. 使用无头浏览器或系统打印功能生成 PDF
    """

    def __init__(self):
        """初始化渲染器"""
        self.md = MarkItDown() if MARKITDOWN_AVAILABLE else None
        self.temp_dir = Path(tempfile.gettempdir()) / "bettafish_pdf"
        self.temp_dir.mkdir(exist_ok=True)

    def render_to_pdf(
        self,
        content: str,
        output_path: Optional[str] = None,
        title: str = "BettaFish 报告",
        css_style: Optional[str] = None
    ) -> str:
        """
        将内容渲染为 PDF

        Args:
            content: 要渲染的内容（支持 Markdown）
            output_path: 输出 PDF 路径（可选）
            title: PDF 文档标题
            css_style: 自定义 CSS 样式

        Returns:
            str: 生成的 PDF 文件路径
        """
        if not MARKITDOWN_AVAILABLE:
            raise ImportError("MarkItDown 库未安装，请运行: pip install markitdown")

        if not self.md:
            raise RuntimeError("MarkItDown 初始化失败")

        try:
            # 生成输出路径
            if not output_path:
                output_path = str(self.temp_dir / f"{title}_{int(time.time())}.pdf")

            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # 转换 Markdown 为 HTML
            if isinstance(content, str):
                # 将内容写入临时文件
                temp_md = self.temp_dir / f"temp_markdown_{int(time.time())}.md"
                markdown_content = f"# {title}\n\n{content}"

                with open(temp_md, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)

                # 使用 MarkItDown 转换
                result = self.md.convert(str(temp_md))
                html_content = result.text_content

                # 清理临时文件
                temp_md.unlink(missing_ok=True)
            else:
                html_content = str(content)

            # 创建带有打印样式的 HTML
            html_with_style = self._wrap_with_print_styles(html_content, title, css_style)

            # 保存为临时 HTML 文件
            temp_html = self.temp_dir / f"temp_{int(time.time())}.html"
            with open(temp_html, 'w', encoding='utf-8') as f:
                f.write(html_with_style)

            # 转换为 PDF
            pdf_path = self._html_to_pdf(temp_html, output_path)

            # 清理临时文件
            temp_html.unlink(missing_ok=True)

            logger.info(f"PDF 已生成: {pdf_path}")
            return str(pdf_path)

        except Exception as e:
            logger.error(f"PDF 生成失败: {str(e)}")
            raise

    def _wrap_with_print_styles(
        self,
        html_content: str,
        title: str,
        custom_css: Optional[str] = None
    ) -> str:
        """
        为 HTML 添加打印样式

        Args:
            html_content: 原始 HTML 内容
            title: 文档标题
            custom_css: 自定义 CSS

        Returns:
            str: 包含打印样式的完整 HTML
        """
        default_css = """
            @page {
                size: A4;
                margin: 2cm;
            }

            body {
                font-family: 'Microsoft YaHei', 'SimHei', Arial, sans-serif;
                font-size: 12pt;
                line-height: 1.6;
                color: #333;
                margin: 0;
                padding: 0;
            }

            h1, h2, h3, h4, h5, h6 {
                color: #2c3e50;
                margin-top: 1.5em;
                margin-bottom: 0.8em;
                page-break-after: avoid;
            }

            h1 {
                font-size: 24pt;
                text-align: center;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
            }

            h2 {
                font-size: 18pt;
                border-bottom: 1px solid #ecf0f1;
                padding-bottom: 5px;
            }

            p {
                margin: 1em 0;
                text-align: justify;
            }

            code {
                font-family: 'Consolas', 'Monaco', monospace;
                background-color: #f8f9fa;
                padding: 2px 4px;
                border-radius: 3px;
                font-size: 0.9em;
            }

            pre {
                background-color: #f8f9fa;
                padding: 1em;
                border-radius: 5px;
                overflow-x: auto;
                page-break-inside: avoid;
            }

            blockquote {
                border-left: 4px solid #3498db;
                padding-left: 1em;
                margin: 1em 0;
                color: #7f8c8d;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                margin: 1em 0;
            }

            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }

            th {
                background-color: #f2f2f2;
                font-weight: bold;
            }

            ul, ol {
                margin: 1em 0;
                padding-left: 2em;
            }

            a {
                color: #3498db;
                text-decoration: none;
            }

            .header, .footer {
                display: none;
            }

            @media print {
                body {
                    -webkit-print-color-adjust: exact;
                }

                a {
                    color: #000;
                    text-decoration: underline;
                }

                .no-print {
                    display: none !important;
                }
            }
        """

        # 合并自定义样式
        final_css = default_css
        if custom_css:
            final_css += "\n" + custom_css

        # 构建完整 HTML
        full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{final_css}
    </style>
</head>
<body>
    {html_content}
</body>
</html>"""

        return full_html

    def _html_to_pdf(self, html_path: Path, output_path: Path) -> Path:
        """
        将 HTML 文件转换为 PDF

        使用多种方法尝试转换：
        1. 使用 wkhtmltopdf（如果可用）
        2. 使用 Playwright（如果已安装）
        3. 使用 Chrome/Edge 无头模式
        4. 最后回退到使用浏览器打印对话框
        """
        # 尝试使用 Playwright
        try:
            return self._convert_with_playwright(html_path, output_path)
        except Exception as e:
            logger.debug(f"Playwright 转换失败: {e}")

        # 尝试使用 Chrome 无头模式
        try:
            return self._convert_with_chrome(html_path, output_path)
        except Exception as e:
            logger.debug(f"Chrome 转换失败: {e}")

        # 回退到浏览器打印方法
        return self._convert_with_browser_print(html_path, output_path)

    def _convert_with_playwright(self, html_path: Path, output_path: Path) -> Path:
        """使用 Playwright 转换 HTML 为 PDF"""
        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(f"file://{html_path.absolute()}")
                page.pdf(
                    path=str(output_path),
                    format="A4",
                    print_background=True,
                    margin={
                        "top": "2cm",
                        "bottom": "2cm",
                        "left": "2cm",
                        "right": "2cm"
                    }
                )
                browser.close()

            return output_path

        except ImportError:
            raise Exception("Playwright 未安装")
        except Exception as e:
            raise Exception(f"Playwright 转换失败: {str(e)}")

    def _convert_with_chrome(self, html_path: Path, output_path: Path) -> Path:
        """使用 Chrome 无头模式转换 HTML 为 PDF"""
        import platform

        # Chrome 命令行参数
        chrome_args = [
            "--headless",
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--disable-software-rasterizer",
            "--run-all-tests",
            "--print-to-pdf=" + str(output_path),
            f"--file://{html_path.absolute()}"
        ]

        # 不同系统的 Chrome 路径
        if platform.system() == "Windows":
            chrome_paths = [
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
                "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
            ]
        elif platform.system() == "Darwin":  # macOS
            chrome_paths = [
                "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            ]
        else:  # Linux
            chrome_paths = [
                "/usr/bin/google-chrome",
                "/usr/bin/chromium-browser",
                "/usr/bin/microsoft-edge",
            ]

        # 尝试找到并使用 Chrome
        for chrome_path in chrome_paths:
            if os.path.exists(chrome_path):
                try:
                    subprocess.run([chrome_path] + chrome_args, check=True, timeout=30)
                    return output_path
                except subprocess.CalledProcessError as e:
                    logger.debug(f"Chrome 执行失败: {e}")
                    continue

        raise Exception("未找到 Chrome 或 Edge 浏览器")

    def _convert_with_browser_print(self, html_path: Path, output_path: Path) -> Path:
        """
        使用浏览器打印功能（最后的选择）

        注意：这个方法会打开浏览器，需要用户手动保存 PDF
        """
        logger.warning("即将打开浏览器，请使用 Ctrl+P 打印并保存为 PDF")

        # 打开浏览器
        webbrowser.open(f"file://{html_path.absolute()}")

        # 提示用户
        input("请在浏览器中按 Ctrl+P，选择'保存为 PDF'，保存后按回车继续...")

        # 返回预期的输出路径（用户应该已经保存）
        return output_path

    def test_renderer(self) -> bool:
        """
        测试渲染器是否正常工作

        Returns:
            bool: 是否可以正常生成 PDF
        """
        if not MARKITDOWN_AVAILABLE:
            logger.error("MarkItDown 库未安装")
            return False

        try:
            test_content = """
# 测试文档

这是一个测试 PDF 导出功能的示例文档。

## 功能特点

1. 无需 GTK 依赖
2. 使用 MarkItDown 库
3. 支持 Markdown 格式
4. 自动优化打印样式

## 代码示例

```python
print("Hello, BettaFish!")
```

## 表格示例

| 功能 | 状态 |
|------|------|
| PDF 导出 | ✅ 正常 |
| 免费搜索 | ✅ 正常 |
| AI 总结 | ✅ 正常 |

> 这是一个引用示例。
            """

            test_pdf = self.temp_dir / "test_output.pdf"
            self.render_to_pdf(test_content, str(test_pdf), "测试文档")

            if test_pdf.exists():
                logger.success("PDF 渲染器测试成功！")
                logger.info(f"测试文件已生成: {test_pdf}")
                return True
            else:
                logger.error("PDF 文件未生成")
                return False

        except Exception as e:
            logger.error(f"测试失败: {str(e)}")
            return False


# 创建全局实例
pdf_renderer = MarkItDownPDFRenderer()


def render_pdf(
    content: str,
    output_path: Optional[str] = None,
    title: str = "BettaFish 报告"
) -> str:
    """
    便捷函数：将内容渲染为 PDF

    Args:
        content: 要渲染的内容
        output_path: 输出路径（可选）
        title: 文档标题

    Returns:
        str: 生成的 PDF 文件路径
    """
    return pdf_renderer.render_to_pdf(content, output_path, title)


# 模块初始化时进行测试
if __name__ == "__main__":
    logger.info("测试 MarkItDown PDF 渲染器...")
    if pdf_renderer.test_renderer():
        logger.success("PDF 渲染器已就绪！")
    else:
        logger.error("PDF 渲染器初始化失败")