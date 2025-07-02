@echo off
echo ==========================================
echo KnowledgeBaseMCP XLSX Test ve Kurulum
echo ==========================================

cd /d "C:\Users\mehmet.ozcan\Desktop\MCPPlayground\KnowledgeBaseMCP"

echo.
echo [1/4] Bağımlılıkları kontrol ediliyor...
python -c "import sys; print(f'Python version: {sys.version}')"

echo.
echo [2/4] Gerekli paketleri yükleniyor...
pip install openpyxl>=3.1.0
pip install pandas>=2.0.0
pip install mcp>=0.9.0
pip install python-docx>=1.1.0
pip install pdfplumber>=0.9.0
pip install python-pptx>=0.6.23
pip install lxml>=4.9.0

echo.
echo [3/4] Import testleri yapılıyor...
python -c "import pandas; print('✓ pandas imported')"
python -c "import openpyxl; print('✓ openpyxl imported')"
python -c "from openpyxl.styles import Font; print('✓ openpyxl.styles imported')"
python -c "import sys; sys.path.insert(0, 'src'); from xlsx_writer import XlsxWriter; print('✓ XlsxWriter imported')"

echo.
echo [4/4] XLSX test çalıştırılıyor...
python test_xlsx.py

echo.
echo Test tamamlandı!
pause
