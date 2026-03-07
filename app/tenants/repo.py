import secrets
from sqlalchemy.orm import Session

from app.core.security import hash_api_key
from app.tenants.db_model import Tenant
from app.tenants.schemas import TenantCreate


def create_tenant(db: Session, data: TenantCreate) -> Tenant | str:

    api_key_plain = secrets.token_urlsafe(32)
    api_key_hash = hash_api_key(api_key_plain)

    tenant = Tenant(
        tenant_id=data.tenant_id,
        name=data.name,
        api_key_hash=api_key_hash,
    )
    db.add(tenant)
    db.commit()
    db.refresh(tenant)

    return tenant, api_key_plain