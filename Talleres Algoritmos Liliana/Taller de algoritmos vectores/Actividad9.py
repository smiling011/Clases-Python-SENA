# Llenar un vector de 30 números por el usuario, donde saque promedio de los
# números, diga el menor, el mayor y los que son múltiplos de 2.
import numpy as np

vec = np.random.randint(1, 100, 30)  
print("Vector:", vec)

prom = np.mean(vec)
print("Promedio:", prom)

men = np.min(vec)
may = np.max(vec)
print("Menor:", men, "Mayor:", may)

mult = vec[vec % 2 == 0]
print("Multiplos de 2:", mult)