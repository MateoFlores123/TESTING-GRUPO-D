import tkinter as tk
from tkinter import ttk, messagebox
import re

class InterfazBiblioteca:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("📚 Biblioteca - Grupo D (Gestor Premium)")
        self.root.geometry("900x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")

        # Estilos
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#f0f4f8", tabposition='n')
        style.configure("TNotebook.Tab", font=("Segoe UI", 11, "bold"), padding=[15, 5], background="#d9e2ec")
        style.map("TNotebook.Tab", background=[("selected", "#4a90e2")], foreground=[("selected", "white")])
        style.configure("TButton", font=("Segoe UI", 10), padding=6, background="#4a90e2", foreground="white")
        style.map("TButton", background=[("active", "#357abd")])
        style.configure("TLabel", font=("Segoe UI", 10), background="#f0f4f8")
        style.configure("TEntry", font=("Segoe UI", 10), padding=4)

        # Pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        self.crear_pestana_registro()
        self.crear_pestana_prestamo()
        self.crear_pestana_devolucion()
        self.crear_pestana_consulta()
        self.crear_pestana_listado()

        # Inicializar validaciones
        self.init_validaciones()

    def crear_pestana_registro(self):
        frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(frame, text="📖 Registrar Libro")

        # Campos
        ttk.Label(frame, text="ISBN:").grid(row=0, column=0, sticky="e", pady=8, padx=5)
        self.isbn_entry = ttk.Entry(frame, width=40)
        self.isbn_entry.grid(row=0, column=1, pady=8, padx=5)
        self.isbn_error = ttk.Label(frame, text="", foreground="red", font=("Segoe UI", 9))
        self.isbn_error.grid(row=0, column=2, sticky="w", padx=10)

        ttk.Label(frame, text="Título:").grid(row=1, column=0, sticky="e", pady=8, padx=5)
        self.titulo_entry = ttk.Entry(frame, width=40)
        self.titulo_entry.grid(row=1, column=1, pady=8, padx=5)
        self.titulo_error = ttk.Label(frame, text="", foreground="red")
        self.titulo_error.grid(row=1, column=2, sticky="w", padx=10)

        ttk.Label(frame, text="Autor:").grid(row=2, column=0, sticky="e", pady=8, padx=5)
        self.autor_entry = ttk.Entry(frame, width=40)
        self.autor_entry.grid(row=2, column=1, pady=8, padx=5)
        self.autor_error = ttk.Label(frame, text="", foreground="red")
        self.autor_error.grid(row=2, column=2, sticky="w", padx=10)

        ttk.Label(frame, text="Cantidad:").grid(row=3, column=0, sticky="e", pady=8, padx=5)
        self.cantidad_entry = ttk.Entry(frame, width=40)
        self.cantidad_entry.grid(row=3, column=1, pady=8, padx=5)
        self.cantidad_error = ttk.Label(frame, text="", foreground="red")
        self.cantidad_error.grid(row=3, column=2, sticky="w", padx=10)

        btn = ttk.Button(frame, text="➕ Registrar Libro", command=self.registrar_libro)
        btn.grid(row=4, column=0, columnspan=2, pady=20)

    def crear_pestana_prestamo(self):
        frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(frame, text="📤 Prestar Libro")

        ttk.Label(frame, text="ISBN:").grid(row=0, column=0, sticky="e", pady=8, padx=5)
        self.prest_isbn_entry = ttk.Entry(frame, width=40)
        self.prest_isbn_entry.grid(row=0, column=1, pady=8, padx=5)
        self.prest_isbn_error = ttk.Label(frame, text="", foreground="red")
        self.prest_isbn_error.grid(row=0, column=2, sticky="w", padx=10)

        ttk.Label(frame, text="Usuario:").grid(row=1, column=0, sticky="e", pady=8, padx=5)
        self.prest_usuario_entry = ttk.Entry(frame, width=40)
        self.prest_usuario_entry.grid(row=1, column=1, pady=8, padx=5)
        self.prest_usuario_error = ttk.Label(frame, text="", foreground="red")
        self.prest_usuario_error.grid(row=1, column=2, sticky="w", padx=10)

        btn = ttk.Button(frame, text="✅ Prestar", command=self.prestar_libro)
        btn.grid(row=2, column=0, columnspan=2, pady=20)

    def crear_pestana_devolucion(self):
        frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(frame, text="📥 Devolver Libro")

        ttk.Label(frame, text="ISBN:").grid(row=0, column=0, sticky="e", pady=8, padx=5)
        self.dev_isbn_entry = ttk.Entry(frame, width=40)
        self.dev_isbn_entry.grid(row=0, column=1, pady=8, padx=5)
        self.dev_isbn_error = ttk.Label(frame, text="", foreground="red")
        self.dev_isbn_error.grid(row=0, column=2, sticky="w", padx=10)

        ttk.Label(frame, text="Usuario:").grid(row=1, column=0, sticky="e", pady=8, padx=5)
        self.dev_usuario_entry = ttk.Entry(frame, width=40)
        self.dev_usuario_entry.grid(row=1, column=1, pady=8, padx=5)
        self.dev_usuario_error = ttk.Label(frame, text="", foreground="red")
        self.dev_usuario_error.grid(row=1, column=2, sticky="w", padx=10)

        btn = ttk.Button(frame, text="🔄 Devolver", command=self.devolver_libro)
        btn.grid(row=2, column=0, columnspan=2, pady=20)

    def crear_pestana_consulta(self):
        frame = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(frame, text="🔍 Consultar")

        ttk.Label(frame, text="ISBN:").grid(row=0, column=0, sticky="e", pady=8, padx=5)
        self.cons_isbn_entry = ttk.Entry(frame, width=40)
        self.cons_isbn_entry.grid(row=0, column=1, pady=8, padx=5)
        self.cons_isbn_error = ttk.Label(frame, text="", foreground="red")
        self.cons_isbn_error.grid(row=0, column=2, sticky="w", padx=10)

        self.cons_resultado = ttk.Label(frame, text="", font=("Segoe UI", 11, "bold"), foreground="#2c3e50", background="#f0f4f8")
        self.cons_resultado.grid(row=1, column=0, columnspan=3, pady=20)

        btn = ttk.Button(frame, text="🔎 Consultar", command=self.consultar_disponibilidad)
        btn.grid(row=2, column=0, columnspan=3, pady=10)

    def crear_pestana_listado(self):
        frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame, text="📋 Préstamos Activos")

        # Treeview
        columns = ("ID", "ISBN", "Libro", "Usuario", "Fecha préstamo", "Devolución prevista")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=18)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120 if col != "Libro" else 200)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        btn_refresh = ttk.Button(frame, text="🔄 Refrescar", command=self.actualizar_listado)
        btn_refresh.pack(pady=10)
        self.actualizar_listado()

    def init_validaciones(self):
        # Validación ISBN (formato básico en tiempo real)
        def validar_isbn(entry, error_label):
            texto = entry.get().strip()
            if not texto:
                error_label.config(text="")
                return True
            if not texto.isdigit():
                error_label.config(text="❌ Solo dígitos numéricos (0-9)")
                return False
            if len(texto) != 10:
                error_label.config(text="❌ Debe tener exactamente 10 dígitos")
                return False
            error_label.config(text="✅ Válido", foreground="green")
            return True

        def validar_no_vacio(entry, error_label, campo):
            texto = entry.get().strip()
            if not texto:
                error_label.config(text=f"⚠️ {campo} obligatorio")
                return False
            error_label.config(text="✅ OK", foreground="green")
            return True

        def validar_cantidad(entry, error_label):
            texto = entry.get().strip()
            if not texto:
                error_label.config(text="")
                return True
            if not texto.isdigit() or int(texto) <= 0:
                error_label.config(text="❌ Número positivo")
                return False
            error_label.config(text="✅ OK", foreground="green")
            return True

        def validar_usuario(entry, error_label):
            texto = entry.get().strip()
            if not texto:
                error_label.config(text="")
                return True
            if len(texto) < 3:
                error_label.config(text="❌ Mínimo 3 caracteres")
                return False
            error_label.config(text="✅ OK", foreground="green")
            return True

        # Asignar eventos
        self.isbn_entry.bind("<KeyRelease>", lambda e: validar_isbn(self.isbn_entry, self.isbn_error))
        self.prest_isbn_entry.bind("<KeyRelease>", lambda e: validar_isbn(self.prest_isbn_entry, self.prest_isbn_error))
        self.dev_isbn_entry.bind("<KeyRelease>", lambda e: validar_isbn(self.dev_isbn_entry, self.dev_isbn_error))
        self.cons_isbn_entry.bind("<KeyRelease>", lambda e: validar_isbn(self.cons_isbn_entry, self.cons_isbn_error))

        self.titulo_entry.bind("<KeyRelease>", lambda e: validar_no_vacio(self.titulo_entry, self.titulo_error, "Título"))
        self.autor_entry.bind("<KeyRelease>", lambda e: validar_no_vacio(self.autor_entry, self.autor_error, "Autor"))
        self.cantidad_entry.bind("<KeyRelease>", lambda e: validar_cantidad(self.cantidad_entry, self.cantidad_error))

        self.prest_usuario_entry.bind("<KeyRelease>", lambda e: validar_usuario(self.prest_usuario_entry, self.prest_usuario_error))
        self.dev_usuario_entry.bind("<KeyRelease>", lambda e: validar_usuario(self.dev_usuario_entry, self.dev_usuario_error))

    def prestar_libro(self):
        isbn = self.prest_isbn_entry.get()
        usuario = self.prest_usuario_entry.get()
        try:
            prestamo = self.controlador.prestar_libro(isbn, usuario)
            messagebox.showinfo("Préstamo", f"Préstamo ID {prestamo.id_prestamo} - Devuelva antes de {prestamo.fecha_devolucion_prevista}")
            self.prest_isbn_entry.delete(0, tk.END)
            self.prest_usuario_entry.delete(0, tk.END)
            self.prest_isbn_error.config(text="")
            self.prest_usuario_error.config(text="")
            # 👇 Refrescar la tabla de préstamos activos
            self.actualizar_listado()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def devolver_libro(self):
        isbn = self.dev_isbn_entry.get()
        usuario = self.dev_usuario_entry.get()
        try:
            self.controlador.devolver_libro(isbn, usuario)
            messagebox.showinfo("Devolución", "Libro devuelto correctamente")
            self.dev_isbn_entry.delete(0, tk.END)
            self.dev_usuario_entry.delete(0, tk.END)
            self.dev_isbn_error.config(text="")
            self.dev_usuario_error.config(text="")
            # 👇 Refrescar la tabla de préstamos activos
            self.actualizar_listado()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def registrar_libro(self):
        isbn = self.isbn_entry.get()
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        cantidad_str = self.cantidad_entry.get()
        if not cantidad_str.isdigit():
            messagebox.showerror("Error", "Cantidad inválida")
            return
        cantidad = int(cantidad_str)
        try:
            self.controlador.registrar_libro(isbn, titulo, autor, cantidad)
            messagebox.showinfo("Éxito", f"Libro '{titulo}' registrado")
            self.isbn_entry.delete(0, tk.END)
            self.titulo_entry.delete(0, tk.END)
            self.autor_entry.delete(0, tk.END)
            self.cantidad_entry.delete(0, tk.END)
            self.isbn_error.config(text="")
            self.titulo_error.config(text="")
            self.autor_error.config(text="")
            self.cantidad_error.config(text="")
            # 👇 Opcional: refrescar por si algún préstamo se ve afectado
            self.actualizar_listado()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def consultar_disponibilidad(self):
        isbn = self.cons_isbn_entry.get()
        try:
            libro, cantidad = self.controlador.consultar_disponibilidad(isbn)
            self.cons_resultado.config(text=f"📗 '{libro.titulo}' - {libro.autor} → Disponibles: {cantidad}")
            self.cons_isbn_error.config(text="✅ Válido", foreground="green")
        except ValueError as e:
            self.cons_resultado.config(text="❌ " + str(e))
            self.cons_isbn_error.config(text="❌ No encontrado", foreground="red")

    def actualizar_listado(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        prestamos = self.controlador.listar_prestamos_activos()
        for p in prestamos:
            self.tree.insert("", tk.END, values=(p["ID"], p["ISBN"], p["Libro"], p["Usuario"], p["Fecha préstamo"], p["Devolución prevista"]))

    def iniciar(self):
        self.root.mainloop()