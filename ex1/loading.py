#!/usr/bin/env python3
from importlib import metadata, import_module
import sys

lib_dict = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computation",
            "requests": "Network access",
            "matplotlib": "Visualization",
           }
lib_fail: list[str] = []
for lib, msg in lib_dict.items():
    try:
        module = import_module(lib)
        print(f"[OK] {module.__name__} ({metadata.version(lib)})", end=" ")
        print(f"- {msg} ready")
    except Exception:
        print(f"[KO] {lib}")
        lib_fail.append(lib)
if len(lib_fail) > 0:
        print(
              f"\nMissing modules: {', '.join(lib_fail)}"
              "\n\nInstalling with pip requirements.txt, run:"
              "\n $>pip install -r requirements.txt"
              "\nInstalling with Poetry, run:"
              "\n $>poetry install"
             )
        sys.exit(1)