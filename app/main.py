from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi

from app.core.config import settings
from app.core.tenant import get_tenant_id
from app.customers.router import router as customers_router
from app.tenants.router import router as tenants_router

API_PREFIX = "/api/v1"

tags_metadata = [
    {"name": "customers", "description": "CRUD de clientes"},
    {"name": "tenants", "description": "Gestão de tenants (admin)"},
    {"name": "default", "description": "Utilitários"},
]

app = FastAPI(
    title=settings.app_name,
    version="0.2.0",
    openapi_tags=tags_metadata,
    swagger_ui_parameters={"persistAuthorization": True},
)

# tudo sob /api/v1
app.include_router(customers_router, prefix=API_PREFIX)
app.include_router(tenants_router, prefix=API_PREFIX)


@app.get(f"{API_PREFIX}/whoami", tags=["default"])
def whoami(tenant_id: str = Depends(get_tenant_id)):
    return {"tenant_id": tenant_id}


@app.get("/health", tags=["default"])
def health():
    return {"status": "ok", "env": settings.env}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="API B2B SaaS multi-tenant com autenticação via API Key.",
        routes=app.routes,
    )

    openapi_schema.setdefault("components", {}).setdefault("securitySchemes", {})
    openapi_schema["components"]["securitySchemes"]["ApiKeyAuth"] = {
        "type": "apiKey",
        "in": "header",
        "name": "X-API-Key",
    }

    # aplica autenticação por padrão (exceto endpoints que você decidir liberar)
    openapi_schema["security"] = [{"ApiKeyAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi