print("Interes compuesto del dinero prestado")
dinp = int(input("Ingrese el valor del dinero prestado: $"))
tasainteres = int(input("Ingrese el porcentaje de interes: %"))
ano = int(input("Ingrese el numero de años acumulados: $"))
interescom = dinp *  tasainteres / 100  * ano
print("El total de interes del dinero prestado es de: $",interescom)
