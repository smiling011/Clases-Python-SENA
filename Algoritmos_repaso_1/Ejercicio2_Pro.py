opcion = int(input('Ingrese un numero del 1 al 4: '))

if opcion == 1:
     #area de circulo
    radio = int(input("ingrese el radio: ")) 
    areac = (radio**2)*3.1416
    print(areac)
    
elif opcion == 2:
    #area de triangulo
    b = int(input("ingrese la base: ")) 
    h = int(input("ingrese la altura: " ))
    areat = (b * h)/2
    print (areat)
    
elif opcion == 3:
    #area de penta
    lado = int(input("ingrese el lado: ")) 
    apotema = int(input("ingrese el apotema: " ))
    p = lado * 5
    areap = (p*apotema)/2
    print (areap)
    
elif opcion == 4:
    #area de octa
    lado = int(input("ingrese el lado: ")) 
    apotema = int(input("ingrese el apotema: " ))
    p = lado * 8
    areap = (p*apotema)/2
    print (areap)
else:
    print('Presiono un numero que no es del 1 al 4')