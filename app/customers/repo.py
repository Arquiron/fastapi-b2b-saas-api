from sqlalchemy.orm import Session
from app.customers.db_model import Customer
from app.customers.models import CustomerCreate, CustomerOut
from sqlalchemy.exc import IntegrityError

def create_customer(db: Session, tenant_id: str, data: CustomerCreate) -> CustomerOut:
    row = Customer(tenant_id=tenant_id, name=data.name, email=data.email)
    db.add(row)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists for this tenant")

    db.refresh(row)
    return CustomerOut(id=row.id, name=row.name, email=row.email)

def list_customers(db: Session, tenant_id: str) -> list[CustomerOut]:
    rows = db.query(Customer).filter(Customer.tenant_id == tenant_id).order_by(Customer.id.asc()).all()
    return [CustomerOut(id=r.id, name=r.name, email=r.email) for r in rows]

def get_customer(db: Session, tenant_id: str, customer_id: int) -> CustomerOut | None:
    row = (
        db.query(Customer)
        .filter(Customer.tenant_id == tenant_id, Customer.id == customer_id)
        .first()
    )
    if not row:
        return None
    return CustomerOut(id=row.id, name=row.name, email=row.email)

def delete_customer(db: Session, tenant_id: str, customer_id: int) -> bool:
    row = (
        db.query(Customer)
        .filter(Customer.tenant_id == tenant_id, Customer.id == customer_id)
        .first()
    )
    if not row:
        return False
    db.delete(row)
    db.commit()
    return True
