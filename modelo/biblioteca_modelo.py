import json
import os
from datetime import datetime, timedelta
from .libro import Libro
from .prestamo import Prestamo

class BibliotecaModelo:
    def __init__(self, ruta_datos="datos"):
        self.ruta_datos = ruta_datos
        self.libros = {}
        self.prestamos = []
        self.contador_prestamos = 1
        self._inicializar_archivos()
        self._cargar_datos()
        self._cargar_datos_prueba_si_vacio()

    def _inicializar_archivos(self):
        os.makedirs(self.ruta_datos, exist_ok=True)
        self.ruta_libros = os.path.join(self.ruta_datos, "libros.json")
        self.ruta_prestamos = os.path.join(self.ruta_datos, "prestamos.json")

    def _cargar_datos(self):
        if os.path.exists(self.ruta_libros):
            with open(self.ruta_libros, "r", encoding="utf-8") as f:
                data = json.load(f)
                for isbn, lib_data in data.items():
                    try:
                        self.libros[isbn] = Libro.from_dict(lib_data)
                    except ValueError:
                        pass
        if os.path.exists(self.ruta_prestamos):
            with open(self.ruta_prestamos, "r", encoding="utf-8") as f:
                data = json.load(f)
                for p_data in data:
                    try:
                        p = Prestamo.from_dict(p_data)
                        self.prestamos.append(p)
                        if p.id_prestamo >= self.contador_prestamos:
                            self.contador_prestamos = p.id_prestamo + 1
                    except ValueError:
                        pass

    def _guardar_libros(self):
        with open(self.ruta_libros, "w", encoding="utf-8") as f:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, f, indent=4, ensure_ascii=False)

    def _guardar_prestamos(self):
        with open(self.ruta_prestamos, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.prestamos], f, indent=4, ensure_ascii=False)

    def _cargar_datos_prueba_si_vacio(self):
        if not self.libros:
            datos_iniciales = [
                ("1234567890", "Clean Code", "Robert C. Martin", 3),
                ("9876543210", "Aprendiendo Python", "Mark Lutz", 2),
                ("5555555555", "Design Patterns", "Erich Gamma", 1)
            ]
            for isbn, titulo, autor, cant in datos_iniciales:
                try:
                    self.registrar_libro(isbn, titulo, autor, cant)
                except ValueError:
                    pass

    def registrar_libro(self, isbn, titulo, autor, cantidad):
        isbn_clean = isbn.strip()
        if isbn_clean in self.libros:
            raise ValueError(f"Ya existe un libro con ISBN {isbn_clean}")
        libro = Libro(isbn_clean, titulo, autor, cantidad)
        self.libros[libro.isbn] = libro
        self._guardar_libros()
        return libro

    def prestar_libro(self, isbn, usuario):
        isbn_clean = isbn.strip()
        usuario_clean = usuario.strip()
        if len(usuario_clean) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        libro = self.libros.get(isbn_clean)
        if not libro:
            raise ValueError(f"No existe libro con ISBN {isbn_clean}")
        if libro.cantidad <= 0:
            raise ValueError(f"No hay ejemplares disponibles de '{libro.titulo}'")
        # Verificar préstamo activo para ese usuario y libro
        for p in self.prestamos:
            if p.isbn == isbn_clean and p.usuario == usuario_clean and not p.devuelto:
                raise ValueError(f"El usuario '{usuario_clean}' ya tiene un préstamo activo de '{libro.titulo}'")
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        fecha_dev = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        nuevo = Prestamo(self.contador_prestamos, isbn_clean, usuario_clean, fecha_hoy, fecha_dev, False)
        self.prestamos.append(nuevo)
        self.contador_prestamos += 1
        libro.cantidad -= 1
        self._guardar_libros()
        self._guardar_prestamos()
        return nuevo

    def devolver_libro(self, isbn, usuario):
        isbn_clean = isbn.strip()
        usuario_clean = usuario.strip()
        libro = self.libros.get(isbn_clean)
        if not libro:
            raise ValueError(f"No existe libro con ISBN {isbn_clean}")
        prestamo_activo = None
        for p in self.prestamos:
            if p.isbn == isbn_clean and p.usuario == usuario_clean and not p.devuelto:
                prestamo_activo = p
                break
        if not prestamo_activo:
            raise ValueError(f"No hay préstamo activo de '{libro.titulo}' para '{usuario_clean}'")
        prestamo_activo.devuelto = True
        libro.cantidad += 1
        self._guardar_libros()
        self._guardar_prestamos()
        return prestamo_activo

    def consultar_disponibilidad(self, isbn):
        isbn_clean = isbn.strip()
        libro = self.libros.get(isbn_clean)
        if not libro:
            raise ValueError(f"No existe libro con ISBN {isbn_clean}")
        return libro, libro.cantidad

    def listar_prestamos_activos(self):
        activos = [p for p in self.prestamos if not p.devuelto]
        resultado = []
        for p in activos:
            libro = self.libros.get(p.isbn)
            titulo = libro.titulo if libro else "Desconocido"
            resultado.append({
                "ID": p.id_prestamo,
                "ISBN": p.isbn,
                "Libro": titulo,
                "Usuario": p.usuario,
                "Fecha préstamo": p.fecha_prestamo,
                "Devolución prevista": p.fecha_devolucion_prevista
            })
        return resultado