#listas
#Secuencias ordenadas de objetos estos datos pueden ser de distintos tipos: float, int etc.

# LISTA

lista=[]
lista1=[1,"nombre",True, "Cl 10",1.90]
#       0    1      2        3     4
#print(lista)

print(lista1)
print(lista1[2])
lista1[2]=False
print(lista1[2])
lista1.pop(2)
lista2=lista1
lista.append(5)
print("esta e lista",lista)
lista4=[1,45,4,8,0]
lista4.sort()# no lo va ordenar por que tiene que ser de un solo tipo
lista3=[1,4,True,"cl 10",1.90]
print("esta e lista",lista4)
print("esta rango",lista3[0:3])


#TUPLAS
# estructuras de datos que almacenan múltiples elementos en una única variable.

# ejemplos de tuplas de la
mi_tupla=(1,[3,4,6],True)
# las tuplas no se puede eliminar índices, tampoco puede modificar contenido
# permite ordenar pero debe ser del mismo tipo
var=mi_tupla[1]
print(var)
print(var[2])
# una tupla es una lista constante
