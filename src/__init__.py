"""
KnowledgeBaseMCP - A Model Context Protocol server for document text extraction
"""

__version__ = "1.0.0"
__author__ = "KnowledgeBaseMCP Team"
__description__ = "MCP server for extracting text from DOCX, PDF, and PPTX files"

from .extractors import DocumentExtractor
# from .main import KnowledgeBaseMCP  # Commented out to avoid import issues

__all__ = ["DocumentExtractor"]
