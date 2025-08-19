from fastapi import Depends, Query, HTTPException, APIRouter
from sqlalchemy.orm import Session

from api.app import app
from api.main import verify_api_key
from api.models import Base
from api.models.organization import Organization
from api.models.activity import Activity


router = APIRouter(tags=["organizations"])


@router.get("/organizations/by-building")
def get_organizations_by_building(
    building_id: int = Query(..., description="ID здания"),
    _api_key: str = Depends(verify_api_key),
    db: Session = Depends(lambda: next(Base.get_db()))
):
    """Список организаций по зданию"""
    organizations = db.query(Organization).filter(Organization.building_id == building_id).all()
    return {"organizations": [org.name for org in organizations]}


@router.get("/organizations/by-activity")
def get_organizations_by_activity(
    activity_id: int = Query(..., description="ID вида деятельности"),
    _api_key: str = Depends(verify_api_key),
    db: Session = Depends(lambda: next(Base.get_db()))
):
    """Список организаций по виду деятельности"""
    organizations = (
        db.query(Organization)
        .join(Organization.activities)
        .filter(Activity.id == activity_id)
        .all()
    )
    return {"organizations": [org.name for org in organizations]}


@router.get("/organizations/by-radius")
def get_organizations_by_radius(
    lat: float = Query(..., description="Широта центра"),
    lon: float = Query(..., description="Долгота центра"),
    radius: float = Query(..., description="Радиус поиска в метрах"),
    _api_key: str = Depends(verify_api_key),
    db: Session = Depends(lambda: next(Base.get_db()))
):
    """Cписок организаций в радиусе"""
    # Пример: простая "квадратная" фильтрация
    organizations = (
        db.query(Organization)
        .filter(
            (Organization.latitude.between(lat - 0.01, lat + 0.01)) &
            (Organization.longitude.between(lon - 0.01, lon + 0.01))
        )
        .all()
    )
    return {"organizations": [org.name for org in organizations]}


@router.get("/organizations/{org_id}")
def get_organization_by_id(
    org_id: int,
    _api_key: str = Depends(verify_api_key),
    db: Session = Depends(lambda: next(Base.get_db()))
):
    """Информация об организации по ID"""
    org = db.query(Organization).filter(Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Организация не найдена")
    return {
        "id": org.id,
        "name": org.name,
        "building_id": org.building_id,
        "phones": [phone.number for phone in org.phones],
        "activities": [activity.name for activity in org.activities],
    }
