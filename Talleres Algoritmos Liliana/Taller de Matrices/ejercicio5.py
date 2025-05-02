# Un algoritmo que llene una matriz de 6 x 8 y que almacene toda la matriz en un vector.
# Imprimir el vector resultante.

import numpy as np

mat = np.random.randint(1,11,(6,8))
print(mat)
vec = np.hstack(mat)# np.hstack(): Apila arrays horizontalmente
print("Datos almacenados: ",vec)