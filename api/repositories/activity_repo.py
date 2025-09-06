# api/repositories/activity_repo.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.models.activity import Activity


class ActivityRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        """Получить все виды деятельности"""
        result = await self.db.execute(select(Activity))
        return result.scalars().all()

    async def get_by_id(self, activity_id: int):
        """Получить деятельность по id"""
        result = await self.db.execute(
            select(Activity).where(Activity.id == activity_id)
        )
        return result.scalars().first()

    async def create(self, activity: Activity):
        """Создать новый вид деятельности"""
        self.db.add(activity)
        await self.db.commit()
        await self.db.refresh(activity)
        return activity

    async def get_children(self, parent_id: int):
        """Получить все подкатегории деятельности"""
        result = await self.db.execute(
            select(Activity).where(Activity.parent_id == parent_id)
        )
        return result.scalars().all()
