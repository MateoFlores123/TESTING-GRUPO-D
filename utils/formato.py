# utils/formato.py

SEP  = "-" * 62
SEP2 = "=" * 62


def encabezado(texto):
    print(f"\n{SEP2}\n  {texto}\n{SEP2}")


def ok(msg):
    print(f"\n  [✔] {msg}")


def error(msg):
    print(f"\n  [✖] {msg}")


def imprimir_libro(libro):
    print(SEP)
    print(f"  Código          : {libro.get_codigo()}")
    print(f"  Título          : {libro.get_titulo()}")
    print(f"  Autor           : {libro.get_autor()}")
    print(f"  Categoría       : {libro.get_categoria()}")
    print(f"  Año publicación : {libro.get_anio_publicacion()}")
    print(f"  Disponibles     : {libro.get_cantidad_disponible()} / {libro.get_cantidad_total()}")
    print(f"  Estado          : {libro.get_estado()}")
    print(SEP)


def imprimir_disponibilidad(libro):
    print(SEP)
    print(f"  Título          : {libro.get_titulo()}")
    print(f"  Autor           : {libro.get_autor()}")
    print(f"  Total ejemplares: {libro.get_cantidad_total()}")
    print(f"  Disponibles     : {libro.get_cantidad_disponible()}")
    print(f"  Estado          : {libro.get_estado()}")
    print(SEP)


def imprimir_lista(libros):
    print(SEP)
    print(f"  {'Código':<10} {'Título':<28} {'Autor':<18} {'Disp.'}")
    print(SEP)
    for l in libros:
        print(
            f"  {l.get_codigo():<10} "
            f"{l.get_titulo()[:27]:<28} "
            f"{l.get_autor()[:17]:<18} "
            f"{l.get_cantidad_disponible()}/{l.get_cantidad_total()}"
        )
    print(SEP)


def pausar():
    input("\n  Presiona Enter para continuar...")