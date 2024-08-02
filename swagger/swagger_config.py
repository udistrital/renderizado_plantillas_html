from flasgger import Swagger

def configure_swagger(app):
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'swagger',
                "route": '/swagger.json',
                "rule_filter": lambda rule: True,  # include all routes
                "model_filter": lambda tag: True,  # include all models
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "swagger_ui_url": "/swagger",
        "specs_route": "/swagger"
    }

    Swagger(app, config=swagger_config)