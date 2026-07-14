import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Telegram
# ==========================================

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==========================================
# OpenRouter
# ==========================================

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = os.getenv(
    "MODEL",
    "openai/gpt-4.1-mini"
)

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# ==========================================
# Database
# ==========================================

DATABASE_PATH = "data/memory.db"

# ==========================================
# AI Settings
# ==========================================

TEMPERATURE = 0.7
MAX_TOKENS = 1500
MAX_HISTORY = 20
REQUEST_TIMEOUT = 60

# ==========================================
# Features
# ==========================================

ENABLE_MEMORY = True
ENABLE_IMAGE_ANALYSIS = True
ENABLE_WEB_SEARCH = True
ENABLE_STREAMING = False

# ==========================================
# Logging
# ==========================================

LOG_FILE = "logs/bot.log"
LOG_LEVEL = "INFO"
