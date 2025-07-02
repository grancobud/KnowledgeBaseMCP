# KnowledgeBaseMCP

A powerful Model Context Protocol (MCP) server for extracting text content from various document formats including PDF, DOCX, PPTX, and XLSX files. This tool enables AI assistants like Claude to read and analyze document contents from your local knowledge base, and also create new Excel spreadsheets.

## 🚀 Features

### Document Reading
- **Multi-format support**: Extract text from PDF, DOCX, PPTX, and XLSX files
- **Directory processing**: Process entire directories of documents
- **Recursive scanning**: Optionally scan subdirectories 
- **File metadata**: Get detailed information about document files
- **Error handling**: Robust error handling with clear error messages
- **Async processing**: Efficient asynchronous document processing

### Excel Spreadsheet Creation
- **XLSX workbook creation**: Create Excel files with multiple sheets
- **DataFrame support**: Convert pandas DataFrames to Excel
- **Data formatting**: Apply professional formatting and styling
- **Report generation**: Create structured reports with summaries
- **Data appending**: Add data to existing Excel files
- **Template support**: Use predefined templates for consistent formatting

### Integration
- **Easy integration**: Simple setup with Claude Desktop
- **MCP protocol**: Built on the Model Context Protocol standard

## 📁 Supported File Types

### Reading Support
- **PDF** (.pdf) - Portable Document Format (using pdfplumber)
- **DOCX** (.docx) - Microsoft Word documents  
- **PPTX** (.pptx) - Microsoft PowerPoint presentations
- **XLSX** (.xlsx) - Microsoft Excel spreadsheets (using openpyxl and pandas)

### Writing Support
- **DOCX** (.docx) - Create Word documents with formatting
- **XLSX** (.xlsx) - Create Excel workbooks with multiple sheets, formatting, and charts

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

#### Document Reading Tools

##### `extract_text_from_file`
Extract text content from a single document file.

**Parameters:**
- `file_path` (string): Path to the document file

##### `extract_text_from_directory` 
Extract text content from all supported documents in a directory.

**Parameters:**
- `directory_path` (string): Path to the directory containing documents
- `recursive` (boolean, optional): Whether to search subdirectories recursively

##### `list_supported_files`
List all supported document files in a directory with metadata.

**Parameters:**
- `directory_path` (string): Path to the directory to scan

#### DOCX Creation Tools

##### `create_docx_document`
Create a new Word document with text content.

**Parameters:**
- `content` (string): Document content
- `file_path` (string): Output file path (.docx extension)
- `title` (string, optional): Document title

##### `create_structured_report`
Create a structured Word report with formatting.

**Parameters:**
- `report_data` (object): Report data structure
- `file_path` (string): Output file path (.docx extension)

#### XLSX Creation Tools

##### `create_xlsx_workbook`
Create a new Excel workbook with multiple sheets.

**Parameters:**
- `data` (object): Dictionary with sheet names as keys and data as values
- `file_path` (string): Output file path (.xlsx extension)
- `apply_formatting` (boolean, optional): Apply default formatting

##### `create_xlsx_from_dataframe`
Create Excel workbook from pandas DataFrames.

**Parameters:**
- `dataframes` (object): Dictionary with sheet names and DataFrame data
- `file_path` (string): Output file path (.xlsx extension)
- `include_index` (boolean, optional): Include DataFrame index

##### `append_to_xlsx`
Append data to existing Excel workbook.

**Parameters:**
- `file_path` (string): Path to existing XLSX file
- `sheet_name` (string): Target sheet name
- `data` (any): Data to append (list, dict, or DataFrame)

##### `create_xlsx_report`
Create a formatted Excel report with multiple sections.

**Parameters:**
- `report_data` (object): Report structure with title, description, and data sections
- `file_path` (string): Output file path (.xlsx extension)

### Example Usage in Claude

#### Reading Documents
```
Please analyze all the documents in my Documents/Reports folder using your KnowledgeBaseMCP tools.
```

#### Creating Excel Reports
```
Create an Excel report with sales data for Q1 2025. Include a summary sheet and detailed transaction data.
```

#### Data Analysis and Export
```
Read the data from 'financial_report.xlsx' and create a new Excel file with a summary analysis.
```

#### Document Conversion
```
Extract content from all PDF files in my research folder and create a consolidated Excel workbook with the findings.
```

Claude will then use the MCP server to extract and analyze the content from your documents or create new Excel files as requested.

## 🏗️ Project Structure

```
KnowledgeBaseMCP/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── main.py             # Main MCP server
│   ├── extractors.py       # Document reading classes
│   ├── docx_writer.py      # Word document creation
│   └── xlsx_writer.py      # Excel spreadsheet creation
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
├── README.md              # This file
├── LICENSE                # MIT License
├── launch_mcp.py          # Server launcher
├── run_server.py          # Alternative launcher
├── test.py               # Basic test script
└── test_xlsx.py          # XLSX functionality tests
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

### Core Dependencies
- `mcp>=0.9.0` - Model Context Protocol framework

### Document Reading
- `python-docx>=1.1.0` - For DOCX file processing
- `pdfplumber>=0.9.0` - For PDF file processing  
- `python-pptx>=0.6.23` - For PPTX file processing
- `openpyxl>=3.1.0` - For XLSX file reading/writing
- `pandas>=2.0.0` - For advanced data manipulation and analysis

### Additional
- `lxml>=4.9.0` - XML processing support

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