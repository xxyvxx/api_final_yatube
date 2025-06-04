## Проект «API для Yatube»

Yatube - проект социальной сети. «API для Yatube» расширяет возможности социальной сети. Новый функционал позволяет пользователям публиковать свои посты и управлять подписками через программный интерфейс взаимодействия.


## Установка

1. Клонировать репозиторий:

   ```
   git clone https://github.com/xxyvxx/api_final_yatube.git
   ```

2. Перейти в папку с проектом:

   ```
   cd api_yatube/
   ```

3. Установить виртуальное окружение для проекта:

   ```
   python -m venv venv
   ```

4. Активировать виртуальное окружение для проекта:

   ```
   source venv/Scripts/activate
   ```

5. Установить зависимости:

   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Выполнить миграции на уровне проекта:

   ```
   cd yatube
   python manage.py makemigrations
   python manage.py migrate
   ```


#### После запуска проекта, документация будет доступна по адресу:
`http://localhost:port/redoc/`
