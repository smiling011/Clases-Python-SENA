# Sumar los números pares del 1 al 20 utilizando un ciclo repita.
num = 2 # d 2 en 2 para q sea siempre par
sum = 0

while True:
    sum = sum + num
    num = num + 2
    if num > 20:
        break 
        #termina el cilo
print("La suma de los numeros pares es de: ",sum)