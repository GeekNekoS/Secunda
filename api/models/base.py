# api/models/base.py
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from dotenv import load_dotenv
import os


load_dotenv()

POSTGRES_DB_URL = os.getenv("POSTGRES_DB_URL")
engine = create_engine(POSTGRES_DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    """Базовый класс для всех моделей"""

    # --- CRUD методы ---
    def save(self, session: Session | None = None):
        db = session or SessionLocal()
        db.add(self)
        db.commit()
        db.refresh(self)
        if session is None:
            db.close()
        return self

    def delete(self, session: Session | None = None):
        db = session or SessionLocal()
        db.delete(self)
        db.commit()
        if session is None:
            db.close()

    def update(self, session: Session | None = None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db = session or SessionLocal()
        db.commit()
        db.refresh(self)
        if session is None:
            db.close()
        return self

    @classmethod
    def bulk_update(cls, filter_dict: dict, update_dict: dict, session: Session | None = None):
        db = session or SessionLocal()
        db.query(cls).filter_by(**filter_dict).update(update_dict, synchronize_session=False)
        db.commit()
        if session is None:
            db.close()

    # --- Получение сессии ---
    @staticmethod
    def get_db():
        """Контекстный менеджер для сессии"""
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
