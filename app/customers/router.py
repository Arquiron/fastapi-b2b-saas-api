from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.tenant import get_tenant_id
from app.db.deps import get_db
from app.customers.models import CustomerCreate, CustomerOut
from app.customers import repo

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("", response_model=CustomerOut, status_code=status.HTTP_201_CREATED)
def create_customer(
    payload: CustomerCreate,
    tenant_id: str = Depends(get_tenant_id),
    db: Session = Depends(get_db),
):
    try:
        return repo.create_customer(db, tenant_id, payload)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("", response_model=list[CustomerOut])
def list_customers(
    tenant_id: str = Depends(get_tenant_id),
    db: Session = Depends(get_db),
):
    return repo.list_customers(db, tenant_id)

@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer(
    customer_id: int,
    tenant_id: str = Depends(get_tenant_id),
    db: Session = Depends(get_db),
):
    c = repo.get_customer(db, tenant_id, customer_id)
    if not c:
        raise HTTPException(status_code=404, detail="Customer not found")
    return c

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(
    customer_id: int,
    tenant_id: str = Depends(get_tenant_id),
    db: Session = Depends(get_db),
):
    ok = repo.delete_customer(db, tenant_id, customer_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Customer not found")
