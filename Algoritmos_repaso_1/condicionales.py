#variables condicionales
a = "Dacky"
if a == "Vicky":
    print(f'El nombre es correcto, {a} es igual a "Vicky"')
else:
    print(f'El nombre es incorrecto, {a} no es igual a "Vicky"')

opcion = int(input('Ingrese un numero del 1 al 5: '))

if opcion == 1:
    print('Presiono 1')
elif opcion == 2:
    print('Presiono 2')
elif opcion == 3:
    print('Presiono 3')
elif opcion == 4:
    print('Presiono 4')
elif opcion == 5:
    print('Presiono 5')
else:
    print('Presiono un numero que no es del 1 al 5')
    
    #elif= ademas... else= de lo contrario del if
    
# condiciones verdadero y falso 

nom = "Vicky"
telefono = 12345

if nom == "Vicky" and telefono == 12345:
    print("Se cumplen las dos condiciones")
else: 
    print("NO se cumplen las dos condiciones")



