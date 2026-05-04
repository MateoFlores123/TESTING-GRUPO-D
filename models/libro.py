# models/libro.py

class Libro:
    def __init__(self, codigo, titulo, autor, categoria, anio_publicacion, cantidad_total):
        self._codigo             = codigo
        self._titulo             = titulo
        self._autor              = autor
        self._categoria          = categoria
        self._anio_publicacion   = anio_publicacion
        self._cantidad_total     = cantidad_total
        self._cantidad_disponible = cantidad_total

    def get_codigo(self):            return self._codigo
    def get_titulo(self):            return self._titulo
    def get_autor(self):             return self._autor
    def get_categoria(self):         return self._categoria
    def get_anio_publicacion(self):  return self._anio_publicacion
    def get_cantidad_total(self):    return self._cantidad_total
    def get_cantidad_disponible(self): return self._cantidad_disponible

    def esta_disponible(self):
        return self._cantidad_disponible > 0

    def get_estado(self):
        return "Disponible" if self.esta_disponible() else "No disponible"

    def reducir_disponibilidad(self):
        if self._cantidad_disponible > 0:
            self._cantidad_disponible -= 1
            return True
        return False

    def aumentar_disponibilidad(self):
        if self._cantidad_disponible < self._cantidad_total:
            self._cantidad_disponible += 1
            return True
        return False