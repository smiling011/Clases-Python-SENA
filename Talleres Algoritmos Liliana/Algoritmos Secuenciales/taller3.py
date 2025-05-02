#Determinar si un número ingresado por el usuario es par o impar.

num = int(input("Ingresa el numero: "))
# if num / 2 == num / 2:
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")    

# % lee el residuo de la division de ahi si es par o no
