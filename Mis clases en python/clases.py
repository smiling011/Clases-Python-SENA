class persona:
    pass # clase q define en mayuscula en primera
    def __init__(self, nombre, apellido, edad, direccion):
        #atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        
    #metodo saludar
    def saludar(self):
        print(f"Hola, {self.nombre} {self.apellido}")
        
        
# # vicky es un objeto q es parte de la coleccion de la clase persona
# Vicky=persona("Vicky","Vielma",19,"cl 12 c78")
# Vicky.saludar()
objeto_persona = persona("Circulo","Mejia",17,"cl 12 c 78")
objeto_persona.saludar()
class Aprendiz(persona):
    def __init__(self, programa,estado):
        super().__init__(nombre, apellido, edad, direccion) # indicando atributos de la clase principal
        self.programa = programa
        self.estado = estado
    def activar(self):
        if self.estado == True:
            print("El aprendiz esta activo")
        else:
            print("El aprendiz esta desactivado")
            
Arredondo = Aprendiz("adso",false)
Arredondo.activar()
if __name__=="__main__":
    Arredondo = Aprendiz("Areedondo", "Mejia",17,"cl 12 c 78, adso, false")
    print()