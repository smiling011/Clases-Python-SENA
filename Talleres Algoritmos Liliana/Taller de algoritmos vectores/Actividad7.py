# Llenar un vector, donde el algoritmo sea capaz de calcular y llenarse solo
# con múltiplos de 20, cuando esté listo, debe realizar tres preguntas al usuario,
# desea promediar el vector, mostrar su suma, mostrar cada resultado de cada
# posición dividido por 2.

import numpy as np

mult = np.arange(20, 201, 20)
print(mult)

prom = np.mean(mult)
print("Promedio:", prom)

sum = np.sum(mult)
print("Suma:", sum)

div = mult / 2
print("Dividido por 2:", div)
