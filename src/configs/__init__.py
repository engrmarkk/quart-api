from src.constants import SECRET_KEY
from datetime import datetime, timedelta


class Config:
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = True
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = True
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


config = {"dev": DevConfig, "prod": ProdConfig}
