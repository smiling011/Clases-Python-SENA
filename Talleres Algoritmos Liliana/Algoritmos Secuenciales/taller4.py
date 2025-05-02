#Calcular el factorial de un número natural ingresado por el usuario
# 3! = 3x2x1 = 6 
#Calcula el numero de orden en el q se puede organizar el numero factorial ej:
#123
#132
#213
#231
#312
#321       3! = 6 por q se organiza de 6 maneras diferentes :) secuencia


num = int(input("Ingresa el numero: "))
fac = 1
for i in range(1, num + 1):
    # el + 1 para q forme la lista del 1 hasta el numero q le indica, si no le pones + 1 el bucle quedara incompleto 
    fac = fac * i
print(f"El factorial de {num} es: {fac}") 