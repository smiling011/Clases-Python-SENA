import os

# Ruta completa a la carpeta donde se crearán los archivos
ruta_completa = "C:\JAVASCRIPT\Trimestre 3\Taller 3"

# Crear los directorios si no existen
os.makedirs(ruta_completa, exist_ok=True)

# Crear 20 archivos numerados de 1.py ...
for i in range(1, 7):
    filename = os.path.join(ruta_completa, f"Ejercicio{i}.js")
    with open(filename, "w") as file:
        file.write(f" ")

# Confirmación
os.listdir(ruta_completa)
