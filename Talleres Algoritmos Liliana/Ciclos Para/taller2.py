# Sumar los números pares del 1 al 20.

suma = 0
for i in range(1,21):
    if i % 2 == 0:
        suma = suma + i
        print("La suma de los pares es: ", suma)
    

