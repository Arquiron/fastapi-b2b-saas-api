from pydantic import BaseModel, Field


class TenantCreate(BaseModel):
    tenant_id: str = Field(..., min_length=2, max_length=80, examples=["acme"])
    name: str = Field(..., min_length=2, max_length=120, examples=["ACME Ltda"])


class TenantCreated(BaseModel):
    tenant_id: str
    name: str
    api_key: str 