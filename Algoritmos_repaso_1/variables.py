ninguno = None
print(ninguno)
print(type(ninguno))
valor = 1500
print(valor)
print(type(valor))
valor2= 560.25
print(valor2)
print(type(valor2))
valor3 = b"hola"
print(valor3)
print(type(valor3))
""" hola como estas"""
valor4 = "Las Flipantes aventuras de Dacky"
print(valor4)
print(type(valor4))
valor5 = True
valor6 = False
print(valor5)
print(type(valor5))
print(valor6)
print(type(valor6))

lista = [None, 12, 5.4, b"18", True, False, "Vicky", [1, 2, 3, 4, 5, 6, 7, 8, 9, [10]]]
print(lista)
print(type(lista))
print(lista[6])
print(lista[7][2])
print(lista[7][9][0])
""" diccionario"""
diccionario = {"nombre": "Vicky", "altura": "180", "peso": "78"}
print(diccionario)
print(type(diccionario))
print(diccionario["nombre"])
"""doble diccionario"""
estudiantes = {"nombre": "Vicky","edad": 19, "calificaciones": {"historia": 5, "matematicas": 4} }

print(estudiantes["calificaciones"])
print(estudiantes["calificaciones"]["matematicas"])

"""tuple"""
estudiante = ("Vicky", 1, (90, 85, 88))
print(type(estudiante))
print(estudiante[2][1])