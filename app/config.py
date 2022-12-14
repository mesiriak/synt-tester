from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_URL: str = "postgresql+psycopg2://postgres:postgrespw@0.0.0.0:9876/postgres"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
