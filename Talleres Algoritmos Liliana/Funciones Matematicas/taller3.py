#Implementar la función sin() para calcular el seno de un ángulo.
#  ° a radianes

# math.sqrt = raiz
# pow = potencia
# math.sin = seno
# math.cos = coseno
# math.tan = tangente

# todos los grados se pasan primero a radianes math.radians
import math
ang = int(input(f"Ingrese el angulo: "))
sin = math.sin(math.radians(ang))

print(f"El seno del angulo de {ang}° es de: {sin}")