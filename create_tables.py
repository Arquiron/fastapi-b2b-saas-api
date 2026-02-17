from app.db.session import engine
from app.db.base import Base
from app.customers.db_model import Customer

Base.metadata.create_all(bind=engine)


