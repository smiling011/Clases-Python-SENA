# solicitar 10 numeros, y comprobar si
# son pares o impares, una vez combrobado, sumar los pares y sumar los impares
#if num % 2 == 0:
#else:

#con for
"""
sumaimpar = 0
suma = 0

for i in range(10):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        suma += num
    else:
        sumaimpar += num
print(f"La suma de los Pares es: {suma}")
print(f"La suma de los Impares es: {sumaimpar}")
"""

#con while
sumapar = 0
sumaimpar = 0
i = 0
while i <= 10:
    i += 1
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
            sumapar += num
    else:
        sumaimpar += num
print(f"La suma de los Pares es: {sumapar}")
print(f"La suma de los Impares es: {sumaimpar}")