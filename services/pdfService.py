from jinja2 import Template
from weasyprint import HTML, CSS


def renderizar_pdf(plantillaHTML, css=None, context={}):
    # htmlRenderizado = plantilla.render(context)
    htmlRenderizado = renderizar_html(plantillaHTML, context)

    # Renderizar el HTML y generar el PDF
    if css:
        css_obj = CSS(string=css)
        pdf= HTML(string=htmlRenderizado).write_pdf(stylesheets=[css_obj])
    else:
        pdf=HTML(string=htmlRenderizado).write_pdf()
    return pdf

def renderizar_html(plantillaHTML, context={}):
    # Convertir la cadena HTML en una plantilla Jinja2
    plantilla = Template(plantillaHTML)

    # Renderizar el HTML con el contexto
    return  plantilla.render(context)
