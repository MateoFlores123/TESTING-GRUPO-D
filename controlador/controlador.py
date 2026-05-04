from modelo import BibliotecaModelo

class ControladorBiblioteca:
    def __init__(self):
        self.modelo = BibliotecaModelo()

    def registrar_libro(self, isbn, titulo, autor, cantidad):
        return self.modelo.registrar_libro(isbn, titulo, autor, cantidad)

    def prestar_libro(self, isbn, usuario):
        return self.modelo.prestar_libro(isbn, usuario)

    def devolver_libro(self, isbn, usuario):
        return self.modelo.devolver_libro(isbn, usuario)

    def consultar_disponibilidad(self, isbn):
        return self.modelo.consultar_disponibilidad(isbn)

    def listar_prestamos_activos(self):
        return self.modelo.listar_prestamos_activos()