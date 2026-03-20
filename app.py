import logging
from flask import Flask, jsonify
from controllers.pdfController import pdf_blueprint
from conf.conf import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    if app.debug:
        from swagger.swagger_config import configure_swagger
        configure_swagger(app)

    app.register_blueprint(pdf_blueprint)

    @app.route("/", methods=["GET"])
    def health_check():
        health_status = {"status": "ok", "message": "Renderizado Plantillas HTML OK"}
        return jsonify(health_status), 200

    @app.errorhandler(Exception)
    def handle_exception(e):
        response = {"Error": str(e)}
        return jsonify(response), 500

    return app


app = create_app()

if __name__ == "__main__":
    try:
        port = int(config.RENDERIZADO_HTML_PORT)
    except (ValueError, TypeError):
        port = 8080
        logger.warning(f"Invalid port in config. Using default: {port}")

    app.run(host="0.0.0.0", port=port)
