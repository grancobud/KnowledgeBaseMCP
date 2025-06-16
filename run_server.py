#!/usr/bin/env python3
"""
KnowledgeBaseMCP Launcher - Import sorunlarını çözmek için
"""

import sys
import os
from pathlib import Path

# Proje kök dizinini Python path'ine ekle
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

# Ana modülü import et ve çalıştır
from main import main

if __name__ == "__main__":
    main()
