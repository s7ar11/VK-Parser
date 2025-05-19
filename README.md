# VK-Parser
Парсер постов и комментариев из групп VK
# Парсер постов и комментариев из групп VK

[![GNU General Public License (GPL)](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://opensource.org/licenses/GPL-3.0)

Автоматический парсер для сбора постов и комментариев из групп ВКонтакте с сохранением результатов в CSV.

---

## 📋 Особенности
- Получение постов через API VK (`wall.get`).
- Сбор комментариев к каждому посту (`wall.getComments`).
- Сохранение данных в CSV (посты и комментарии отдельно).
- Обработка ошибок API (повторные запросы, ограничение лимитов).
- Поддержка нескольких групп за один запуск.

---

## ⚙️ Требования
- Python 3.11+
- Библиотеки:
  - `requests`
  - `pandas`
  - `python-dotenv`
  - `tqdm`

---

## 🛠️ Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/s7ar11/VK-Parser.git
   cd VK-Parser

    Установите зависимости:
    pip install -r requirements.txt

Создайте файл .env:

    VK_TOKEN=ваш_токен_vk_api
    VK_GROUPS=group1,group2,group3

Как получить VK API :
    (https://smmplanner.com/blog/gaid-po-api-vk-kak-podkliuchit-i-ispolzovat/#02)

---

## 🚀 Использование

    Настройте список групп в main.py:   

    GROUPS = [
        "pro_che",
        "secrets_of_teachers",
        # Добавьте свои группы (screen_name из URL)
    ]

Запустите парсер:

    python main.py

Результаты будут сохранены в папке output:

        posts.csv — посты.

        comments.csv — комментарии.

---

## 📝 Лицензия

Этот проект распространяется под лицензией GNU General Public License v3.0.

Авторы: s7ar11 Vldln
