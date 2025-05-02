# Un algoritmo que llene una matriz de 10 x10 y que almacene en la diagonal principal el
# menor de ese renglón.

import numpy as np

mat = np.random.randint(1,11,(10,10))
print(mat)
diag = np.diag(mat)
print("Diagonal sin oganizar: ",diag)
diag_o = np.sort(diag)# np.sort(): Ordena un array
print("Diagonal organizada de menor a mayor: ",diag_o)
