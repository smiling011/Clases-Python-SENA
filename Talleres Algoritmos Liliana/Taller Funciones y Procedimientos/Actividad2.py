# Diseñar la función FACTORIAL que calcule la factorial de un número entero
# entre el rango 100 a 1.000.000.
def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)


factorial = fac(18)
print("Factorial de 18 es:", factorial)
