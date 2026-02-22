from fastapi import Depends, FastAPI
from app.core.config import settings
from app.core.tenant import get_tenant_id
from app.customers.router import router as customers_router
from fastapi.openapi.utils import get_openapi

tags_metadata = [
    {"name": "customers", "description": "CRUD de clientes"},
    {"name": "default", "description": "Utilitários"},
]

app = FastAPI(
    title=settings.app_name,
    version="0.2.0",
    openapi_tags=tags_metadata,
    swagger_ui_parameters={"persistAuthorization": True},
)

app.include_router(customers_router)

@app.get("/health")
def health():
    return {"status": "ok", "env": settings.env}

@app.get("/whoami")
def whoami(tenant_id: str = Depends(get_tenant_id)):
    return {"tenant_id": tenant_id}

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

    # aplica globalmente (o Swagger passa a enviar o header em tudo após Authorize)
    openapi_schema["security"] = [{"ApiKeyAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi