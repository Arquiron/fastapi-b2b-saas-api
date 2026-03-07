from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db, verify_admin
from app.tenants.repo import create_tenant as repo_create_tenant
from app.tenants.schemas import TenantCreate, TenantCreated

router = APIRouter(tags=["tenants"])


@router.post("/tenants", response_model=TenantCreated, dependencies=[Depends(verify_admin)])
def create_tenant(payload: TenantCreate, db: Session = Depends(get_db)):
    tenant, api_key_plain = repo_create_tenant(db, payload)
    return {
        "tenant_id": tenant.tenant_id,
        "name": tenant.name,
        "api_key": api_key_plain,
    }