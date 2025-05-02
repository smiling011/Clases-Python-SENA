# calcular la suma de los elementos de la diagonal principal de una matriz de 4x4

import numpy as np

mat = np.random.randint(1, 11, (4, 4))
sum = np.trace(mat)

print(mat)
print("Suma de la diagonal:", sum)
