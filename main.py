"""
main.py — Sistema de Biblioteca
Ejecutar: python main.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.catalogo import Catalogo
from data.datos_prueba import cargar_datos_prueba
from utils.formato import (
    encabezado, ok, error,
    imprimir_libro, imprimir_disponibilidad,
    imprimir_lista, pausar,
)


# ======================================================================
# RF-01 — Registrar Libro
# ======================================================================
def menu_registrar(catalogo):
    encabezado("RF-01 — REGISTRAR LIBRO")

    codigo    = input("  Código          : ").strip()
    titulo    = input("  Título          : ").strip()
    autor     = input("  Autor           : ").strip()
    categoria = input("  Categoría       : ").strip()
    anio      = input("  Año publicación : ").strip()
    cantidad  = input("  Cantidad        : ").strip()

    exito, resultado = catalogo.registrar_libro(codigo, titulo, autor, categoria, anio, cantidad)

    if exito:
        ok("Libro registrado exitosamente.")
        imprimir_libro(resultado)
    else:
        error(resultado)

    pausar()


# ======================================================================
# RF-02 — Buscar Libro
# ======================================================================
def menu_buscar(catalogo):
    encabezado("RF-02 — BUSCAR LIBRO")

    criterio = input("  Ingrese código, título o autor: ").strip()
    exito, resultado = catalogo.buscar_libro(criterio)

    if exito:
        ok(f"Se encontraron {len(resultado)} resultado(s).")
        imprimir_lista(resultado)
    else:
        error(resultado)

    pausar()


# ======================================================================
# RF-03 — Mostrar Disponibilidad
# ======================================================================
def menu_disponibilidad(catalogo):
    encabezado("RF-03 — DISPONIBILIDAD DE LIBRO")

    criterio = input("  Ingrese código o título: ").strip()
    exito, resultado = catalogo.mostrar_disponibilidad(criterio)

    if exito:
        ok(f"Consulta exitosa — {resultado.get_estado()}")
        imprimir_disponibilidad(resultado)
    else:
        error(resultado)

    pausar()


# ======================================================================
# Listar todos
# ======================================================================
def menu_listar(catalogo):
    encabezado("TODOS LOS LIBROS")
    libros = catalogo.listar_todos()
    if not libros:
        error("No hay libros registrados.")
    else:
        ok(f"{len(libros)} libro(s) en el sistema.")
        imprimir_lista(libros)
    pausar()


# ======================================================================
# Casos de prueba automáticos
# ======================================================================
def ejecutar_casos_prueba(catalogo):
    encabezado("CASOS DE PRUEBA AUTOMÁTICOS")

    casos = [
        ("RF-01 | Registro exitoso",
         catalogo.registrar_libro,
         ("LIB-099", "Clean Code", "Robert C. Martin", "Informática", 2008, 2), True),

        ("RF-01 | Código duplicado",
         catalogo.registrar_libro,
         ("LIB-099", "Clean Code", "Robert C. Martin", "Informática", 2008, 2), False),

        ("RF-01 | Título vacío",
         catalogo.registrar_libro,
         ("LIB-100", "", "Autor X", "Novela", 2020, 1), False),

        ("RF-01 | Cantidad = 0",
         catalogo.registrar_libro,
         ("LIB-101", "Libro X", "Autor Y", "Ciencia", 2021, 0), False),

        ("RF-01 | Año no numérico",
         catalogo.registrar_libro,
         ("LIB-102", "Libro Z", "Autor Z", "Arte", "abc", 1), False),

        ("RF-02 | Buscar por título (minúsculas)",
         catalogo.buscar_libro, ("python",), True),

        ("RF-02 | Buscar por autor",
         catalogo.buscar_libro, ("orwell",), True),

        ("RF-02 | Buscar por código",
         catalogo.buscar_libro, ("LIB-005",), True),

        ("RF-02 | Criterio sin resultados",
         catalogo.buscar_libro, ("xyzabc",), False),

        ("RF-02 | Criterio vacío",
         catalogo.buscar_libro, ("",), False),

        ("RF-03 | Disponibilidad por código",
         catalogo.mostrar_disponibilidad, ("LIB-001",), True),

        ("RF-03 | Disponibilidad por título parcial",
         catalogo.mostrar_disponibilidad, ("principito",), True),

        ("RF-03 | Libro inexistente",
         catalogo.mostrar_disponibilidad, ("LIB-999",), False),

        ("RF-03 | Campo vacío",
         catalogo.mostrar_disponibilidad, ("",), False),
    ]

    aprobados = 0
    fallidos  = 0
    print()

    for descripcion, funcion, args, exito_esperado in casos:
        exito_real, _ = funcion(*args)
        paso   = exito_real == exito_esperado
        estado = "PASS ✔" if paso else "FAIL ✖"
        print(f"  [{estado}]  {descripcion}")
        if paso: aprobados += 1
        else:    fallidos  += 1

    print(f"\n  Resultado: {aprobados} aprobados / {fallidos} fallidos de {len(casos)} casos.")
    pausar()


# ======================================================================
# Menú principal
# ======================================================================
def menu_principal():
    catalogo = Catalogo()
    cargar_datos_prueba(catalogo)

    while True:
        print("\n" + "=" * 62)
        print("       SISTEMA DE BIBLIOTECA")
        print("=" * 62)
        print(f"  Libros en el sistema: {catalogo.total()}")
        print()
        print("  1. Registrar libro")
        print("  2. Buscar libro")
        print("  3. Ver disponibilidad de un libro")
        print("  4. Listar todos los libros")
        print("  5. Ejecutar casos de prueba")
        print("  0. Salir")
        print()

        opcion = input("  Seleccione una opción: ").strip()

        if   opcion == "1": menu_registrar(catalogo)
        elif opcion == "2": menu_buscar(catalogo)
        elif opcion == "3": menu_disponibilidad(catalogo)
        elif opcion == "4": menu_listar(catalogo)
        elif opcion == "5": ejecutar_casos_prueba(catalogo)
        elif opcion == "0":
            print("\n  Hasta luego.\n")
            break
        else:
            print("\n  Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()