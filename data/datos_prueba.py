# data/datos_prueba.py

LIBROS_PRUEBA = [
    ("LIB-001", "Cien años de soledad",             "Gabriel García Márquez",  "Novela",      1967, 3),
    ("LIB-002", "El Quijote",                        "Miguel de Cervantes",     "Clásico",     1605, 2),
    ("LIB-003", "1984",                              "George Orwell",           "Distopía",    1949, 4),
    ("LIB-004", "Introducción a los Algoritmos",     "Thomas H. Cormen",        "Informática", 2009, 2),
    ("LIB-005", "El Principito",                     "Antoine de Saint-Exupéry","Fábula",      1943, 5),
    ("LIB-006", "Harry Potter y la Piedra Filosofal","J.K. Rowling",            "Fantasía",    1997, 3),
    ("LIB-007", "Sapiens",                           "Yuval Noah Harari",       "Historia",    2011, 2),
    ("LIB-008", "Python para todos",                 "Charles Severance",       "Informática", 2016, 1),
]


def cargar_datos_prueba(catalogo):
    """Carga los libros de prueba en el catálogo recibido."""
    for codigo, titulo, autor, categoria, anio, cantidad in LIBROS_PRUEBA:
        catalogo.registrar_libro(codigo, titulo, autor, categoria, anio, cantidad)
    print(f"  [INFO] {catalogo.total()} libros de prueba cargados.\n")