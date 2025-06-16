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
from extractors import DocumentExtractor

# Logging config
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("knowledgebase-mcp")

class KnowledgeBaseMCP:
    def __init__(self):
        self.server = Server("knowledgebase-mcp")
        self.extractor = DocumentExtractor()
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
                    description="Tek dosyadan text çıkar (PDF, DOCX, PPTX)",
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
