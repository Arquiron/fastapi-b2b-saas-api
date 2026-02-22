from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Tenant(Base):
    __tablename__ = "tenants"

    __table_args__ = (
        UniqueConstraint("tenant_id", name="uq_tenant_id"),
        UniqueConstraint("api_key_hash", name="uq_api_key_hash"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tenant_id: Mapped[str] = mapped_column(String(80), index=True)
    name: Mapped[str] = mapped_column(String(120))
    api_key_hash: Mapped[str] = mapped_column(String(120))
