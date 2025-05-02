#Sumar los números positivos que se van ingresando hasta que se ingrese un 0.

num = int(input("Ingresa un numero: "))
suma = 0
while num != 0:
    suma = suma + num
    num = int(input("Ingresa un numero: "))
print("La suma de todos los numeros es de: ",suma)