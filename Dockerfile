# Используем образ Python
FROM python:3.8

# Установка зависимостей
RUN apt-get update && apt-get install -y postgresql

# Установка зависимостей Python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем исходный код приложения
COPY . .

# Запускаем скрипт для создания базы данных
WORKDIR /app/parks-api/parks
RUN python manage.py makemigrations; python manage.py migrate

# Запускаем сервер API
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
