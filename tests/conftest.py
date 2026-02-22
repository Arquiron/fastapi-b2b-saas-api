import os
import pytest
from fastapi.testclient import TestClient

from app.core.security import hash_api_key
from app.db.session import SessionLocal
from app.tenants.db_model import Tenant
from app.main import app
from app.db.session import engine
from app.db.base import Base
from app.db.deps import get_db

TEST_DB_FILE = "test.db"

@pytest.fixture(autouse=True)
def _reset_db():
    # garante um banco limpo por teste
    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)

    # recria as tabelas
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # cleanup
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def client():
    return TestClient(app)

@pytest.fixture
def tenant_api_key():
    db = SessionLocal()
    api_key = "test-key"
    tenant = Tenant(
        tenant_id="acme",
        name="ACME",
        api_key_hash=hash_api_key(api_key),
    )
    db.add(tenant)
    db.commit()
    db.close()
    return api_key