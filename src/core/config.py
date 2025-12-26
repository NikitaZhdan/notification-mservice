from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    POSTGRES_URL: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    KEY_TTL: int

    QUEUE_NAME: str

    RABBIT_URL: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
    )

settings = Settings()
