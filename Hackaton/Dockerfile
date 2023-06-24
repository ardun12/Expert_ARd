# Используем официальное изображение Python в качестве базового
FROM python:3.9

# Устанавливаем системные зависимости
RUN apt-get update \
    && apt-get install -y libpoppler-cpp-dev

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл requirements в контейнер
COPY requirements.txt .

# Обновляем pip
RUN pip install --no-cache-dir --upgrade pip

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код в контейнер
COPY . .

# Создаем директорию 'static/' внутри контейнера
RUN mkdir static

# Задаем команду для запуска скрипта
CMD ["python", "expert_2.py"]