## Especificaciones Técnicas

### Tecnologías Implementadas y Versiones
* [Python 3.12.4](https://github.com/udistrital/lineamientos_oas/blob/master/api_flask/lineamientos_previos.md)
* [Flask 3.0.3](https://flask.palletsprojects.com/es/main/)
* [Weasyprint 62.3](https://doc.courtbouillon.org/weasyprint/stable/)
* [JINJA2 3.1.4](https://jinja.palletsprojects.com/en/3.1.x/)
* [docker](https://docs.docker.com/engine/install/ubuntu/)


### Variables de Entorno

RENDERIZADO_HTML_PORT=[puerto de ejecucion]

### Ejecución del Proyecto
```shel

# 1. Obtener el repositorio con Go
go get github.com/udistrital/renderizado_plantillas_html

# 2. Moverse a la carpeta del repositorio
cd $GOPATH/src/github.com/udistrital/renderizado_plantillas_html

# 3. Moverse a la rama **develop**
git pull origin develop && git checkout develop

# 4. alimentar todas las variables de entorno que utiliza el proyecto.

# 5. ejecutar el proyecto
python app.py
```
## Estado CI

| Develop | Relese 0.0.1 | Master |
| -- | -- | -- |
| [![Build Status](https://hubci.portaloas.udistrital.edu.co/api/badges/udistrital/renderizado_plantillas_html/status.svg?ref=refs/heads/develop)](https://hubci.portaloas.udistrital.edu.co/udistrital/renderizado_plantillas_html/) | [![Build Status](https://hubci.portaloas.udistrital.edu.co/api/badges/udistrital/renderizado_plantillas_html/status.svg?ref=refs/heads/release/0.0.1)](https://hubci.portaloas.udistrital.edu.co/udistrital/renderizado_plantillas_html/) | [![Build Status](https://hubci.portaloas.udistrital.edu.co/api/badges/udistrital/renderizado_plantillas_html/status.svg)](https://hubci.portaloas.udistrital.edu.co/udistrital/renderizado_plantillas_html/) |

## Modelo de Datos

No cuenta con modelo de datos

## Licencia

This file is part of historico_usuarios_roles_crud.

inscripcion_crud is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

inscripcion_crud is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with novedades_crud. If not, see https://www.gnu.org/licenses/.