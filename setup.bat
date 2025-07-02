@echo off
echo ==========================================
echo KnowledgeBaseMCP Kurulum ve Test Script
echo ==========================================

cd /d "C:\Users\mehmet.ozcan\Desktop\MCPPlayground\KnowledgeBaseMCP"

echo.
echo [1/5] Bağımlılıkları yükleniyor...
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo HATA: Bağımlılık yüklemesi başarısız!
    pause
    exit /b 1
)

echo.
echo [2/5] Modül testleri yapılıyor...
python -c "import pandas, openpyxl, docx, pdfplumber, pptx, mcp; print('✓ Tüm modüller yüklü')"
if %ERRORLEVEL% neq 0 (
    echo HATA: Modül testi başarısız!
    pause
    exit /b 1
)

echo.
echo [3/5] Temel testler çalıştırılıyor...
python test.py
if %ERRORLEVEL% neq 0 (
    echo UYARI: Temel test başarısız!
)

echo.
echo [4/5] XLSX testleri çalıştırılıyor...
python test_xlsx.py
if %ERRORLEVEL% neq 0 (
    echo UYARI: XLSX test başarısız!
)

echo.
echo [5/5] MCP sunucu testi...
echo MCP sunucu 5 saniye test edilecek...
timeout /t 2 /nobreak > nul
start /b python launch_mcp.py > mcp_test.log 2>&1
timeout /t 5 /nobreak > nul
taskkill /f /im python.exe /fi "WINDOWTITLE eq launch_mcp.py" > nul 2>&1

echo.
echo ==========================================
echo Kurulum tamamlandı!
echo ==========================================
echo.
echo Şimdi Claude Desktop konfigürasyonunu yapın:
echo 1. Claude Desktop'ı kapatın
echo 2. %APPDATA%\Claude\claude_desktop_config.json dosyasını düzenleyin
echo 3. Konfigürasyonu ekleyin ve Claude'u yeniden başlatın
echo.
echo Konfigürasyon dosyası içeriği:
echo {
echo   "mcpServers": {
echo     "knowledgebase": {
echo       "command": "python",
echo       "args": ["C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\KnowledgeBaseMCP\\launch_mcp.py"],
echo       "env": {
echo         "PYTHONPATH": "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\KnowledgeBaseMCP\\src"
echo       }
echo     }
echo   }
echo }

pause
