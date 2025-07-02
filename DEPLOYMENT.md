# KnowledgeBaseMCP Deployment Guide

Bu kılavuz, KnowledgeBaseMCP'yi Claude Desktop ile kullanmak için gerekli adımları açıklar.

## 🔧 Kurulum Adımları

### 1. Gereksinimler
- Python 3.8 veya üzeri
- Claude Desktop uygulaması
- Git (opsiyonel)

### 2. Projeyi İndirin
```bash
# Git ile klonlama
git clone https://github.com/yourusername/KnowledgeBaseMCP.git
cd KnowledgeBaseMCP

# Veya ZIP dosyasını indirip açın
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Kurulumu Test Edin
```bash
python test.py
python test_xlsx.py  # XLSX özelliklerini test etmek için
```

## ⚙️ Claude Desktop Konfigürasyonu

### Windows Konfigürasyonu
Konfigürasyon dosyası konumu:
```
%APPDATA%\Claude\claude_desktop_config.json
```

### macOS Konfigürasyonu
Konfigürasyon dosyası konumu:
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

### Konfigürasyon Dosyası İçeriği
```json
{
  "mcpServers": {
    "knowledgebase": {
      "command": "python",
      "args": ["C:\\tam\\yol\\KnowledgeBaseMCP\\launch_mcp.py"],
      "env": {
        "PYTHONPATH": "C:\\tam\\yol\\KnowledgeBaseMCP\\src"
      }
    }
  }
}
```

**Önemli:** `C:\\tam\\yol\\` kısmını kendi kurulum yolunuzla değiştirin.

### Örnek Tam Konfigürasyon
```json
{
  "mcpServers": {
    "knowledgebase": {
      "command": "python",
      "args": ["C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\KnowledgeBaseMCP\\launch_mcp.py"],
      "env": {
        "PYTHONPATH": "C:\\Users\\mehmet.ozcan\\Desktop\\MCPPlayground\\KnowledgeBaseMCP\\src"
      }
    }
  }
}
```

## 🚀 Claude Desktop'ı Yeniden Başlatın

Konfigürasyon dosyasını güncelledikten sonra:
1. Claude Desktop'ı tamamen kapatın
2. Uygulamayı yeniden başlatın
3. Yeni bir sohbet başlatın

## ✅ Kurulumu Doğrulayın

Claude'a şu mesajı gönderin:
```
KnowledgeBaseMCP araçlarını listele ve test et
```

Başarılı kurulum için şu araçları görmelisiniz:

### Dosya Okuma Araçları
- `extract_text_from_file`
- `extract_text_from_directory`
- `list_supported_files`

### DOCX Oluşturma Araçları
- `create_docx_document`
- `create_structured_report`

### XLSX Oluşturma Araçları
- `create_xlsx_workbook`
- `create_xlsx_from_dataframe`
- `append_to_xlsx`
- `create_xlsx_report`

## 🔍 Sorun Giderme

### Araçlar Görünmüyor
1. Konfigürasyon dosyasının doğru konumda olduğunu kontrol edin
2. Dosya yollarının doğru olduğunu kontrol edin
3. Python'un PATH'te olduğunu kontrol edin
4. Claude Desktop'ı tamamen yeniden başlatın

### Python Hataları
```bash
# Bağımlılıkları yeniden yükleyin
pip install --upgrade -r requirements.txt

# Python versiyonunu kontrol edin
python --version  # 3.8+ olmalı

# Modülleri test edin
python -c "import pandas, openpyxl, docx, pdfplumber; print('Tüm modüller yüklü')"
```

### İzin Hataları
- Klasör izinlerini kontrol edin
- Python'u yönetici olarak çalıştırmayı deneyin
- Antivirus yazılımının Python'u engellemediğini kontrol edin

### Dosya Bulunamadı Hataları
- Mutlak dosya yolları kullanın
- Ters eğik çizgilerin düzgün kaçış karakteriyle yazıldığını kontrol edin
- Türkçe karakterli klasör adlarından kaçının

## 📊 Kullanım Örnekleri

### Basit Dosya Okuma
```
"C:\Users\kullanici\Belgeler\rapor.pdf" dosyasını oku ve özetle
```

### Excel Raporu Oluşturma
```
Satış verilerini içeren bir Excel raporu oluştur:
- Özet sayfası
- Aylık veriler
- Grafik verileri
```

### Klasör Analizi
```
"C:\Projeler\Belgeler" klasöründeki tüm dosyaları analiz et ve bir özet rapor oluştur
```

## 🔧 Gelişmiş Konfigürasyon

### Çoklu MCP Sunucuları
```json
{
  "mcpServers": {
    "knowledgebase": {
      "command": "python",
      "args": ["C:\\path\\to\\KnowledgeBaseMCP\\launch_mcp.py"]
    },
    "other-server": {
      "command": "node",
      "args": ["C:\\path\\to\\other-server\\index.js"]
    }
  }
}
```

### Ortam Değişkenleri
```json
{
  "mcpServers": {
    "knowledgebase": {
      "command": "python",
      "args": ["C:\\path\\to\\KnowledgeBaseMCP\\launch_mcp.py"],
      "env": {
        "PYTHONPATH": "C:\\path\\to\\KnowledgeBaseMCP\\src",
        "LOG_LEVEL": "DEBUG",
        "MAX_FILE_SIZE": "100MB"
      }
    }
  }
}
```

## 📝 Güncelleme

### Yeni Sürüm Kurulumu
```bash
# Mevcut dosyaları yedekleyin
cp claude_desktop_config.json claude_desktop_config.json.backup

# Yeni sürümü indirin
git pull origin main

# Bağımlılıkları güncelleyin
pip install --upgrade -r requirements.txt

# Test edin
python test.py
```

## 🆘 Destek

Sorun yaşıyorsanız:

1. **Logları kontrol edin**: Claude Desktop'ın hata mesajlarını inceleyin
2. **Test scriptlerini çalıştırın**: `python test.py` ve `python test_xlsx.py`
3. **GitHub Issues**: Sorunu GitHub'da rapor edin
4. **Discord/Community**: Topluluk desteği alın

### Log Dosyaları
- Windows: `%APPDATA%\\Claude\\logs\\`
- macOS: `~/Library/Logs/Claude/`

## 🎯 Performans Optimizasyonu

### Büyük Dosyalar İçin
- Dosya boyutunu kontrol edin (>100MB için dikkatli olun)
- Recursive scanning'i sadece gerektiğinde kullanın
- Çok büyük Excel dosyaları için chunk processing kullanın

### Bellek Yönetimi
- Claude Desktop'ı düzenli olarak yeniden başlatın
- Aynı anda çok fazla büyük dosya işlemeyin
- Geçici dosyaları temizleyin

---

**Not**: Bu kılavuz KnowledgeBaseMCP v2.0.0 için hazırlanmıştır. Eski sürümler için farklılıklar olabilir.
