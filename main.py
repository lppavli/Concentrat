import redis
import uvicorn
from fastapi import FastAPI
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from fastapi import Request
from starlette.middleware.cors import CORSMiddleware

from custom_openapi import custom_openapi
from src.api.v1.resources import users, materials
from src.core import config
from src.db import cache, redis_cache


app = FastAPI(
    # Конфигурируем название проекта. Оно будет отображаться в документации
    title=config.PROJECT_NAME,
    version=config.VERSION,
    # Адрес документации в красивом интерфейсе
    docs_url="/api/openapi",
    redoc_url="/api/redoc",
    # Адрес документации в формате OpenAPI
    openapi_url="/api/openapi.json",
)
# app.openapi = custom_openapi(app)
origins = [
"http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.get("/")
def root():
    return {"service": config.PROJECT_NAME, "version": config.VERSION}


@app.on_event("startup")
def startup():
    """Подключаемся к базам при старте сервера"""
    cache.cache = redis_cache.CacheRedis(
        cache_instance=redis.Redis(
            host=config.REDIS_HOST, port=config.REDIS_PORT, max_connections=10
        )
    )


@app.on_event("shutdown")
def shutdown():
    """Отключаемся от баз при выключении сервера"""
    cache.cache.close()


# Подключаем роутеры к серверу
app.include_router(router=materials.router, prefix="/api/v1/materials")
app.include_router(router=users.router, prefix="/api/v1")


if __name__ == "__main__":
    # Приложение может запускаться командой
    # `uvicorn main:app --host 0.0.0.0 --port 8000`
    # но чтобы не терять возможность использовать дебагер,
    # запустим uvicorn сервер через python
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
    )
