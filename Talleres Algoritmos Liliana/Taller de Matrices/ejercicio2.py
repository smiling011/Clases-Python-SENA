# Un algoritmo que llene una matriz de 7 x 7. Calcular la suma de cada renglón y
# almacenarla en un vector, la suma de cada columna y almacenarla en otro vector.

import  numpy as np

mat = np.random.randint(1,11,(7,7))
print(mat)
sum_c = mat.sum(axis=0)#axis=0 para eje vertical
sum_f = mat.sum(axis=1)#axis=1 para eje horizontal

print("Total de las columnas: ",sum_c)
print("Total de las filas: ",sum_f)