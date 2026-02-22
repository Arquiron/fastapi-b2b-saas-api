![CI](https://github.com/Arquiron/fastapi-b2b-saas-api/actions/workflows/ci.yml/badge.svg)

# 🚀 FastAPI B2B SaaS API (Multi-Tenant)

API REST construída com FastAPI focada em arquitetura B2B SaaS multi-tenant com autenticação via API Key.

Projeto estruturado com separação de camadas (core, db, tenants, customers) e preparado para evolução como produto real.

---

## 🏗 Arquitetura

- 🔐 Autenticação por **API Key**
- 🏢 Isolamento por **Tenant**
- 🧱 Estrutura modular
- 📄 Documentação automática via Swagger
- 🧪 Testes automatizados com Pytest
- 🗄 Banco SQLite (dev) — preparado para migração futura

---

## 📌 Funcionalidades

### 👤 Customers
- `POST /customers`
- `GET /customers`
- `GET /customers/{customer_id}`
- `DELETE /customers/{customer_id}`

### 🔎 Utilitários
- `GET /health`
- `GET /whoami`

---

## 🔐 Autenticação

A API utiliza autenticação via header:

