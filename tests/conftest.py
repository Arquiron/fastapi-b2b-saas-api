import os
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db.session import engine
from app.db.base import Base
from app.db.deps import get_db
from app.db.session import SessionLocal

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
