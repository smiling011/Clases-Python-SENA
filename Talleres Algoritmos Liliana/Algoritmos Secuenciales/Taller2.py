#Calcular el promedio de un conjunto de números ingresados por el usuario.

cant_num = int(input("Cantidad de numeros a calcular: "))
suma = 0

for i in range(cant_num):
    num = float(input(f"Ingrese los numeros {i+1}: "))
    suma = suma + num
    
promedio = suma / cant_num
print("El promedio de los numeros ingresados es: ", promedio)