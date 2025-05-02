cant_num = int(input('¿Cuántos números quiere ingresar: '))
if cant_num > 0:
    suma = 0
    for i in range(cant_num):
        num = float(input(f'Ingrese el número {(i + 1)}: '))
        suma += num
    pro = suma / cant_num
    print(f'El promedio de los {cant_num} números es {pro:.2f}')
    
else:
    print('El valor ingresado no es válido.')