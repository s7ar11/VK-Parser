import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

# Читаем список групп из переменной VK_GROUPS
GROUPS = os.getenv("VK_GROUPS", "").split(",")

# Удаляем пустые строки (если есть)
GROUPS = [group.strip() for group in GROUPS if group.strip()]