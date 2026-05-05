from flask import Blueprint, request, jsonify
from services.docxService import renderizar_docx
import base64

docx_blueprint = Blueprint("generar-docx", __name__)

@docx_blueprint.route("/generar-docx", methods=["POST"])
def generar_docx():
    """
    Genera un DOCX a partir de un HTML.
    ---
    tags:
      - DOCX Generation
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - html
          properties:
            css:
              type: string
              description: Optional CSS string.
            data:
              type: object
              description: Optional data for Jinja2 templating.
            html:
              type: string
              description: The HTML template string.
    responses:
      200:
        description: DOCX generated successfully
        schema:
          type: object
          properties:
            Data:
              type: string
              description: Base64 encoded DOCX string
            Message:
              type: string
            Status:
              type: integer
            Success:
              type: boolean
      500:
        description: Error generating DOCX
        schema:
          type: object
          properties:
            Message:
              type: string
            Status:
              type: integer
            Success:
              type: boolean
    """
    try:
        data = request.json
        plantilla_html = data.get("html")
        css = data.get("css", None)  # CSS es opcional
        datos = data.get("data", {})

        if not plantilla_html:
            raise ValueError("La plantilla HTML es requerida.")

        docx_file = renderizar_docx(plantilla_html, css, datos)

        # Convertir el DOCX a base64
        docx_base64 = base64.b64encode(docx_file).decode("utf-8")

        # Crear una respuesta JSON con el DOCX en base64
        response_data = {
            "Data": docx_base64,
            "Message": "DOCX generado exitosamente",
            "Status": 200,
            "Success": True,
        }
        return jsonify(response_data)
    except Exception as e:
        print(f"Error: {e}")
        error_response = {
            "Message": f"Ha ocurrido un error: {str(e)}",
            "Status": 500,
            "Success": False,
        }
        return jsonify(error_response), 500