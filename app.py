from flask import Flask, jsonify
from controllers.pdfController import pdf_blueprint
from swagger.swagger_config import configure_swagger
from conf.conf import config



app = Flask(__name__)

# Configura Swagger
configure_swagger(app)

app.register_blueprint(pdf_blueprint)

@app.route('/', methods=['GET'])
def health_check():
    health_status = {
        "status": "ok",
        "message": "El servicio está funcionando correctamente"
    }
    return jsonify(health_status), 200

@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "Error": str(e)
    }
    return jsonify(response), 500

if __name__ == '__main__':
    port_str = config.RENDERIZADO_HTML_PORT
    app.run(host='0.0.0.0', port=port_str, debug=True)