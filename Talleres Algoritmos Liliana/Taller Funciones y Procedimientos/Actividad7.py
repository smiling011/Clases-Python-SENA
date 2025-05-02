# Realizar un procedimiento que realice la conversión de coordinadas
# polares(r,0) a coordenadas caterianas x,y
# X= r. cos(0)
# Y= r. sen(0)
import math

def conv(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

x, y = conv(5, math.pi/4)
print(f"Coordenadas Cartesianas: x={x}, y={y}")
