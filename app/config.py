import os
from dotenv import load_dotenv

load_dotenv()

# OCR
OCR_LANG = "fra"

# LLM
LLM_MODEL_NAME = os.getenv("LLM_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")
LLM_TEMPERATURE = 0.0

# MCP
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:8080/mcp")

# Validation
CONFIDENCE_THRESHOLD = 0.85

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
