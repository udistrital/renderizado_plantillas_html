import logging

logger = logging.getLogger(__name__)


def configure_swagger(app):
    if not app.debug:
        return
    try:
        from flasgger import Swagger

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
        }

        Swagger(app, config=swagger_config)
    except ImportError:
        logger.warning(
            "Flasgger is not installed in this environment. Ensure 'uv add flasgger --dev' was used for development."
        )
