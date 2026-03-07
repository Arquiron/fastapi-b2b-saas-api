![CI](https://github.com/Arquiron/fastapi-b2b-saas-api/actions/workflows/ci.yml/badge.svg)

# 🚀 FastAPI B2B SaaS API (Multi-Tenant)

Production-style FastAPI backend implementing a multi-tenant B2B SaaS architecture with API Key authentication, tenant isolation, automated tests and CI pipeline.

Projeto estruturado com separação de responsabilidades (core, db, tenants, customers) e preparado para evoluir como produto SaaS real.

---

## 🏗 Arquitetura

- 🔐 Autenticação via **X-API-Key**
- 🏢 Isolamento por **Tenant**
- 🧱 Estrutura modular organizada por domínio
- 📄 Documentação automática via Swagger (OpenAPI)
- 🧪 Testes automatizados com Pytest
- 🗄 SQLite (dev) – preparado para migração futura para PostgreSQL

---

## 📌 Endpoints

### 👤 Customers

- `POST /api/v1/customers` – Criar cliente
- `GET /api/v1/customers` – Listar clientes
- `GET /api/v1/customers/{customer_id}` – Buscar cliente
- `DELETE /api/v1/customers/{customer_id}` – Remover cliente

### 🏢 Tenants (Admin)

POST /api/v1/tenants – Criar tenant

### 🔎 Utilitários

- `GET /health` – Health check
- `GET /whoami` – Retorna o tenant autenticado

---

## Run locally

```bash
git clone https://github.com/Arquiron/fastapi-b2b-saas-api
cd fastapi-b2b-saas-api

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python create_tables.py

uvicorn app.main:app --reload
```

Swagger UI:
http://localhost:8000/docs

## 🔐 Autenticação
