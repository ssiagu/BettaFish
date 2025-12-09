"""
Report Engine渲染器集合。

提供 HTMLRenderer 和 PDFRenderer，支持HTML和PDF输出。
"""

from loguru import logger
from .html_renderer import HTMLRenderer

# 尝试导入 WeasyPrint PDF 渲染器
try:
    from .pdf_renderer import PDFRenderer as WeasyPrintPDFRenderer
    WEASYPRINT_AVAILABLE = True
    logger.info("使用 WeasyPrint PDF 渲染器")
except Exception as e:
    WEASYPRINT_AVAILABLE = False
    logger.debug(f"WeasyPrint 不可用: {e}")

# 尝试导入 MarkItDown PDF 渲染器
try:
    from .markitdown_pdf_renderer import MarkItDownPDFRenderer
    MARKITDOWN_AVAILABLE = True
    logger.info("MarkItDown PDF 渲染器可用")
except Exception as e:
    MARKITDOWN_AVAILABLE = False
    logger.debug(f"MarkItDown 不可用: {e}")

# 智能选择 PDF 渲染器
if WEASYPRINT_AVAILABLE:
    # 优先使用 WeasyPrint（功能更完整）
    PDFRenderer = WeasyPrintPDFRenderer
elif MARKITDOWN_AVAILABLE:
    # 回退到 MarkItDown（无需系统依赖）
    PDFRenderer = MarkItDownPDFRenderer
    logger.info("使用 MarkItDown PDF 渲染器（无系统依赖）")
else:
    # 创建一个空的 PDF 渲染器类
    class PDFRenderer:
        """PDF 渲染器未可用时的占位符"""
        def __init__(self):
            logger.error("PDF 渲染器不可用")

        def render(self, *args, **kwargs):
            raise ImportError(
                "PDF 渲染器不可用。请安装以下依赖之一：\n"
                "1. WeasyPrint + GTK 运行时（推荐）\n"
                "   pip install weasyprint\n"
                "   并安装 GTK3 Runtime\n"
                "2. MarkItDown（轻量级）\n"
                "   pip install markitdown"
            )

    logger.warning("没有可用的 PDF 渲染器")
from .pdf_layout_optimizer import (
    PDFLayoutOptimizer,
    PDFLayoutConfig,
    PageLayout,
    KPICardLayout,
    CalloutLayout,
    TableLayout,
    ChartLayout,
    GridLayout,
)

__all__ = [
    "HTMLRenderer",
    "PDFRenderer",
    "PDFLayoutOptimizer",
    "PDFLayoutConfig",
    "PageLayout",
    "KPICardLayout",
    "CalloutLayout",
    "TableLayout",
    "ChartLayout",
    "GridLayout",
]
