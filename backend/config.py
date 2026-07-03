from pathlib import Path
import os
from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from project root
load_dotenv(BASE_DIR / ".env")

print("Looking for .env at:", BASE_DIR / ".env")
print("File exists:", (BASE_DIR / ".env").exists())
print("API Key:", os.getenv("GOOGLE_API_KEY"))