import secrets
from app.db.session import SessionLocal
from app.tenants.db_model import Tenant
from app.core.security import hash_api_key

def main():
    db = SessionLocal()
    try:
        tenant_id = "acme"
        name = "ACME Ltd"

        api_key = secrets.token_urlsafe(32)
        api_key_hash = hash_api_key(api_key)

        t = Tenant(tenant_id=tenant_id, name=name, api_key_hash=api_key_hash)
        db.add(t)
        db.commit()

        print("Tenant criado!")
        print("tenant_id:", tenant_id)
        print("api_key (SALVE AGORA):", api_key)
    finally:
        db.close()

if __name__ == "__main__":
    main()
