from fastapi.testclient import TestClient
from app.main import app
from tests.conftest import client

def test_whoami_requires_tenant_header(client):
    r = client.get("/whoami")
    assert r.status_code == 400

def test_customers_crud_per_tenant(client):
    headers = {"X-Tenant-ID": "acme"}

    # create
    r = client.post("/customers", json={"name": "ACME Buyer", "email": "buyer@acme.com"}, headers=headers)
    assert r.status_code == 201
    created = r.json()
    assert created["id"] == 1

    # list
    r = client.get("/customers", headers=headers)
    assert r.status_code == 200
    assert len(r.json()) >= 1

    # get
    r = client.get("/customers/1", headers=headers)
    assert r.status_code == 200
    assert r.json()["email"] == "buyer@acme.com"

    # delete
    r = client.delete("/customers/1", headers=headers)
    assert r.status_code == 204

    # get after delete
    r = client.get("/customers/1", headers=headers)
    assert r.status_code == 404

def test_tenant_isolation(client):
    h1 = {"X-Tenant-ID": "t1"}
    h2 = {"X-Tenant-ID": "t2"}

    r1 = client.post("/customers", json={"name": "C1", "email": "c1@t1.com"}, headers=h1)
    r2 = client.post("/customers", json={"name": "C2", "email": "c2@t2.com"}, headers=h2)

    assert r1.status_code == 201
    assert r2.status_code == 201

    id1 = r1.json()["id"]
    id2 = r2.json()["id"]
    assert id1 != id2  # ids são globais no banco

    list1 = client.get("/customers", headers=h1).json()
    list2 = client.get("/customers", headers=h2).json()

    assert len(list1) == 1
    assert len(list2) == 1
    assert list1[0]["email"] == "c1@t1.com"
    assert list2[0]["email"] == "c2@t2.com"

