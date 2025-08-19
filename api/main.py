from fastapi import Header, HTTPException
from api.config import settings


API_KEY = settings.API_KEY


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
