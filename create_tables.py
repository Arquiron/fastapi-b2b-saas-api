from app.db.session import engine
from app.db.base import Base
from app.customers.db_model import Customer
from app.tenants.db_model import Tenant

Base.metadata.create_all(bind=engine)


