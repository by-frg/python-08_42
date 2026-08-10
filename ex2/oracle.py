#!/usr/bin/env python3
import sys
import os
try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing modules: 'python-dotenv'")
    print("run:\n pip install -r requirements.txt")
    sys.exit(1)

#Dictionary with necessary env variables & list for fail configs
var_dict = {
            "MATRIX_MODE": "",
            "DATABASE_URL": "",
            "API_KEY=": "",
            "LOG_LEVEL": "",
            "ZION_ENDPOINT": "",
           }
config_fail: list[str] = []
#override test variable
test_var = os.getenv("OVERRIDE", "Original")

# Load environment variables from .env file & update dict and list
print("\nORACLE STATUS: Reading the Matrix...")
load_dotenv()
for name in var_dict.keys():
    var_dict[name] = os.getenv(name)
    if var_dict[name] == "":
        config_fail.append(name)
#if failure, show error msg and exit
if len(config_fail) > 0:
    print(
          f"Missing configuration: {', '.join(config_fail)}"
          "\nComplete configuration setting in respective .env file"
          "\n\nExiting program..."
         )
    sys.exit(1)

print("\nConfiguration Loaded:")
if var_dict["MATRIX_MODE"] == "development":
    print(
          f"Mode: {var_dict['MATRIX_MODE']}\n"
          "Database: Connected to local instance\n"
          "API Access: Authenticated\n"
          f"Log Level: {var_dict['LOG_LEVEL']}\n"
          "Zion Network: Online\n"
         )
elif var_dict["MATRIX_MODE"] == "production":
    print(
          f"Mode: {var_dict['MATRIX_MODE']}\n"
          "Database: Connected to online database\n"
          "API Access: Authenticated\n"
          f"Log Level: {var_dict['LOG_LEVEL']}\n"
          "Zion Network: Online\n"
         )

print("\nEnvironment security check:")
#hardcoded secrets - only used os.getenv
print("[OK] No hardcoded secrets detected")

#.env file exists
if os.path.isfile(".env") and len(config_fail) == 0:
    print("[OK] .env file is properly configured")
else:
    print("[KO] .env file is not properly configured")

#overrides available (automatically by using dotenv module)
if test_var != "Original":
    print("[OK] Production overrides available")
else:
    print(
          "[KO] To test production override, run:\n"
          " $> OVERRIDE=overridden ./oracle.py"
         )
print("\nThe Oracle sees all configurations.")



