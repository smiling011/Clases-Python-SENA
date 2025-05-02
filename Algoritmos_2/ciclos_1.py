#estructuras repetitiva
# for: para
# while : hace que se ejecute un numero interminado de veces, condicional.(mientras)
# cont = cont + 1 : la cantidad de veces que se repite la accion
#acum = acum + valor : 

cont = 0
acum = 0

while cont < 3:
    num = int(input("Ingrese un numero: "))
    cont = cont + 1
    acum = acum + num
print(f"El acumulado total es de: {acum}")

