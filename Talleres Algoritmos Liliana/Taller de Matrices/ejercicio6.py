# Un algoritmo que llene una matriz de 5 x 6 y que imprima cuantos de los números
# almacenados son ceros, cuantos son positivos y cuantos son negativos.

import numpy as np

mat = np.random.randint(-10,11,(5,6))
print(mat)

cant_c = np.sum(mat == 0)
cant_p = np.sum(mat > 0)
cant_n = np.sum(mat < 0)

print("Cantidad de ceros: ",cant_c)
print("Cantidad de numeros positivos: ",cant_p)
print("Cantidad de numeros negativos: ",cant_n)
