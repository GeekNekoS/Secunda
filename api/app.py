# api/app.py
from fastapi import FastAPI
from api.endpoints import organizations, buildings, search

app = FastAPI(
    title="Secunda API",
    description="API для управления организациями, зданиями и поиском",
    version="1.0.0",
    docs_url="/docs",      # Swagger UI
    redoc_url="/redoc"     # Redoc
)


# подключаем роутеры
app.include_router(organizations.router, prefix="/organizations")
app.include_router(buildings.router, prefix="/buildings")
app.include_router(search.router, prefix="/search")
