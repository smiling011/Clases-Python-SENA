# Promediar un conjunto de calificaciones de estudiantes.

num_cal = int(input("Numero de calificaciones: "))
suma = 0

for i in range(num_cal):
    cal = int(input(f"Calificacion {i+1}: "))
    suma = suma + cal
    
prom = suma / num_cal
print(f"Tu promedio es: {prom}")