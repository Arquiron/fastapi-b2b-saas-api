from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "B2B API"
    env: str = "dev"
    api_key_pepper: str = "ci-pepper"
    database_url: str = "sqlite:///./app.db"
    admin_api_key: Optional[str] = None  # trocar para admin_api_key: str quando estiver em produção
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
