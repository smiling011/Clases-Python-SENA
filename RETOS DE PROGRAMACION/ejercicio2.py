# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */

Triangulo = 1
Cuadrado = 2
Rectangulo = 3

poligono = int(input("Elige el poligono que quieres calcular su area: "))

if poligono == 1:
    b = float(input("Ingresa la base: "))
    h = float(input("Ingresa la altura: "))
    area = (b*h)/2
    print(f"El area del triangulo es: {area}")
elif poligono == 2:
    l = float(input("Ingresa la medida del lado: "))
    area = l*l
    print(f"El area del cuadrado es de {area}")
elif poligono == 3:
    b = float(input("Ingresa la base: "))
    h = float(input("Ingresa la altura: "))
    area = (b*h)
    print(f"El area del rectangulo es {area}")
else:
    print("Numero invalido")