![CI](https://github.com/Arquiron/fastapi-b2b-saas-api/actions/workflows/ci.yml/badge.svg)

# B2B API (FastAPI) — Multi-tenant

API FastAPI focada em produto B2B: multi-tenant via header `X-Tenant-ID`, CRUD de clientes e testes automatizados.

## Stack
- FastAPI
- SQLAlchemy (SQLite)
- Pytest

## Rodar local
```bash
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
