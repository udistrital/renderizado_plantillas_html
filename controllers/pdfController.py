from flask import Blueprint, request, jsonify
from services.pdfService import renderizar_pdf
from services.pdfService import renderizar_html
import base64

pdf_blueprint = Blueprint("generar-pdf", __name__)


@pdf_blueprint.route("/generar-pdf", methods=["POST"])
def generar_pdf():
    """
    Genera un PDF a partir de un HTML.
    ---
    tags:
      - PDF Generation
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
        description: PDF generated successfully
        schema:
          type: object
          properties:
            Data:
              type: string
              description: Base64 encoded PDF string
            Message:
              type: string
            Status:
              type: integer
            Success:
              type: boolean
      500:
        description: Error generating PDF
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

        pdf_file = renderizar_pdf(plantilla_html, css, datos)

        # Convertir el PDF a base64
        pdf_base64 = base64.b64encode(pdf_file).decode("utf-8")

        # Crear una respuesta JSON con el PDF en base64
        response_data = {
            "Data": pdf_base64,
            "Message": "PDF generado exitosamente",
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


@pdf_blueprint.route("/generar-html", methods=["POST"])
def generar_html():
    """
    Genera un HTML a partir de un HTML.
    ---
    tags:
      - HTML Generation
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - html
          properties:
            datos:
              type: object
              description: Optional data for Jinja2 templating.
            html:
              type: string
              description: The HTML template string.
    responses:
      200:
        description: HTML generated successfully
        schema:
          type: object
          properties:
            Data:
              type: string
              description: Rendered HTML with variables replaced
            Message:
              type: string
            Status:
              type: integer
            Success:
              type: boolean
      500:
        description: Error generating HTML
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
        datos = data.get("datos", {})

        if not plantilla_html:
            raise ValueError("La plantilla HTML es requerida.")

        rendered_html = renderizar_html(plantilla_html, datos)

        response_data = {
            "Data": rendered_html,
            "Message": "HTML generado exitosamente",
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
