import os
from pathlib import Path

BASE_DIR = Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', f"sqlite:///{BASE_DIR / 'main.db'}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SQLALCHEMY_ECHO = False
    DEBUG = os.environ.get("FLASK_DEBUG", True)
    PORT = 5000
    SECRET_KEY = "My secret key =)"
    RESTFUL_JSON = {
        'ensure_ascii': False,
    }
    UPLOAD_FOLDER_NAME = 'upload'
    UPLOAD_FOLDER = BASE_DIR / UPLOAD_FOLDER_NAME
    LANGUAGES = ['en', 'ru']
