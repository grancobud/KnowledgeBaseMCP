# KnowledgeBaseMCP

A powerful Model Context Protocol (MCP) server for extracting text content from various document formats including PDF, DOCX, and PPTX files. This tool enables AI assistants like Claude to read and analyze document contents from your local knowledge base.

## 🚀 Features

- **Multi-format support**: Extract text from PDF, DOCX, and PPTX files
- **Directory processing**: Process entire directories of documents
- **Recursive scanning**: Optionally scan subdirectories 
- **File metadata**: Get detailed information about document files
- **Error handling**: Robust error handling with clear error messages
- **Async processing**: Efficient asynchronous document processing
- **Easy integration**: Simple setup with Claude Desktop

## 📁 Supported File Types

- **PDF** (.pdf) - Portable Document Format (using pdfplumber)
- **DOCX** (.docx) - Microsoft Word documents  
- **PPTX** (.pptx) - Microsoft PowerPoint presentations

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Claude Desktop application

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/mehmetozcan-zz/KnowledgeBaseMCP.git
cd KnowledgeBaseMCP
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Test the server**
```bash
python test.py
```

## ⚙️ Configuration

### Claude Desktop Integration

Add this server to your Claude Desktop configuration file:

**Windows**: `%APPDATA%\\Claude\\claude_desktop_config.json`  
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "knowledgebase": {
      "command": "python",
      "args": ["path/to/KnowledgeBaseMCP/launch_mcp.py"]
    }
  }
}
```

Replace `path/to/KnowledgeBaseMCP` with your actual installation path.

## 🎯 Usage

Once configured, you can use these tools in Claude:

### Available Tools

#### `extract_text_from_file`
Extract text content from a single document file.

**Parameters:**
- `file_path` (string): Path to the document file

#### `extract_text_from_directory` 
Extract text content from all supported documents in a directory.

**Parameters:**
- `directory_path` (string): Path to the directory containing documents
- `recursive` (boolean, optional): Whether to search subdirectories recursively

#### `list_supported_files`
List all supported document files in a directory with metadata.

**Parameters:**
- `directory_path` (string): Path to the directory to scan

### Example Usage in Claude

```
Please analyze all the documents in my Documents/Reports folder using your KnowledgeBaseMCP tools.
```

Claude will then use the MCP server to extract and analyze the content from your documents.

## 🏗️ Project Structure

```
KnowledgeBaseMCP/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── main.py             # Main MCP server
│   └── extractors.py       # Document processing classes
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
├── README.md              # This file
├── LICENSE                # MIT License
├── launch_mcp.py          # Server launcher
├── run_server.py          # Alternative launcher
└── test.py               # Test script
```

## 🔧 Development

### Running Tests

```bash
python test.py
```

### Adding New File Formats

To add support for additional document formats:

1. Add the file extension to `SUPPORTED_EXTENSIONS` in `extractors.py`
2. Install the required library
3. Add the library check to `check_dependencies()`
4. Implement the extraction method (e.g., `_extract_xlsx()`)
5. Add the format handling to `extract_from_file()`

### Debugging

For debugging MCP connection issues:

1. Check Claude Desktop logs
2. Ensure the server starts without errors:
   ```bash
   python launch_mcp.py
   ```
3. Verify the config file path and format

## 📦 Dependencies

- `mcp>=0.9.0` - Model Context Protocol framework
- `python-docx>=1.1.0` - For DOCX file processing
- `pdfplumber>=0.9.0` - For PDF file processing  
- `python-pptx>=0.6.23` - For PPTX file processing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with the [Model Context Protocol](https://modelcontextprotocol.io/)
- Uses [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF processing
- Uses [python-docx](https://github.com/python-openxml/python-docx) for Word documents
- Uses [python-pptx](https://github.com/scanny/python-pptx) for PowerPoint presentations

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ for the Claude AI community**
