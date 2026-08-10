#!/usr/bin/env python3
import sys
import os
try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing modules: 'python-dotenv'")
    print("run:\n pip install -r requirements.txt")
    sys.exit(1)

# Load environment variables from .env file
load_dotenv()
matrix_mode = os.getenv("MATRIX_MODE", "development")
db_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_lvl = os.getenv("LOG_LEVEL", "DEBUG")
zion_netw = os.getenv("ZION_ENDPOINT", "Online")
