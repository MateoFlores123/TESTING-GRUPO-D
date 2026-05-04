import unittest
import os
import shutil
from modelo import BibliotecaModelo

class TestBiblioteca(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data_dir = "test_datos_temp"
        if os.path.exists(cls.test_data_dir):
            shutil.rmtree(cls.test_data_dir)

    def setUp(self):
        self.biblio = BibliotecaModelo(ruta_datos=self.test_data_dir)
        self.biblio.libros.clear()
        self.biblio.prestamos.clear()
        self.biblio.contador_prestamos = 1

    def tearDown(self):
        del self.biblio

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_data_dir):
            shutil.rmtree(cls.test_data_dir)

    # ---------- Pruebas de registro ----------
    def test_registrar_libro_exitoso(self):
        libro = self.biblio.registrar_libro("1234567890", "Python 101", "Juan Perez", 5)
        self.assertEqual(libro.isbn, "1234567890")
        self.assertEqual(libro.titulo, "Python 101")
        self.assertEqual(libro.cantidad, 5)
        self.assertIn("1234567890", self.biblio.libros)

    def test_registrar_libro_isbn_duplicado(self):
        self.biblio.registrar_libro("1112223334", "Libro A", "Autor A", 1)
        with self.assertRaises(ValueError) as context:
            self.biblio.registrar_libro("1112223334", "Libro B", "Autor B", 2)
        self.assertTrue("Ya existe" in str(context.exception))

    def test_registrar_libro_isbn_invalido(self):
        with self.assertRaises(ValueError):
            self.biblio.registrar_libro("", "Titulo", "Autor", 1)
        with self.assertRaises(ValueError):
            self.biblio.registrar_libro("ABC", "Titulo", "Autor", 1)

    def test_registrar_libro_cantidad_negativa(self):
        with self.assertRaises(ValueError):
            self.biblio.registrar_libro("9999999999", "Titulo", "Autor", -5)

    # ---------- Préstamos ----------
    def test_prestar_libro_exitoso(self):
        self.biblio.registrar_libro("7894560123", "Libro Test", "Autor T", 2)
        prestamo = self.biblio.prestar_libro("7894560123", "Luis Gomez")
        self.assertEqual(prestamo.usuario, "Luis Gomez")
        self.assertFalse(prestamo.devuelto)
        _, cant = self.biblio.consultar_disponibilidad("7894560123")
        self.assertEqual(cant, 1)

    def test_prestar_libro_sin_stock(self):
        self.biblio.registrar_libro("0001112223", "Sin Stock", "Autor", 1)
        self.biblio.prestar_libro("0001112223", "Usuario1")
        with self.assertRaises(ValueError) as ctx:
            self.biblio.prestar_libro("0001112223", "Usuario2")
        self.assertTrue("No hay ejemplares disponibles" in str(ctx.exception))

    def test_prestar_libro_usuario_repite_mismo_libro(self):
        self.biblio.registrar_libro("5556667778", "Libro Unico", "Autor", 2)
        self.biblio.prestar_libro("5556667778", "Laura")
        with self.assertRaises(ValueError) as ctx:
            self.biblio.prestar_libro("5556667778", "Laura")
        self.assertTrue("ya tiene un préstamo activo" in str(ctx.exception))

    def test_prestar_libro_isbn_inexistente(self):
        with self.assertRaises(ValueError) as ctx:
            self.biblio.prestar_libro("NO-EXISTE", "Usuario")
        self.assertTrue("No existe libro" in str(ctx.exception))

    def test_prestar_libro_usuario_corto(self):
        self.biblio.registrar_libro("7778889990", "Libro", "Autor", 1)
        with self.assertRaises(ValueError) as ctx:
            self.biblio.prestar_libro("7778889990", "A")
        self.assertTrue("al menos 3 caracteres" in str(ctx.exception))

    # ---------- Devoluciones ----------
    def test_devolver_libro_exitoso(self):
        self.biblio.registrar_libro("4445556667", "Libro Dev", "Autor D", 1)
        self.biblio.prestar_libro("4445556667", "Carlos")
        prestamo = self.biblio.devolver_libro("4445556667", "Carlos")
        self.assertTrue(prestamo.devuelto)
        _, cant = self.biblio.consultar_disponibilidad("4445556667")
        self.assertEqual(cant, 1)

    def test_devolver_libro_sin_prestamo_activo(self):
        self.biblio.registrar_libro("9990001112", "Libro No Prestado", "Autor", 1)
        with self.assertRaises(ValueError) as ctx:
            self.biblio.devolver_libro("9990001112", "Ana")
        self.assertTrue("No hay préstamo activo" in str(ctx.exception))

    def test_devolver_libro_isbn_invalido(self):
        with self.assertRaises(ValueError):
            self.biblio.devolver_libro("", "Usuario")

    # ---------- Consulta disponibilidad ----------
    def test_consultar_disponibilidad_existente(self):
        self.biblio.registrar_libro("1231231234", "Libro Consulta", "Autor C", 3)
        libro, cant = self.biblio.consultar_disponibilidad("1231231234")
        self.assertEqual(libro.titulo, "Libro Consulta")
        self.assertEqual(cant, 3)

    def test_consultar_disponibilidad_inexistente(self):
        with self.assertRaises(ValueError):
            self.biblio.consultar_disponibilidad("INE-999")

    # ---------- Listar préstamos activos ----------
    def test_listar_prestamos_activos(self):
        self.biblio.registrar_libro("9998887776", "Libro Lista", "Autor L", 2)
        self.biblio.prestar_libro("9998887776", "Pedro")
        self.biblio.prestar_libro("9998887776", "Maria")
        self.biblio.devolver_libro("9998887776", "Pedro")
        activos = self.biblio.listar_prestamos_activos()
        self.assertEqual(len(activos), 1)
        self.assertEqual(activos[0]["Usuario"], "Maria")

    def test_listado_vacio(self):
        activos = self.biblio.listar_prestamos_activos()
        self.assertEqual(len(activos), 0)

if __name__ == "__main__":
    unittest.main()