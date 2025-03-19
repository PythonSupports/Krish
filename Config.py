import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")    # Telegram Bot Token from @BotFather
API_ID = int(os.getenv("API_ID"))       # API ID from my.telegram.org
API_HASH = os.getenv("API_HASH")        # API Hash from my.telegram.org
