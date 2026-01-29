import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

ALLOWED_FILE_EXTENSIONS = [".xls", ".xlsx"]

MAX_FILE_SIZE = 20 * 1024 * 1024

TEMP_FILES_DIR = "temp_files"

LOG_LEVEL = "INFO"
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
