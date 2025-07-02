#!/usr/bin/env python3
"""
Test script for KnowledgeBaseMCP
"""

import asyncio
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from extractors import DocumentExtractor

async def test_extractor():
    """Test the document extractor"""
    print("Testing KnowledgeBaseMCP Document Extractor")
    print("=" * 50)
    
    extractor = DocumentExtractor()
    
    # Test directory listing
    test_dir = input("Enter directory path to test (or press Enter for current dir): ").strip()
    if not test_dir:
        test_dir = "."
    
    print(f"\n1. Testing directory listing for: {test_dir}")
    files = await extractor.list_supported_files(test_dir, recursive=True)
    
    if files and not files[0].get("error"):
        print(f"Found {len(files)} supported files:")
        for file_info in files:
            print(f"  - {file_info['name']} ({file_info['type']}, {file_info['size_mb']} MB)")
    else:
        print("No supported files found or error occurred")
        if files and files[0].get("error"):
            print(f"Error: {files[0]['error']}")
    
    # Test single file extraction
    if files and not files[0].get("error"):
        print(f"\n2. Testing text extraction from first file:")
        first_file = files[0]["path"]
        print(f"Processing: {first_file}")
        
        text = await extractor.extract_from_file(first_file)
        print(f"Extracted text length: {len(text)} characters")
        print("First 500 characters:")
        print("-" * 30)
        print(text[:500])
        print("-" * 30)
        
        # Test file info
        print(f"\n3. Testing file info:")
        info = await extractor.get_file_info(first_file)
        print(f"File info: {info}")
    
    print("\nTest completed!")

if __name__ == "__main__":
    asyncio.run(test_extractor())
