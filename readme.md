# Система добавления данных о качественных показателях железнорудного концентрата и просмотра сводной информации по всем концентратам
## Используемые технологии
- Код приложения пишется на Python + FastAPI.
- Приложение запускается под управлением сервера uvicorn.
- База данных – PostgreSQL.
- За кеширование данных отвечает – redis cluster.
- Все компоненты системы запускаются через docker.
### Для сборки и запуска проекта выполните следующие команды:
```
    git clone https://github.com/lppavli/Concentrat
    docker-compose up -d --build
    
```
### Для миграций
```
    alembic upgrade head
```
### Документация доступна по ссылке
http://localhost:8000/api/openapi
![](C:\Users\Liliya\PycharmProjects\Concentrat\документация.png)
Для тестирования можно использовать Postman-коллекцию Testing.postman_collection.json