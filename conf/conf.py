import os
from dotenv import load_dotenv

class Config:
    # Carga las variables de entorno desde el archivo .env
    load_dotenv() 

    RENDERIZADO_HTML_PORT = os.getenv('RENDERIZADO_HTML_PORT')

config = Config()