from pydantic import BaseSettings
import os

DB_ENGINE = os.environ.get('DB_ENGINE')
DB_NAME = os.environ.get('DB_NAME')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')


class Settings(BaseSettings):
    db_url: str = (f"{DB_ENGINE}://{POSTGRES_USER}:"
                   f"{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")


settings = Settings()
