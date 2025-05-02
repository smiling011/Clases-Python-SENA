# Un algoritmo que llene una matriz de 5 x 5 y que almacene la diagonal principal en un
# vector. Imprimir el vector resultante.

import numpy as np

mat = np.random.randint(1,11,(5,5))
vec = np.diag(mat)

print(mat)
print(vec)