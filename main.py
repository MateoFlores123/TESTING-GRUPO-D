#!/usr/bin/env python3
from controlador import ControladorBiblioteca
from vista import InterfazBiblioteca

if __name__ == "__main__":
    app = InterfazBiblioteca(ControladorBiblioteca())
    app.iniciar()