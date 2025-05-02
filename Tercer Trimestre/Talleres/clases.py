# Clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn, precio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Precio: ${self.precio}")

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

# Clase Cliente
class Cliente:
    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"Cliente: {self.nombre}, Correo: {self.correo}, Telefono: {self.telefono}")

# Clase Pedido
class Pedido:
    def __init__(self, numero_pedido, cliente):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.lista_libros = []
        self.total = 0

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(libro.precio for libro in self.lista_libros)

    def mostrar_pedido(self):
        print(f"Pedido #{self.numero_pedido} para {self.cliente.nombre}:")
        for libro in self.lista_libros:
            libro.mostrar_informacion()
        print(f"Total: ${self.total}")

# Clase Libreria
class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_clientes = []
        self.lista_libros = []

    def agregar_cliente(self, cliente):
        self.lista_clientes.append(cliente)

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)

    def mostrar_inventario(self):
        print(f"Inventario de la librería {self.nombre}:")
        for libro in self.lista_libros:
            libro.mostrar_informacion()

    def buscar_libro(self, isbn):
        for libro in self.lista_libros:
            if libro.isbn == isbn:
                return libro
        return None

# Crear instancias de libros
libro1 = Libro("Python Basico", "John Doe", "123456", 50)
libro2 = Libro("Programacion Avanzada", "Jane Doe", "789012", 70)

# Crear una instancia de cliente
cliente1 = Cliente("Carlos Lopez", "carlos@mail.com", "555-0123")

# Crear una instancia de librería
libreria = Libreria("Librería Central")
libreria.agregar_libro(libro1)
libreria.agregar_libro(libro2)
libreria.agregar_cliente(cliente1)

# Crear un pedido para el cliente
pedido1 = Pedido(1, cliente1)
pedido1.agregar_libro(libro1)
pedido1.agregar_libro(libro2)

# Mostrar inventario y detalles del pedido
libreria.mostrar_inventario()
pedido1.mostrar_pedido()
