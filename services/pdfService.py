from jinja2 import Template
from weasyprint import HTML, CSS


def renderizar_pdf(plantillaHTML, css=None, context={}):
    # htmlRenderizado = plantilla.render(context)
    htmlRenderizado = renderizar_html(plantillaHTML, context)

    # Renderizar el HTML y generar el PDF
    if css:
        css_obj = CSS(string=css)
        pdf = HTML(string=htmlRenderizado).write_pdf(stylesheets=[css_obj])
    else:
        pdf = HTML(string=htmlRenderizado).write_pdf()
    return pdf


def renderizar_html(plantillaHTML, context={}):
    # Convertir la cadena HTML en una plantilla Jinja2
    plantilla = Template(plantillaHTML)

    # Renderizar el HTML con el contexto
    html_final = plantilla.render(context)

    # --- LIMPIEZA DE NON-BREAKING SPACES ---
    # Reemplaza la entidad de texto '&nbsp;' por un espacio común
    html_saneado = html_final.replace("&nbsp;", " ")
    
    # Reemplaza el carácter Unicode invisible No-Break Space (\xa0) por un espacio común
    html_saneado = html_saneado.replace("\xa0", " ")
    # ----------------------------------------

    return html_saneado
