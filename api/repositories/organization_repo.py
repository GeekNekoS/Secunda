# api/repositories/organization_repo.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.models.organization import Organization
from api.models.activity import Activity


class OrganizationRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        """Получить все организации"""
        result = await self.db.execute(select(Organization))
        return result.scalars().all()

    async def get_by_id(self, org_id: int):
        """Получить организацию по id"""
        result = await self.db.execute(select(Organization).where(Organization.id == org_id))
        return result.scalars().first()

    async def create(self, org: Organization):
        """Создать новую организацию"""
        self.db.add(org)
        await self.db.commit()
        await self.db.refresh(org)
        return org

    async def get_by_office(self, office_id: int):
        """Получить организации, находящиеся в конкретном здании"""
        result = await self.db.execute(select(Organization).where(Organization.office_id == office_id))
        return result.scalars().all()

    async def get_by_activity(self, activity_id: int):
        """Получить организации по виду деятельности"""
        stmt = select(Organization).join(Organization.activities).where(Activity.id == activity_id)
        result = await self.db.execute(stmt)
        return result.scalars().all()
