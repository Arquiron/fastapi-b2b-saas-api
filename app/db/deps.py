from typing import Generator
from sqlalchemy.orm import Session
from fastapi import Header, HTTPException, status
from app.db.session import SessionLocal
from app.core.config import settings

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_admin(x_api_key: str = Header(...)):
    if not settings.admin_api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Admin API key not configured",
        )

    if x_api_key != settings.admin_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid admin API key",
        )