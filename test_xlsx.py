#!/usr/bin/env python3
"""
Test script for KnowledgeBaseMCP XLSX functionality
"""

import asyncio
import json
import sys
from pathlib import Path
import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from extractors import DocumentExtractor
from xlsx_writer import XlsxWriter

async def test_xlsx_reading():
    """Test XLSX file reading functionality"""
    print("=== Testing XLSX Reading ===")
    
    extractor = DocumentExtractor()
    
    # Test with existing XLSX files in the playground
    test_files = [
        "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\Aday değerlendirme\\Aday Değerlendirme - QA-BA.xlsx",
        "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\OneDrive_1_17.06.2025\\Appendix\\Appendix 2 - Go-Live Readiness Steps.xlsx"
    ]
    
    for file_path in test_files:
        if Path(file_path).exists():
            print(f"\n--- Testing: {Path(file_path).name} ---")
            result = await extractor.extract_from_file(file_path)
            print(result[:500] + "..." if len(result) > 500 else result)
        else:
            print(f"File not found: {file_path}")

async def test_xlsx_writing():
    """Test XLSX file writing functionality"""
    print("\n=== Testing XLSX Writing ===")
    
    writer = XlsxWriter()
    
    # Test 1: Simple data workbook
    print("\n--- Test 1: Simple Data Workbook ---")
    simple_data = {
        "Sheet1": {
            "Name": "Mehmet",
            "Age": 30,
            "City": "Frankfurt"
        },
        "Sheet2": [
            ["Product", "Price", "Stock"],
            ["Laptop", 1000, 50],
            ["Mouse", 25, 200],
            ["Keyboard", 75, 100]
        ]
    }
    
    result = await writer.create_workbook(
        simple_data, 
        "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\test_simple.xlsx"
    )
    print(result)
    
    # Test 2: DataFrame workbook
    print("\n--- Test 2: DataFrame Workbook ---")
    df1 = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 75000, 85000]
    })
    
    df2 = pd.DataFrame({
        'Product': ['A', 'B', 'C'],
        'Sales': [100, 150, 120],
        'Revenue': [10000, 22500, 18000]
    })
    
    dataframes = {
        "Employees": df1,
        "Sales": df2
    }
    
    result = await writer.create_dataframe_workbook(
        dataframes, 
        "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\test_dataframes.xlsx"
    )
    print(result)
    
    # Test 3: Report workbook
    print("\n--- Test 3: Report Workbook ---")
    report_data = {
        "title": "Monthly Sales Report",
        "description": "Sales analysis for current month",
        "data": {
            "Summary": {
                "Total Sales": 50000,
                "Total Orders": 150,
                "Average Order": 333.33,
                "Top Product": "Laptop"
            },
            "Details": [
                ["Date", "Product", "Quantity", "Revenue"],
                ["2025-01-01", "Laptop", 5, 5000],
                ["2025-01-02", "Mouse", 20, 500],
                ["2025-01-03", "Keyboard", 10, 750]
            ]
        }
    }
    
    result = await writer.create_report_workbook(
        report_data, 
        "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\test_report.xlsx"
    )
    print(result)
    
    # Test 4: Append to existing file
    print("\n--- Test 4: Append Data ---")
    new_data = [
        ["2025-01-04", "Monitor", 3, 900],
        ["2025-01-05", "Speaker", 8, 400]
    ]
    
    result = await writer.append_to_workbook(
        "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\test_report.xlsx",
        "Details",
        new_data
    )
    print(result)

async def test_integration():
    """Test reading and writing together"""
    print("\n=== Testing Integration ===")
    
    extractor = DocumentExtractor()
    writer = XlsxWriter()
    
    # Read an existing XLSX file
    original_file = "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\Aday değerlendirme\\Aday Değerlendirme - QA-BA.xlsx"
    
    if Path(original_file).exists():
        print(f"Reading original file: {Path(original_file).name}")
        content = await extractor.extract_from_file(original_file)
        
        # Create a summary report
        summary_data = {
            "title": "File Analysis Report",
            "description": f"Analysis of {Path(original_file).name}",
            "data": {
                "File_Info": {
                    "Original_File": str(original_file),
                    "File_Size": f"{Path(original_file).stat().st_size / 1024:.2f} KB",
                    "Analysis_Date": "2025-06-25",
                    "Content_Length": len(content)
                },
                "Content_Preview": [
                    ["Section", "Content"],
                    ["First_100_chars", content[:100]],
                    ["Last_100_chars", content[-100:]],
                    ["Total_Length", str(len(content))]
                ]
            }
        }
        
        result = await writer.create_report_workbook(
            summary_data,
            "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\analysis_report.xlsx"
        )
        print(result)
    else:
        print(f"Original file not found: {original_file}")

async def main():
    """Main test function"""
    print("KnowledgeBaseMCP XLSX Functionality Test")
    print("=" * 50)
    
    try:
        await test_xlsx_reading()
        await test_xlsx_writing()
        await test_integration()
        
        print("\n" + "=" * 50)
        print("All tests completed!")
        
    except Exception as e:
        print(f"Test error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
