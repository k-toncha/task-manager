# 1. Базовый образ с Python
FROM python:3.12-slim

# 2. Переменные окружения (чтобы Python работал корректно в контейнере)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Рабочая директория внутри контейнера
WORKDIR /app

# 4. Копируем список зависимостей
COPY requirements.txt .

# 5. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 6. Копируем весь проект внутрь контейнера
COPY . .

# 7. Команда запуска контейнера
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
