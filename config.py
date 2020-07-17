import os


class Config(object):
    CATEGORIES_PATH = "app/categories.json"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PW")}@localhost:5432/{os.environ.get("POSTGRES_DB")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    BASE_URL = "https://www.example.com"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevelopmentConfig(Config):
    BASE_URL = "http://localhost:5000"
    DEVELOPMENT = True
    DEBUG = True
