# Implementar la función cos() para calcular el coseno de un ángulo.

# math.sqrt = raiz
# pow = potencia
# math.sin = seno
# math.cos = coseno
# math.tan = tangente

import math
ang = int(input(F"Ingresa el angulo: "))
cos = math.cos(math.radians(ang))

print(f"El coseno del angulo de {ang}° es de: {cos}")