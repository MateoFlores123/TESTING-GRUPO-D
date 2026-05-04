class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, cantidad: int):
        if not isbn or not isbn.strip():
            raise ValueError("ISBN es obligatorio")
        isbn_clean = isbn.strip()
        # Validar que sean solo 10 dígitos numéricos
        if not isbn_clean.isdigit():
            raise ValueError("ISBN debe contener solo dígitos numéricos (0-9)")
        if len(isbn_clean) != 10:
            raise ValueError("ISBN debe tener exactamente 10 dígitos")

        if not titulo or not titulo.strip():
            raise ValueError("El título es obligatorio")
        if not autor or not autor.strip():
            raise ValueError("El autor es obligatorio")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")

        self.isbn = isbn_clean
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.cantidad = cantidad

    def to_dict(self):
        return {"isbn": self.isbn, "titulo": self.titulo, "autor": self.autor, "cantidad": self.cantidad}

    @staticmethod
    def from_dict(data):
        return Libro(data["isbn"], data["titulo"], data["autor"], data["cantidad"])