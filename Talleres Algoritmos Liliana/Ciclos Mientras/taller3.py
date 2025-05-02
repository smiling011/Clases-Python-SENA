#Calcular el factorial de un número utilizando un ciclo mientras.
# 3! = 3x2x1 = 6 

num = int(input("Ingresa el numero: "))
fac = 1
i = 1
while i <= num:
    fac = fac * i
    i = i + 1
print(f"El factorial de {num} es: {fac}")   