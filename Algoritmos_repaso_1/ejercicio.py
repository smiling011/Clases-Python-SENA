"""Crear un algoritmo que pida numeros del 1 al 4, 
si el usuario presiona 1 entonces pida un numero1 y guardelo en la variable num1
y luego pida el numero dos y guardelo en la variable num2 (suma es igual num1 + num2)
Si el usuario presiona 2, entonces
pide lo mismo de arriba resta= num1-num2
si el usuario presiona 3, entonces
'' ''  multiplica=num1*num2
si el usuario presiona 4, entonces
'' '' divide=num1/num2""" 


opcion = int(input('Ingrese un numero del 1 al 4: '))

if opcion == 1:
    
    num1 = int(input("ingrese un numero: ")) 
    num2 = int(input("ingrese otro numero: " ))
    suma = num1 + num2
    print (suma)
    
elif opcion == 2:
    num1 = int(input("ingrese un numero: ")) 
    num2 = int(input("ingrese otro numero: " ))
    resta = num1 - num2
    print (resta)
elif opcion == 3:
    num1 = int(input("ingrese un numero: ")) 
    num2 = int(input("ingrese otro numero: " ))
    mult = num1 * num2
    print (mult)
elif opcion == 4:
    num1 = int(input("ingrese un numero: ")) 
    num2 = int(input("ingrese otro numero: " ))
    div = num1 / num2
    print (div)
else:
    print('Presiono un numero que no es del 1 al 4')
    
    #elif= ademas... else= de lo contrario del if