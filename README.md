# Code example
__example with using FastAPI, Tortoise ORM and Docker__

Скопируйте к себе проект и добавьте в корень проекта файл `.env` со следующим содержимым:

```
POSTGRES_DB=project_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=asHvgnoI02S3oEc
POSTGRES_HOST=db
POSTGRES_PORT=5432

```
Затем выполните команды `sudo docker-compose build` и `sudo docker-compose up`

Приложение будет доступно по адресу `http://127.0.0.1:8000/`