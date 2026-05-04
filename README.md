# Sistema de Biblioteca

Proyecto base para el curso de **Testing, Implementación y Mantenimiento de Sistemas**.  
Cubre las funcionalidades RF-01, RF-02 y RF-03 del requerimiento funcional de biblioteca.

---

## Estructura del proyecto

```
biblioteca/
├── models/
│   ├── __init__.py
│   ├── libro.py                 ← Clase Libro (atributos + getters/setters + lógica de inventario)
│   ├── resultado_operacion.py   ← Envuelve cualquier respuesta del sistema
│   └── catalogo.py              ← Repositorio central — RF-01, RF-02, RF-03, stubs RF-05/RF-06
├── data/
│   ├── __init__.py
│   └── datos_prueba.py          ← 8 libros precargados para pruebas
├── utils/
│   ├── __init__.py
│   └── formato.py               ← Funciones para imprimir en consola
├── main.py                      ← Demo ejecutable de las 3 funcionalidades
└── README.md
```

---

## Requisitos

- Python 3.10 o superior  
- Sin dependencias externas

---

## Ejecución

```bash
# Desde la raíz del proyecto
python main.py
```

---

## Guía para cada integrante

### Integrante 1 — RF-01: Registrar Libro
Archivo: `models/catalogo.py` → método `registrar_libro()`  
El modelo ya está implementado. Crea tu módulo de vista/controlador que llame a este método y muestre los resultados usando `utils/formato.py`.

### Integrante 2 — RF-02: Buscar Libro
Archivo: `models/catalogo.py` → método `buscar_libro(criterio)`  
El método busca por código, título o autor sin distinción de mayúsculas.  
Crea tu módulo de vista que reciba el criterio del usuario y muestre la lista.

### Integrante 3 — RF-03: Mostrar Disponibilidad
Archivo: `models/catalogo.py` → método `mostrar_disponibilidad(criterio)`  
Retorna estado "Disponible" / "No disponible" con conteo de ejemplares.  
Crea tu módulo de vista que consuma este método.

---

## Cómo usar el Catálogo desde tu módulo

```python
from models.catalogo import Catalogo
from data.datos_prueba import cargar_datos_prueba
from utils.formato import imprimir_resultado, imprimir_libro

# Opción A: catálogo vacío
catalogo = Catalogo()

# Opción B: catálogo con datos de prueba
catalogo = cargar_datos_prueba()

# RF-01
resultado = catalogo.registrar_libro("LIB-010", "Mi Libro", "Autor", "Novela", 2023, 3)
imprimir_resultado(resultado)

# RF-02
resultado = catalogo.buscar_libro("autor")
if resultado.es_exitoso():
    for libro in resultado.get_datos():
        imprimir_libro(libro)

# RF-03
resultado = catalogo.mostrar_disponibilidad("LIB-001")
imprimir_resultado(resultado)
```

---

## Datos de prueba disponibles

| Código   | Título                              | Autor                    | Disponible |
|----------|-------------------------------------|--------------------------|------------|
| LIB-001  | Cien años de soledad                | Gabriel García Márquez   | 3/3        |
| LIB-002  | El Quijote                          | Miguel de Cervantes      | 2/2        |
| LIB-003  | 1984                                | George Orwell            | 4/4        |
| LIB-004  | Introducción a los Algoritmos       | Thomas H. Cormen         | 2/2        |
| LIB-005  | El Principito                       | Antoine de Saint-Exupéry | 5/5        |
| LIB-006  | Harry Potter y la Piedra Filosofal  | J.K. Rowling             | 3/3        |
| LIB-007  | Sapiens                             | Yuval Noah Harari        | 2/2        |
| LIB-008  | Python para todos                   | Charles Severance        | 1/1        |

---

## Validaciones implementadas (por RF)

### RF-01 — Registrar
- Campo vacío → `"Todos los campos son obligatorios."`
- Código duplicado → `"Ya existe un libro registrado con ese código."`
- Cantidad < 1 → `"La cantidad debe ser mayor a cero."`

### RF-02 — Buscar
- Criterio vacío → `"Ingrese un criterio de búsqueda."`
- Sin resultados → `"No se encontraron libros con ese criterio."`

### RF-03 — Disponibilidad
- Campo vacío → `"Ingrese un código o título para consultar."`
- No encontrado → `"No se encontró ningún libro con ese criterio."`