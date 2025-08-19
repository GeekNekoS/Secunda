from api.endpoints import organizations, buildings, search
from fastapi import FastAPI


app = FastAPI(title="Secunda API")


# подключаем роутеры
# app.include_router(organizations.router, prefix="/organizations")
# app.include_router(buildings.router, prefix="/buildings")
# app.include_router(search.router, prefix="/search")
