import ipaddress
import socket
from urllib.parse import urlsplit

from weasyprint import URLFetcher

# Protocolos permitidos al resolver los recursos externos de una plantilla.
# Se excluyen file:// y ftp:// para impedir la lectura de archivos del contenedor.
PROTOCOLOS_PERMITIDOS = ("http", "https", "data")

PUERTOS_POR_DEFECTO = {"http": 80, "https": 443}


class FetcherSeguro(URLFetcher):
    """URLFetcher que restringe los recursos externos de las plantillas.

    Las plantillas llegan por la API, así que su contenido no es confiable.
    Este fetcher bloquea los protocolos distintos de HTTP(S) y las direcciones
    que no son públicas, evitando que un HTML malicioso alcance servicios de la
    red interna o el endpoint de metadatos del proveedor de nube (SSRF).
    """

    def __init__(self, **kwargs):
        kwargs.setdefault("allowed_protocols", PROTOCOLOS_PERMITIDOS)
        # Sin redirecciones: una URL pública podría redirigir a una interna.
        kwargs.setdefault("allow_redirects", False)
        super().__init__(**kwargs)

    def fetch(self, url, headers=None):
        self._validar_destino(url)
        return super().fetch(url, headers)

    @staticmethod
    def _validar_destino(url):
        partes = urlsplit(url)
        scheme = partes.scheme.lower()

        # Las data: URI no salen a la red; los demás protocolos los filtra
        # allowed_protocols en la clase base.
        if scheme not in PUERTOS_POR_DEFECTO:
            return

        host = partes.hostname
        if not host:
            raise ValueError(f"URI sin host: {url}")

        puerto = partes.port or PUERTOS_POR_DEFECTO[scheme]
        try:
            resueltas = socket.getaddrinfo(host, puerto, proto=socket.IPPROTO_TCP)
        except socket.gaierror as error:
            raise ValueError(f"No se pudo resolver el host: {host}") from error

        # Se revisan todas las IP resueltas: basta con que una sea interna
        # para descartar el recurso.
        for info in resueltas:
            ip = ipaddress.ip_address(info[4][0])
            if not ip.is_global or ip.is_reserved:
                raise ValueError(f"URI apunta a una dirección no pública: {url}")
