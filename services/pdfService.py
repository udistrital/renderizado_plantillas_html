from jinja2 import Template
from weasyprint import HTML, CSS
import io


def renderizar_pdf(html_template_str, css=None, context={}):
   # Convertir la cadena HTML en una plantilla Jinja2
    template = Template(html_template_str)

    # Renderizar el HTML con el contexto
    html_rendered = template.render(context)

    # Crear un objeto BytesIO para el PDF
    pdf_file = io.BytesIO()

    # Renderizar el HTML y generar el PDF
    if css:
        css_obj = CSS(string=css)
        HTML(string=html_rendered).write_pdf(target=pdf_file, stylesheets=[css_obj])
    else:
        HTML(string=html_rendered).write_pdf(target=pdf_file)

    # Mover el puntero al inicio del archivo en memoria
    pdf_file.seek(0)

    return pdf_file