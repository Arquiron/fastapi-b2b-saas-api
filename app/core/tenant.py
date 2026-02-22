from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_api_key
from app.db.deps import get_db
from app.tenants.db_model import Tenant

def get_tenant_id(
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
    db: Session = Depends(get_db),
) -> str:
    if not x_api_key:
        raise HTTPException(status_code=401, detail="X-API-Key header is required")

    h = hash_api_key(x_api_key)
    tenant = db.query(Tenant).filter(Tenant.api_key_hash == h).first()
    if not tenant:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return tenant.tenant_id