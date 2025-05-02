# Un algoritmo que almacene números en una matriz de 5 x 6. Imprimir la suma de los
# números almacenados en la matriz.

import numpy as np

mat = np.random.randint(1,50,(5,6))
sum = np.sum(mat)

print(mat)
print("La suma total es: ",sum)