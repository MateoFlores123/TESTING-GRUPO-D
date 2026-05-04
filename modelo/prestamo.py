import re
from datetime import datetime

class Prestamo:
    def __init__(self, id_prestamo: int, isbn: str, usuario: str,
                 fecha_prestamo: str, fecha_devolucion_prevista: str, devuelto: bool = False):
        if not isinstance(id_prestamo, int) or id_prestamo <= 0:
            raise ValueError("ID de préstamo inválido")
        if not isbn or not isbn.strip():
            raise ValueError("ISBN inválido")
        if not usuario or len(usuario.strip()) < 3:
            raise ValueError("El usuario debe tener al menos 3 caracteres")
        patron_fecha = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        if not patron_fecha.match(fecha_prestamo) or not patron_fecha.match(fecha_devolucion_prevista):
            raise ValueError("Formato de fecha incorrecto (YYYY-MM-DD)")

        self.id_prestamo = id_prestamo
        self.isbn = isbn.strip()
        self.usuario = usuario.strip()
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion_prevista = fecha_devolucion_prevista
        self.devuelto = devuelto

    def to_dict(self):
        return {
            "id_prestamo": self.id_prestamo,
            "isbn": self.isbn,
            "usuario": self.usuario,
            "fecha_prestamo": self.fecha_prestamo,
            "fecha_devolucion_prevista": self.fecha_devolucion_prevista,
            "devuelto": self.devuelto
        }

    @staticmethod
    def from_dict(data):
        return Prestamo(data["id_prestamo"], data["isbn"], data["usuario"],
                        data["fecha_prestamo"], data["fecha_devolucion_prevista"], data["devuelto"])