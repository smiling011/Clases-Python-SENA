# Leer una secuencia de números, hasta que se introduce un número
# negativo y mostrar la suma de dichos números.

sum = 0
while True:
    num = int(input("Introduce un numero: "))
    if num < 0:
        break
    sum += num
print("Suma total:", )
