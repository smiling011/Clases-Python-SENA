# Diseñar el algoritmo para calcular el máximo común divisor de cuatro números
# basado en una su algoritmo función mcd(el máximo común divisor de dos
# números).
import math

def mcd(a, b):
    return math.gcd(a, b)

def mcd_num(a, b, c, d):
    return mcd(mcd(a, b), mcd(c, d))


total = mcd_num(24, 36, 48, 60)
print("El MCD de los cuatro numeros es:", total)
