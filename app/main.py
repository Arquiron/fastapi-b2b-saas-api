from fastapi import Depends, FastAPI
from app.core.config import settings
from app.core.tenant import get_tenant_id
from app.customers.router import router as customers_router
from app.db.session import engine
from app.db.base import Base
from app.customers.db_model import Customer  # noqa: F401

app = FastAPI(title=settings.app_name, version="0.2.0")
app.include_router(customers_router)

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok", "env": settings.env}

@app.get("/whoami")
def whoami(tenant_id: str = Depends(get_tenant_id)):
    return {"tenant_id": tenant_id}

