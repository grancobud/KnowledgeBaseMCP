#!/usr/bin/env python3
"""
KnowledgeBaseMCP - Sadeleştirilmiş versiyon
"""

import asyncio
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

# MCP imports
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp import types

# Local imports
from .extractors import DocumentExtractor
from .docx_writer import DocxWriter
from .xlsx_writer import XlsxWriter

# Logging config
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("knowledgebase-mcp")

class KnowledgeBaseMCP:
    def __init__(self):
        self.server = Server("knowledgebase-mcp")
        self.extractor = DocumentExtractor()
        self.docx_writer = DocxWriter()
        self.xlsx_writer = XlsxWriter()
        self.setup_handlers()
        logger.info("KnowledgeBaseMCP sunucu başlatıldı")
    
    def setup_handlers(self):
        """MCP handler'larını kur"""
        
        @self.server.list_tools()
        async def list_tools():
            """Mevcut araçları listele"""
            logger.info("Tools listelendi")
            return [
                types.Tool(
                    name="extract_text_from_file",
                    description="Tek dosyadan text çıkar (PDF, DOCX, PPTX, XLSX)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "Dosya yolu"
                            }
                        },
                        "required": ["file_path"]
                    }
                ),
                types.Tool(
                    name="extract_text_from_directory",
                    description="Klasördeki tüm desteklenen dosyalardan text çıkar",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "directory_path": {
                                "type": "string",
                                "description": "Klasör yolu"
                            },
                            "recursive": {
                                "type": "boolean",
                                "description": "Alt klasörleri de tara",
                                "default": False
                            }
                        },
                        "required": ["directory_path"]
                    }
                ),
                types.Tool(
                    name="list_supported_files",
                    description="Desteklenen dosyaları listele",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "directory_path": {
                                "type": "string",
                                "description": "Taranacak klasör"
                            }
                        },
                        "required": ["directory_path"]
                    }
                ),
                types.Tool(
                    name="create_docx_document",
                    description="DOCX belgesi oluştur",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "content": {
                                "type": "string",
                                "description": "Belge içeriği"
                            },
                            "file_path": {
                                "type": "string",
                                "description": "Dosya yolu (.docx uzantılı)"
                            },
                            "title": {
                                "type": "string",
                                "description": "Belge başlığı (opsiyonel)",
                                "default": ""
                            }
                        },
                        "required": ["content", "file_path"]
                    }
                ),
                types.Tool(
                    name="create_structured_report",
                    description="Yapılandırılmış DOCX raporu oluştur",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "report_data": {
                                "type": "object",
                                "description": "Rapor verisi (JSON formatında)"
                            },
                            "file_path": {
                                "type": "string",
                                "description": "Dosya yolu (.docx uzantılı)"
                            }
                        },
                        "required": ["report_data", "file_path"]
                    }
                ),
                types.Tool(
                    name="create_xlsx_workbook",
                    description="XLSX çalışma kitabı oluştur",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "description": "Sayfa adları ve verileri içeren sözlük"
                            },
                            "file_path": {
                                "type": "string",
                                "description": "Dosya yolu (.xlsx uzantılı)"
                            },
                            "apply_formatting": {
                                "type": "boolean",
                                "description": "Biçimlendirme uygula",
                                "default": True
                            }
                        },
                        "required": ["data", "file_path"]
                    }
                ),
                types.Tool(
                    name="create_xlsx_from_dataframe",
                    description="Pandas DataFrame'lerden XLSX oluştur",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "dataframes": {
                                "type": "object",
                                "description": "Sayfa adları ve DataFrame verileri"
                            },
                            "file_path": {
                                "type": "string",
                                "description": "Dosya yolu (.xlsx uzantılı)"
                            },
                            "include_index": {
                                "type": "boolean",
                                "description": "Index'i dahil et",
                                "default": True
                            }
                        },
                        "required": ["dataframes", "file_path"]
                    }
                ),
                types.Tool(
                    name="append_to_xlsx",
                    description="Mevcut XLSX dosyasına veri ekle",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "XLSX dosya yolu"
                            },
                            "sheet_name": {
                                "type": "string",
                                "description": "Hedef sayfa adı"
                            },
                            "data": {
                                "description": "Eklenecek veri (liste, sözlük veya DataFrame)"
                            }
                        },
                        "required": ["file_path", "sheet_name", "data"]
                    }
                ),
                types.Tool(
                    name="create_xlsx_report",
                    description="Formatlanmış XLSX raporu oluştur",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "report_data": {
                                "type": "object",
                                "description": "Rapor verisi (başlık, açıklama, veri bölümleri)"
                            },
                            "file_path": {
                                "type": "string",
                                "description": "Dosya yolu (.xlsx uzantılı)"
                            }
                        },
                        "required": ["report_data", "file_path"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]):
            """Tool çağrılarını işle"""
            logger.info(f"Tool çağrıldı: {name}")
            
            try:
                if name == "extract_text_from_file":
                    file_path = arguments.get("file_path")
                    if not file_path:
                        return [types.TextContent(type="text", text="Hata: file_path gerekli")]
                    
                    result = await self.extractor.extract_from_file(file_path)
                    return [types.TextContent(type="text", text=result)]
                
                elif name == "extract_text_from_directory":
                    directory_path = arguments.get("directory_path")
                    recursive = arguments.get("recursive", False)
                    
                    if not directory_path:
                        return [types.TextContent(type="text", text="Hata: directory_path gerekli")]
                    
                    result = await self.extractor.extract_from_directory(directory_path, recursive)
                    return [types.TextContent(type="text", text=result)]
                
                elif name == "list_supported_files":
                    directory_path = arguments.get("directory_path")
                    
                    if not directory_path:
                        return [types.TextContent(type="text", text="Hata: directory_path gerekli")]
                    
                    result = await self.extractor.list_supported_files(directory_path, False)
                    return [types.TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]
                
                elif name == "create_docx_document":
                    content = arguments.get("content")
                    file_path = arguments.get("file_path")
                    title = arguments.get("title", "")
                    
                    if not content or not file_path:
                        return [types.TextContent(type="text", text="Hata: content ve file_path gerekli")]
                    
                    result = await self.docx_writer.create_document(content, file_path, title)
                    return [types.TextContent(type="text", text=result)]
                
                elif name == "create_structured_report":
                    report_data = arguments.get("report_data")
                    file_path = arguments.get("file_path")
                    
                    if not report_data or not file_path:
                        return [types.TextContent(type="text", text="Hata: report_data ve file_path gerekli")]
                    
                    result = await self.docx_writer.create_structured_report(report_data, file_path)
                    return [types.TextContent(type="text", text=result)]
                
                elif name == "create_xlsx_workbook":
                    data = arguments.get("data")
                    file_path = arguments.get("file_path")
                    apply_formatting = arguments.get("apply_formatting", True)
                    
                    if not data or not file_path:
                        return [types.TextContent(type="text", text="Hata: data ve file_path gerekli")]
                    
                    result = await self.xlsx_writer.create_workbook(data, file_path, apply_formatting=apply_formatting)
                    return [types.TextContent(type="text", text=result)]
                
                elif name == "create_xlsx_from_dataframe":
                    dataframes = arguments.get("dataframes")
                    file_path = arguments.get("file_path")
                    include_index = arguments.get("include_index", True)
                    
                    if not dataframes or not file_path:
                        return [types.TextContent(type="text", text="Hata: dataframes ve file_path gerekli")]
                    
                    result = await self.xlsx_writer.create_dataframe_workbook(dataframes, file_path, include_index=include_index)
                    return [types.TextContent(type="text", text=result)]
                
                elif name == "append_to_xlsx":
                    file_path = arguments.get("file_path")
                    sheet_name = arguments.get("sheet_name")
                    data = arguments.get("data")
                    
                    if not file_path or not sheet_name or not data:
                        return [types.TextContent(type="text", text="Hata: file_path, sheet_name ve data gerekli")]
                    
                    result = await self.xlsx_writer.append_to_workbook(file_path, sheet_name, data)
                    return [types.TextContent(type="text", text=result)]
                
                elif name == "create_xlsx_report":
                    report_data = arguments.get("report_data")
                    file_path = arguments.get("file_path")
                    
                    if not report_data or not file_path:
                        return [types.TextContent(type="text", text="Hata: report_data ve file_path gerekli")]
                    
                    result = await self.xlsx_writer.create_report_workbook(report_data, file_path)
                    return [types.TextContent(type="text", text=result)]
                
                else:
                    return [types.TextContent(type="text", text=f"Bilinmeyen tool: {name}")]
                    
            except Exception as e:
                logger.error(f"Tool '{name}' hatası: {str(e)}")
                return [types.TextContent(type="text", text=f"Hata: {str(e)}")]

    async def run(self):
        """Sunucuyu çalıştır"""
        try:
            from mcp.server.stdio import stdio_server
            
            logger.info("MCP sunucu başlatılıyor...")
            
            async with stdio_server() as (read_stream, write_stream):
                logger.info("STDIO bağlantısı kuruldu")
                
                await self.server.run(
                    read_stream,
                    write_stream,
                    InitializationOptions(
                        server_name="knowledgebase-mcp",
                        server_version="1.0.0",
                        capabilities=self.server.get_capabilities(
                            notification_options=NotificationOptions(),
                            experimental_capabilities={}
                        )
                    )
                )
        except Exception as e:
            logger.error(f"Sunucu hatası: {e}")
            raise

def main():
    """Ana giriş noktası"""
    try:
        logger.info("KnowledgeBaseMCP başlatılıyor...")
        mcp_server = KnowledgeBaseMCP()
        asyncio.run(mcp_server.run())
    except KeyboardInterrupt:
        logger.info("Sunucu durduruldu")
    except Exception as e:
        logger.error(f"Kritik hata: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()