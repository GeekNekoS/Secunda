from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api.main import verify_api_key
from api.models import Base
from api.models.office import Office


router = APIRouter(tags=["buildings"])


@router.get("/")
def get_offices(
    _api_key: str = Depends(verify_api_key),
    db: Session = Depends(lambda: next(Base.get_db()))
):
    offices = db.query(Office).all()
    return {
        "offices": [
            {
                "id": office.id,
                "address": office.address,
                "latitude": office.latitude,
                "longitude": office.longitude,
            }
            for office in offices
        ]
    }
