# Realizar un algoritmo donde se recorra los algoritmos simultáneamente los
# vectores del punto 1, 2,3 mostrando posición y resultado.

import Actividad1
import Actividad2
import Actividad3

vec1 = Actividad1.vec1
vec2 = Actividad2.vec2
vec3 = Actividad3.vec3

for i in range(len(vec3)): 
    print(f"Posicion {i+1}: Vector 1={vec1[i]}, Vector 2={vec2[i]}, Vector 3={vec3[i]}")