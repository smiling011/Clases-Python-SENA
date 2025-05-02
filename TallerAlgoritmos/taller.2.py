opcion = int(input("Seleccione un numero del 1 al 3:    "))
if opcion == 1:
    print("Area del triangulo")
    b = int(input("Ingrese la base: "))
    h = int(input("Ingrese la altura: "))
    area = b * h / 2
    print("El area del triangulo es: ", area)

if opcion == 2:
    print("Area del circulo")
    r = int(input("Ingrese el radio del circulo: "))
    area = 3.1416 * r * r
    print("El area del circulo es: ", area)
if opcion == 3:
    print("Area del Rectangulo")
    b = int(input("Ingrese la base: "))
    h = int(input("Ingrese la altura: "))
    area = b * h
    print("El area del rectangulo es: ",area)