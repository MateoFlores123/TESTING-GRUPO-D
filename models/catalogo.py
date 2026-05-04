# models/catalogo.py

from models.libro import Libro


class Catalogo:
    def __init__(self):
        self._libros = {}   # { codigo: Libro }

    # ------------------------------------------------------------------
    # RF-01 — Registrar Libro
    # ------------------------------------------------------------------
    def registrar_libro(self, codigo, titulo, autor, categoria, anio, cantidad):
        # Validar campos obligatorios
        for valor in [codigo, titulo, autor, categoria, anio, cantidad]:
            if valor is None or str(valor).strip() == "":
                return False, "Todos los campos son obligatorios."

        codigo = str(codigo).strip().upper()

        if codigo in self._libros:
            return False, "Ya existe un libro registrado con ese código."

        try:
            anio = int(anio)
        except (ValueError, TypeError):
            return False, "El año de publicación debe ser un número válido."

        try:
            cantidad = int(cantidad)
        except (ValueError, TypeError):
            return False, "La cantidad debe ser un número entero válido."

        if cantidad < 1:
            return False, "La cantidad debe ser mayor a cero."

        libro = Libro(codigo, str(titulo).strip(), str(autor).strip(),
                      str(categoria).strip(), anio, cantidad)
        self._libros[codigo] = libro
        return True, libro

    # ------------------------------------------------------------------
    # RF-02 — Buscar Libro
    # ------------------------------------------------------------------
    def buscar_libro(self, criterio):
        if criterio is None or str(criterio).strip() == "":
            return False, "Ingrese un criterio de búsqueda."

        c = str(criterio).strip().lower()
        resultados = [
            libro for libro in self._libros.values()
            if c in libro.get_codigo().lower()
            or c in libro.get_titulo().lower()
            or c in libro.get_autor().lower()
        ]

        if not resultados:
            return False, "No se encontraron libros con ese criterio."

        return True, resultados

    # ------------------------------------------------------------------
    # RF-03 — Mostrar Disponibilidad
    # ------------------------------------------------------------------
    def mostrar_disponibilidad(self, criterio):
        if criterio is None or str(criterio).strip() == "":
            return False, "Ingrese un código o título para consultar."

        c = str(criterio).strip().lower()
        for libro in self._libros.values():
            if c == libro.get_codigo().lower() or c in libro.get_titulo().lower():
                return True, libro

        return False, "No se encontró ningún libro con ese criterio."

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------
    def listar_todos(self):
        return list(self._libros.values())

    def total(self):
        return len(self._libros)