# repaso de variables :)
"""holiss"""
# variables nulas
ninguno = None
print(type(ninguno))
print(ninguno)

# variables entero
a = 150
print(type(a))
print(a)

#variables decimal
b = 75.7
print(type(b))
print(b)

# variable verdadero o falso
c =True
print(type(c))
print(c)

# variable de cadenas de caracteres
d = "Vicky"
print(type(d))
print(d)

#variables de listas
lista = [None, 150, 75.7, True, "Vicky",[1, 2, 3, ['a', 'b', 'c']]]
print(type(lista))
print(lista)

#variables de diccionario
dic = {
    "nombre": "Vicky",
    "telefono": "320007789",
    "estado": True,
    "salario_hora": "12000.5",
    "materias": {
                "matematicas": 4.4,
                "ciencias": 5,
                "historia": 5
                }
    }
print(type(dic))
print(dic)

#variables tuplas para cambiar las listas
f = ("Vicky", 1234567890, True, 12000.5)
# Cambiar valores en listas
lista[4] = "Dacky"
print(lista)

lista[5][2] = 4
print(lista)

lista[5][3][2] = 'z'
print(lista)

#para cambiar los valores en los dicionarios
dic["materias"]["matematicas"] = 2.0
print(dic)

# no se puede cambiar los valores una tupla