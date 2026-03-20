# Renderizado plantillas HTML

 Servicio encargado de la generación de documentos PDF a partir de plantillas HTML y un objeto JSON con los datos a reemplazar utilizando el motor de renderizado WeasyPrint y Jinja2.


## Especificaciones Técnicas

### Tecnologías Implementadas y Versiones
* [Python 3.12 - Gestionado con uv](https://docs.astral.sh/uv/)
* [Flask 3.1.3](https://flask.palletsprojects.com/en/stable/)
* [Weasyprint 68.1](https://doc.courtbouillon.org/weasyprint/stable/)
* [JINJA2 3.1.6](https://jinja.palletsprojects.com/en/stable/)
* [Flasgger (Swagger UI)](https://github.com/flasgger/flasgger)
* [Gunicorn](https://gunicorn.org/)
* [Docker](https://docs.docker.com/engine/install/ubuntu/)


### Variables de Entorno

RENDERIZADO_HTML_PORT=[Puerto de ejecución del servicio]
ENV=[Entorno de ejecución (dev activa Swagger)]

### Ejecución del Proyecto (local con uv)
```bash
# 1. Clonar el repositorio
git clone https://github.com/udistrital/renderizado_plantillas_html
cd renderizado_plantillas_html

# 2. Instalar dependencias (incluyendo desarrollo)
uv sync

# 3. Configurar variables de entorno (Linux/macOS)
export ENV=dev
export RENDERIZADO_HTML_PORT=8080

# 4.1. Ejecutar en modo desarrollo
uv run flask run --debug --port 8080
```

### Ejecución del Proyecto (local con uv)
```bash
# 1. Construir la imagen
docker build -t renderizado-html-pdf .

# 2. Ejecutar el contenedor
docker run -p 8080:8080 \
  -e ENV=dev \
  -e RENDERIZADO_HTML_PORT=8080 \
  renderizado-html-pdf
```

### Estilo de Código y Calidad

Se utiliza Ruff para el formateo y linting del código.

```bash
# Revisar errores de estilo
uv run ruff check .
# Formatear automáticamente
uv run ruff format .
```

## Estado CI

| Develop | Relese 0.0.1 | Master |
| -- | -- | -- |
| [![Build Status](https://hubci.portaloas.udistrital.edu.co/api/badges/udistrital/renderizado_plantillas_html/status.svg?ref=refs/heads/develop)](https://hubci.portaloas.udistrital.edu.co/udistrital/renderizado_plantillas_html/) | [![Build Status](https://hubci.portaloas.udistrital.edu.co/api/badges/udistrital/renderizado_plantillas_html/status.svg?ref=refs/heads/release/0.0.1)](https://hubci.portaloas.udistrital.edu.co/udistrital/renderizado_plantillas_html/) | [![Build Status](https://hubci.portaloas.udistrital.edu.co/api/badges/udistrital/renderizado_plantillas_html/status.svg)](https://hubci.portaloas.udistrital.edu.co/udistrital/renderizado_plantillas_html/) |

## Modelo de Datos

No aplica

## Licencia

This file is part of historico_usuarios_roles_crud.

inscripcion_crud is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

inscripcion_crud is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with novedades_crud. If not, see https://www.gnu.org/licenses/.