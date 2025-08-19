from fastapi import Depends, Query, APIRouter
from sqlalchemy.orm import Session

from api.app import app
from api.main import verify_api_key
from api.models import Base
from api.models.organization import Organization
from api.models.activity import Activity


router = APIRouter(tags=["search"])


@router.get("/search/by-activity")
def search_organizations_by_activity(
    activity_name: str = Query(..., description="Название вида деятельности, например 'Еда'"),
    _api_key: str = Depends(verify_api_key),
    db: Session = Depends(lambda: next(Base.get_db()))
):
    """Поиск организаций по виду деятельности (с учетом вложенности до 3 уровней)"""
    def get_nested_activities(act: Activity, level=0, max_level=3):
        if level >= max_level:
            return []
        result = [act]
        for child in act.children:
            result.extend(get_nested_activities(child, level + 1, max_level))
        return result

    root_activity = db.query(Activity).filter(Activity.name.ilike(activity_name)).first()
    if not root_activity:
        return {"organizations": []}

    activities = get_nested_activities(root_activity)
    activity_ids = [a.id for a in activities]

    organizations = (
        db.query(Organization)
        .join(Organization.activities)
        .filter(Activity.id.in_(activity_ids))
        .all()
    )

    return {"organizations": [org.name for org in organizations]}


@router.get("/search/by-name")
def search_organizations_by_name(
    name: str = Query(..., description="Название организации"),
    _api_key: str = Depends(verify_api_key),
    db: Session = Depends(lambda: next(Base.get_db()))
):
    """Поиск организаций по названию"""
    organizations = (
        db.query(Organization)
        .filter(Organization.name.ilike(f"%{name}%"))
        .all()
    )
    return {"organizations": [org.name for org in organizations]}
