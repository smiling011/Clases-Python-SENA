# dado el nombre de una serie de estudiantes y las calificaciones obtenidas en
# un examen, calcular e imprimir la calificación media así como cada calificación
# y la diferencia con la media.

def cal_m(estudiantes, calificaciones):
    media = sum(calificaciones) / len(calificaciones)
    print("Calificacion media:", media)
    for estudiante, calificacion in zip(estudiantes, calificaciones):
        diferencia = calificacion - media
        print(f"Estudiante: {estudiante}, Calificacion: {calificacion}, Diferencia con la media: {diferencia:.2f}")

nom = ["Vicky", "David", "Ana", "Nataly", "Juan Camilo"]
calificaciones = [5, 4.5, 5, 4, 4.1]

cal_m(nom, calificaciones)
