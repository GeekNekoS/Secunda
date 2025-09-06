# api/repositories/office_repo.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.models.office import Office


class OfficeRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        """Получить все здания"""
        result = await self.db.execute(select(Office))
        return result.scalars().all()

    async def get_by_id(self, office_id: int):
        """Получить здание по id"""
        result = await self.db.execute(select(Office).where(Office.id == office_id))
        return result.scalars().first()

    async def create(self, office: Office):
        """Создать новое здание"""
        self.db.add(office)
        await self.db.commit()
        await self.db.refresh(office)
        return office
