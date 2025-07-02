# CHANGELOG

All notable changes to KnowledgeBaseMCP will be documented in this file.

## [2.0.0] - 2025-06-25

### 🚀 Major Features Added
- **XLSX Support**: Complete Excel spreadsheet reading and writing functionality
- **Multi-format Document Processing**: Now supports PDF, DOCX, PPTX, and XLSX files
- **Advanced Data Analysis**: Extract comprehensive information from Excel files including:
  - Sheet structure and metadata
  - Column information and data types
  - Sample data preview
  - Statistical summaries for numeric columns
  - Non-null value counts

### 📝 New Tools Added

#### XLSX Reading Tools
- Enhanced `extract_text_from_file` to support XLSX files
- Enhanced `extract_text_from_directory` to process XLSX files
- Enhanced `list_supported_files` to include XLSX metadata

#### XLSX Writing Tools
- `create_xlsx_workbook`: Create Excel workbooks with multiple sheets from various data types
- `create_xlsx_from_dataframe`: Convert pandas DataFrames to formatted Excel files
- `append_to_xlsx`: Add data to existing Excel workbooks
- `create_xlsx_report`: Generate professional reports with formatting and structure

### 🛠️ Dependencies Added
- `openpyxl>=3.1.0` - For XLSX file reading and writing
- `pandas>=2.0.0` - For advanced data manipulation and analysis

### 📁 New Files
- `src/xlsx_writer.py` - Complete XLSX creation and manipulation functionality
- `test_xlsx.py` - Comprehensive testing suite for XLSX features

### ✨ Enhancements
- **Professional Formatting**: Automatic header styling, borders, and column width adjustment
- **Error Handling**: Robust error handling for corrupt or malformed Excel files
- **Memory Efficient**: Uses read-only mode for large file processing
- **Async Support**: All XLSX operations are fully asynchronous

### 📊 Data Features
- **Multi-sheet Support**: Handle workbooks with multiple sheets
- **Data Type Detection**: Automatic detection and reporting of column data types
- **Summary Statistics**: Generate descriptive statistics for numeric data
- **Flexible Input**: Support for dictionaries, lists, and pandas DataFrames
- **Template Support**: Professional formatting templates for reports

### 🔧 Technical Improvements
- Enhanced dependency checking with clear error messages
- Improved logging and debugging capabilities
- Better error recovery for partially corrupted files
- Optimized memory usage for large datasets

### 📚 Documentation Updates
- Updated README.md with comprehensive XLSX documentation
- Added usage examples for all new XLSX tools
- Enhanced project structure documentation
- Added troubleshooting guide for Excel-related issues

### 🧪 Testing
- Complete test suite for XLSX functionality
- Integration tests for reading and writing workflows
- Performance tests for large file handling
- Error condition testing

## [1.0.0] - Previous Release

### Initial Features
- PDF text extraction using pdfplumber
- DOCX document processing
- PPTX presentation text extraction
- DOCX document creation
- MCP protocol integration
- Directory scanning functionality
- File metadata extraction

---

## Migration Guide

### From v1.x to v2.0.0

#### New Dependencies
Install the new required packages:
```bash
pip install openpyxl>=3.1.0 pandas>=2.0.0
```

#### New Tool Usage
The XLSX tools follow the same pattern as existing tools:

```python
# Reading XLSX files
result = await extract_text_from_file("path/to/file.xlsx")

# Creating XLSX files
await create_xlsx_workbook(data, "output.xlsx")
await create_xlsx_report(report_data, "report.xlsx")
```

#### Backwards Compatibility
All existing functionality remains unchanged. Version 2.0.0 is fully backwards compatible with 1.x tool calls and configurations.

---

## Future Roadmap

### Planned Features
- **Chart Generation**: Create charts and graphs in Excel files
- **Advanced Formatting**: More styling options and templates
- **CSV Support**: Direct CSV file processing
- **Database Integration**: Export query results to Excel
- **Conditional Formatting**: Apply conditional formatting rules
- **Data Validation**: Add data validation to Excel cells
- **Pivot Tables**: Generate pivot tables programmatically

### Performance Improvements
- **Streaming Processing**: Handle very large files with streaming
- **Parallel Processing**: Multi-threaded file processing
- **Caching**: Intelligent caching for repeated operations
- **Compression**: Optimize file sizes for generated documents

---

## Contributing

We welcome contributions! Please see our contributing guidelines for details on:
- Code style and standards
- Testing requirements
- Documentation updates
- Feature request process

## License

This project is licensed under the MIT License - see the LICENSE file for details.
