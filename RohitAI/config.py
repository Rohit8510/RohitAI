import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# AI Model
MODEL = os.getenv(
    "MODEL",
    "deepseek/deepseek-r1-0528:free"
)

# API URL
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Database
DATABASE_PATH = "data/memory.db"

# Bot Settings
TEMPERATURE = 0.7
MAX_TOKENS = 1500
MAX_HISTORY = 20

# Logging
LOG_FILE = "logs/bot.log"
LOG_LEVEL = "INFO"

# Request Timeout
REQUEST_TIMEOUT = 60