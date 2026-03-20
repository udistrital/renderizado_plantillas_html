import os


class Config:
    RENDERIZADO_HTML_PORT = int(os.getenv("RENDERIZADO_HTML_PORT", 8080))
    ENV = os.getenv("ENV", "production")
    DEBUG = ENV == "dev" or ENV == "development"


config = Config()
