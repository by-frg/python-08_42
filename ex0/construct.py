#!/usr/bin/env python3
import sys
import os
import site


if sys.prefix == sys.base_prefix:
    matrix_status = "You're still plugged in"
    in_venv = False
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
    message = (
               "\nSUCCESS: You're in an isolated environment!\n"
               "Safe to install packages without affecting\n"
               "the global system.\n"
              )
    site_pack = site.getsitepackages()

print(f"\nMATRIX STATUS:", matrix_status)
print(f"\nCurrent Python:", sys.executable )
print("Virtual Environment:", end=" ")
print(os.getenv("VIRTUAL_ENV", "None Detected")) # module OS
if in_venv:
    print(f"\nEnvironment Path: {sys.prefix}")
print(message)
if in_venv:
    print("Package installation path:")
    print(site_pack[0])

