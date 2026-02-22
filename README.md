![CI](https://github.com/Arquiron/fastapi-b2b-saas-api/actions/workflows/ci.yml/badge.svg)

# 🚀 FastAPI B2B SaaS API (Multi-Tenant)

API REST desenvolvida com **FastAPI**, utilizando arquitetura **multi-tenant** com autenticação via **API Key**.

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

- `POST /customers` – Criar cliente
- `GET /customers` – Listar clientes
- `GET /customers/{customer_id}` – Buscar cliente
- `DELETE /customers/{customer_id}` – Remover cliente

### 🔎 Utilitários

- `GET /health` – Health check
- `GET /whoami` – Retorna o tenant autenticado

---

## 🔐 Autenticação

Todas as requisições protegidas exigem o header:

```http
X-API-Key: <sua_api_key>
