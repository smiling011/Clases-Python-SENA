# Hacer un vector donde el usuario ingrese 5 nota matemáticas, otro vector 5
# notas inglés y el vector nombre del estudiante al que corresponde dichas notas,
# de esos vectores debe calcular un vector promedio, más adelante vector
# promedio debe mostrar todos los promedios y el estudiante que corresponda. 

import numpy as np

mat = np.array([5, 4, 3, 5, 1])
eng = np.array([4, 3, 2, 4, 5])
nom = np.array(['Vicky', 'David', 'Ana', 'Nataly', 'Juan Camilo'])

prom = (mat + eng) / 2
# Del ejercicio 5 el algoritmo debe ser capaz de preguntar al usuario el nombre
# del estudiante que desee mostrar el promedio.
nom_est = input("Ingrese el nombre del estudiante: ")

if nom_est in nom:
    use = np.where(nom == nom_est)[0][0]
    print(f"El promedio de {nom_est} es: {prom[use]}")
else:
    print("Estudiante no encontrado")
