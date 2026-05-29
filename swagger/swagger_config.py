import logging

logger = logging.getLogger(__name__)


def configure_swagger(app):
    if not app.debug:
        return
    try:
        from flasgger import Swagger

        app.config["SWAGGER"] = {
            "title": "PDF and Docx Generation API",
            "description": "API para la generación de PDFs a partir de plantillas HTML.",
            "version": "1.0.0",
            "termsOfService": "",
            "uiversion": 3
        }

        swagger_config = {
            "headers": [],
            "specs": [
                {
                    "endpoint": "swagger",
                    "route": "/swagger.json",
                    "rule_filter": lambda rule: True,  # include all routes
                    "model_filter": lambda tag: True,  # include all models
                }
            ],
            "static_url_path": "/flasgger_static",
            "swagger_ui": True,
            "swagger_ui_url": "/swagger",
            "specs_route": "/swagger",
            "cache_timeout": 0
        }

        Swagger(app, config=swagger_config)
    except ImportError:
        logger.warning(
            "Flasgger is not installed in this environment. Ensure uv add flasgger --dev was used for development."
        )
