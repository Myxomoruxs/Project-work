import os
import time
from pathlib import Path
from aiogram import Bot
from bot.config.settings import TEMP_FILES_DIR, ALLOWED_FILE_EXTENSIONS, MAX_FILE_SIZE


async def download_file(bot: Bot, file_id: str, user_id: int) -> str:
    Path(TEMP_FILES_DIR).mkdir(exist_ok=True)

    file = await bot.get_file(file_id)

    timestamp = int(time.time())
    file_extension = Path(file.file_path).suffix
    filename = f"user_{user_id}_{timestamp}{file_extension}"
    save_path = os.path.join(TEMP_FILES_DIR, filename)

    await bot.download_file(file.file_path, save_path)

    return save_path


def validate_file_extension(filename: str, allowed: list = None) -> bool:
    if allowed is None:
        allowed = ALLOWED_FILE_EXTENSIONS

    file_extension = Path(filename).suffix.lower()
    return file_extension in allowed


def validate_file_size(file_size: int) -> bool:
    return file_size <= MAX_FILE_SIZE


def cleanup_file(file_path: str) -> None:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Ошибка при удалении файла {file_path}: {e}")
