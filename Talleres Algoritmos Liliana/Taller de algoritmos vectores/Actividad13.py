# Hacer un vector de 30 números y mostrar la suma de los pares y el
# producto de los que son múltiplo de 5.

import numpy as np

vec = np.random.randint(1, 100, 30)
print("Vector:", vec)

sum = np.sum(vec[vec % 2 == 0])
prod = np.prod(vec[vec % 5 == 0])
print("Suma de pares:", sum)
print("Producto de multiplos de 5:", prod)
