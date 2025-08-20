import os

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "12345"))
API_HASH = os.environ.get("API_HASH", "")

# Channel & Owner Info
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002973651102"))  # Your DB channel ID
OWNER = os.environ.get("OWNER", "Magic_Mall_GameShop")  # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "1849257766"))  # Owner ID

# Database Info
PORT = int(os.environ.get("PORT", "8080"))
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "FileStore")

# Optional
SESSION_NAME = os.environ.get("SESSION_NAME", "FileStoreBot")
