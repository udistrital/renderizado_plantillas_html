from flask import Flask
from controllers.pdfController import pdf_blueprint
from swagger.swagger_config import configure_swagger
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configura Swagger
configure_swagger(app)

app.register_blueprint(pdf_blueprint)

if __name__ == '__main__':
    # Lee el puerto desde una variable de entorno
    port_str = os.getenv('PORT')
    
    if port_str is None:
        raise EnvironmentError("La variable de entorno PORT no está configurada.")
    
    try:
        port = int(port_str)
    except ValueError:
        raise ValueError(f"La variable de entorno PORT '{port_str}' no es un número válido.")
    
    # Inicia la aplicación en el puerto configurado
    app.run(host='0.0.0.0', port=port, debug=True)