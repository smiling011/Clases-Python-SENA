# Diagrama de grantt
# Clases = progrmacion orientada a onjetos
# UML a programacion orientada a objetos

class Usuario:# esta es una clase decarada pero las clases hijas pueden asignar atributro
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def mostrarInformacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
        
#esta parte es herencia
class Administrador(Usuario):
    def __init__(self, nombre, edad, correo, departamento):
        super().__init__(self, nombre, edad, correo)
        #llamar al constructor
        self.departamento=departamento
    def mostrarInformacion(self):
        print(f"El  nombre del contador es: {self.nombre}, la edad es: {self.edad},su correo es: {self.correo} y pertenece al departamento:{self.departamento}")
    
    
#esta parte es herencia
class Contador(Usuario):
    def __init__(self, nombre, edad, correo, tipo):
        super().__init__(self, nombre, edad, correo)
        #llamar al constructor
        self.tipo=tipo
    def mostrarInformacion(self):
        print(f"El  nombre del contador es: {self.nombre}, la edad es: {self.edad},su correo es: {self.correo} y su tipo de contrato es:{self.tipo}")

Administrador1=Administrador("Diego", 20, "diegogonzalez@gmail.com", "financiera")
Administrador1.mostrarInformacion()
Contador1= Contador("Vicky", 19, "tory_vielma@gmail.com", 2)
Contador1.mostrarInformacion()
