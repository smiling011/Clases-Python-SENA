# escribir el algoritmo que permita obtener el número de elementos positivos de
# una tabla.

import numpy as np

tabla = np.random.randint(-10, 11, size=(3, 3))

def num_p(matriz):
    positivos = 0
    for fila in matriz:
        for elemento in fila:
            if elemento > 0:
                positivos += 1
    return positivos

numero_positivos = num_p(tabla)
print(tabla)
print(f"Los elementos positivos en la tabla es: {numero_positivos}")
