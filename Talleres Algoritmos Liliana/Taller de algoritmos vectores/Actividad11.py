# Leer una secuencia de números y mostrar su producto, el proceso finalizará
# cuando el usuario pulsa la tecla n

pro = 1
while True:
    num = input("Introduce un numero: ")
    if num.lower() == 'n':
        break
    pro *= int(num)
print("Total:", pro)
