# api/core/db.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from api.core.config import settings


# Базовый класс для моделей
Base = declarative_base()


# Асинхронный движок подключения
engine = create_async_engine(
    settings.POSTGRES_DB_URL,  # важно, чтобы URL был async (см. ниже)
    echo=True,                 # логирование SQL (можно выключить на проде)
    future=True,
)

# Фабрика асинхронных сессий
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)

# Dependency для FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
