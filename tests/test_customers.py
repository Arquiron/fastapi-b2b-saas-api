def test_whoami_requires_api_key(client):
    r = client.get("/whoami")
    assert r.status_code == 401


def test_customers_crud(client, tenant_api_key):
    headers = {
        "X-API-Key": tenant_api_key
    }

    # create
    r = client.post(
        "/customers",
        json={"name": "ACME Buyer", "email": "buyer@acme.com"},
        headers=headers
    )
    assert r.status_code == 201
    created = r.json()
    assert created["id"] == 1

    # list
    r = client.get("/customers", headers=headers)
    assert r.status_code == 200
    assert len(r.json()) == 1

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