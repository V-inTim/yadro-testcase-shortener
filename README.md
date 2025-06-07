# Тестовое задание "URL Alias Service"

## Используемые технологии
Django, DRF, Postgres

## Запуск программы с помощью docker-compose

`docker-compose up -d`

## API
openapi по запросу http:/localhost:8000/docs/
Коллекции postman в файле yadro-testcase.postman_collection.json
## Дополнительно 
- Код написан с flake8 (конфигурация прописана в setup.cfg)
- Модели поключены к админке
- Переменные перенесены в .env из соображений безопасности
- Добавлен workflow git actions для запуска тестов и проверки code style по flake8
- Коллекции postman в файле yadro-testcase.postman_collection.json