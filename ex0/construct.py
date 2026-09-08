#!/usr/bin/env python3
import sys
import os
import site

# sys.prefix - pasta raiz do Python atualmente em uso
# sys.base_prefix - pasta raiz do python original do sistema
if sys.prefix == sys.base_prefix:
    matrix_status = "You're still plugged in"
    in_venv = False
    virtual_env = os.getenv("VIRTUAL_ENV", "None detected")
    message = (
               "\nWARNING: You're in the global environment!\n"
               "The machines can see everything you install\n"
               "\nTo enter the construct, run:\n"
               "python -m venv matrix_env\n"
               "source matrix_env/bin/activate # On Unix\n"
               "matrix_env\\Scripts\\activate # On Windows\n"
               "\nThen run this program again."
              )
else:
    matrix_status = "Welcome to the construct"
    in_venv = True
    virtual_env = os.path.basename(os.getenv("VIRTUAL_ENV", "None detected"))
    message = (
               "\nSUCCESS: You're in an isolated environment!\n"
               "Safe to install packages without affecting\n"
               "the global system.\n"
              )

print("\nMATRIX STATUS:", matrix_status)
print("\nCurrent Python:", sys.executable)
print("Virtual Environment:", virtual_env)
if in_venv:
    print(f"Environment Path: {sys.prefix}")
print(message)
if in_venv:
    print("Package installation path:")
    print(site.getusersitepackages())
