from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "B2B API"
    env: str = "dev"
    api_key_pepper: str

    class Config:
        env_file = ".env"

settings = Settings()
