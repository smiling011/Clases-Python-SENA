# Leer una secuencia de números y sumar solo los pares mostrando el
# resultado del proceso.

sum = 0
while True:
    num = int(input("Introduce un numero: "))
    if num == 0:
        break
    if num % 2 == 0:
        sum = sum + num
print("Suma de pares:", sum)
