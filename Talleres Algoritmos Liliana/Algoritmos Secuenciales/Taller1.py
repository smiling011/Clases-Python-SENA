#Calcular el área de un triángulo, rectángulo o círculo, según la figura seleccionada por el usuario.
print("Calcular Area del Triangulo: ingrese 1")
print("Calcular Area del Rectangulo: ingrese 2")
print("Calcular Area del Circulo: ingrese 3")

figura = int(input("Ingrese el numero de la figura que desea calcular: "))

if figura == 1:
    b = float(input("Ingresa la Base: "))
    h = float(input("Ingresa la Altura: "))
    Area = b * h / 2
    print("El area del triangulo es: ", Area)
elif figura == 2:
    b = float(input("Ingresa la Base: "))
    h = float(input("Ingresa la Altura: "))
    Area = b * h
    print("El area del rectangulo es: ", Area)
elif figura == 3:
    r = float(input("Ingresa el Radio: "))
    Area = 3.1416 * r ** 2
    print("El area del circulo es:", Area)
