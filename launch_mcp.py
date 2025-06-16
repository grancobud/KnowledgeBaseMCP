#!/usr/bin/env python3
"""
Tam yol ile KnowledgeBaseMCP launcher 
"""

import sys
import os
from pathlib import Path

# Mutlak path'lerle çalış
script_dir = Path(__file__).absolute().parent
src_dir = script_dir / "src"

# Sys.path'e ekle
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

# Working directory'i değiştir
os.chdir(str(src_dir))

try:
    # Import ve çalıştır
    from main import main
    if __name__ == "__main__":
        main()
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)
