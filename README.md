# ToDo App

Это простое веб-приложение на Django для управления задачами. Приложение использует Docker для контейнеризации, что
делает его легко развертываемым и масштабируемым.

## Запуск приложения

Для запуска этого приложения, убедитесь, что у вас установлены Docker и Docker Compose. Затем выполните следующие шаги:

1. Клонируйте этот репозиторий:

   ```bash
   git clone https://github.com/airmely/todoapp.git
   cd todoapp

2. Введите эти команды:
   docker-compose up
   docker-compose run web python manage.py makemigrations
   docker-compose run web python manage.py migrate
   docker-compose up
3. Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к приложению.
