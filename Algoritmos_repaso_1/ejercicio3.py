"""Un banco le presta dinero a mayores de edad que 
ganan mas de un salario minimo mensual legal vigente. 
Hacer un algoritmo que determine si un cliente puede hacer un prestamo en ese banco."""

edad_mayor = int(input("Si es mayor presione 1, si es menor de edad presione 2:"))

if edad_mayor == 1:
    salario = int(input("Ingrese su salario: "))
    if salario >= 1300000:
    print("el banco no puede hacer el prestamo")
else:
    print("el banco no presta dinero a menores ")
else:
