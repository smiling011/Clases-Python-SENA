# Realizar un procedimiento que obtenga la división entera y el resto de la misma
# utilizando la únicamente los operadores suma y resta

def div(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    resto = dividendo
    print(f"Cociente: {cociente}, Resto: {resto}")

div(17, 3)
