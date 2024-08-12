from flask import Blueprint, request, jsonify
from services.pdfService import renderizar_pdf
import base64

pdf_blueprint = Blueprint('pdf', __name__)

@pdf_blueprint.route('/pdf', methods=['POST'])
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
            html:
              type: string
              description: The HTML template string.
            css:
              type: string
              description: Optional CSS string.
            datos:
              type: object
              description: Optional datos for Jinja2 templating.
    responses:
      200:
        description: PDF generated successfully
        schema:
          type: object
          properties:
            Message:
              type: string
            Success:
              type: boolean
            Status:
              type: integer
            PDF:
              type: string
              description: Base64 encoded PDF string
      500:
        description: Error generating PDF
        schema:
          type: object
          properties:
            Message:
              type: string
            Success:
              type: boolean
            Status:
              type: integer
    """
    try:
        data = request.json
        plantilla_html = data.get('html')
        css = data.get('css', None)  # CSS es opcional
        datos = data.get('data', {})
        
        if not plantilla_html:
            raise ValueError("La plantilla HTML es requerida.")
        
        pdf_file = renderizar_pdf(plantilla_html, css, datos)

        # Convertir el PDF a base64
        pdf_base64 = base64.b64encode(pdf_file).decode('utf-8')
        
        # Crear una respuesta JSON con el PDF en base64
        response_data = {
            "Message": "PDF generado exitosamente",
            "Success": True,
            "Status": 200,
            "Data": pdf_base64
        }
        return jsonify(response_data)

    except Exception as e:
        print(f"Error: {e}")
        error_response = {
            "Message": f"Ha ocurrido un error: {str(e)}",
            "Success": False,
            "Status": 500
        }
        return jsonify(error_response), 500