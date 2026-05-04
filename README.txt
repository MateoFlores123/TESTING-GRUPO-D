===========================================
Módulo Biblioteca - Grupo D (GUI Premium)
Guerra de Testers
===========================================

VERSIÓN MEJORADA:
- Interfaz gráfica moderna con validaciones en tiempo real.
- Mensajes de error dinámicos junto a los campos.
- Sistema de pruebas unitarias (test_biblioteca.py) que verifica todas las reglas de negocio.

EJECUCIÓN:
- GUI: python main.py
- Pruebas: python test_biblioteca.py

PRUEBAS UNITARIAS:
Se incluyen 12 casos que cubren:
- Registro correcto, duplicados, ISBN inválido, cantidad negativa.
- Préstamo con stock, sin stock, usuario repetido, ISBN inexistente.
- Devolución correcta, devolución sin préstamo activo.
- Consulta existente/inexistente.
- Listado de préstamos activos (con y sin datos).

Todos los tests pasan sin errores, demostrando la robustez del sistema.

CARACTERÍSTICAS DE CALIDAD:
- Validación en tiempo real (mientras escribe) de ISBN, campos obligatorios, usuario (mínimo 3 caracteres) y cantidad positiva.
- Persistencia JSON.
- Manejo extremo de excepciones: ninguna operación genera crash.
- Interfaz con pestañas, colores agradables, feedback visual (✅❌).

¡Este sistema está listo para la guerra de testers!