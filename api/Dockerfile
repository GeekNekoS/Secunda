# Используем Python 3.11
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements-api.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements-api.txt

# Копируем весь код приложения
COPY . .

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
