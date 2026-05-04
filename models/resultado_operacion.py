"""
models/resultado_operacion.py
------------------------------
Clase que encapsula el resultado de cualquier operación del sistema.
Todas las funciones del Catálogo retornan este objeto.
"""


class ResultadoOperacion:
    """
    Encapsula el resultado de una operación de negocio.

    Atributos:
        exito   (bool) : True si la operación fue exitosa.
        mensaje (str)  : Mensaje descriptivo del resultado o error.
        datos   (any)  : Datos retornados (Libro, list[Libro], None).
    """

    def __init__(self, exito: bool, mensaje: str, datos=None):
        self._exito   = exito
        self._mensaje = mensaje
        self._datos   = datos

    # Getters
    def es_exitoso(self) -> bool:
        return self._exito

    def get_mensaje(self) -> str:
        return self._mensaje

    def get_datos(self):
        return self._datos

    def __repr__(self) -> str:
        return f"ResultadoOperacion(exito={self._exito}, mensaje='{self._mensaje}')"