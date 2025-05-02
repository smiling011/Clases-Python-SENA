total = 0
for cont in range(5):
    num = int(input("Ingresar numero: "))
    total = total + num
print(f"El total es de: {total}")

total = 0
for cont in range(5):
    num = int(input(f"Ingresar numero {cont + 1}: "))
    total = total + num
print(f"El total es de: {total}")