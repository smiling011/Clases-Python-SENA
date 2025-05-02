# Escribir una función Salario que calcula los salarios de un trabajados para un
# numero dado de horas trabajadas y un salario hora. Las horas que superan las
# 40 horas semanales se pagaran como extras con un salario hora 1,5 veces el
# salario ordinario.

def salario(ht, sal_h):
    if ht <= 40:
        return ht * sal_h
    else:
        he = ht - 40
        return (40 * sal_h) + (he * sal_h * 1.5)

ht = float(input("Ingrese las horas trabajadas: "))
sal_h = float(input("Ingrese el salario por hora: "))

total = salario(ht, sal_h)

print("Salario total:", total)
