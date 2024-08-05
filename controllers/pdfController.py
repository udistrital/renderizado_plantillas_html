from flask import Blueprint, request, jsonify
from services.pdfService import renderizar_pdf
import base64

pdf_blueprint = Blueprint('pdf', __name__)

@pdf_blueprint.route('/generarpdf', methods=['POST'])
def generate_pdf():
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
            context:
              type: object
              description: Optional context for Jinja2 templating.
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
        html_template = data.get('html')
        css = data.get('css', None)  # CSS es opcional
        context = data.get('context', {})
        
        if not html_template:
            raise ValueError("La plantilla HTML es requerida.")
        
        pdf_file = renderizar_pdf(html_template, css, context)

        # Leer el contenido del archivo PDF
        pdf_content = pdf_file.read()
        
        # Convertir el PDF a base64
        pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')
        
        # Crear una respuesta JSON con el PDF en base64
        response_data = {
            "Message": "PDF generado exitosamente",
            "Success": True,
            "Status": 200,
            "Data": pdf_base64
        }

        return jsonify(response_data)

    except Exception as e:
        # Log the error (optional)
        print(f"Error: {e}")

        # Create an error response
        error_response = {
            "Message": f"Ha ocurrido un error: {str(e)}",
            "Success": False,
            "Status": 500
        }
        return jsonify(error_response), 500