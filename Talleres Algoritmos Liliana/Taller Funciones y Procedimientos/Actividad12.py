# Escribir una función que permita deducir si una fecha leída del teclado es
# válida.

def fecha(dia, mes, ano):
    try:
        from datetime import datetime
        datetime(ano, mes, dia)
        return True
    except ValueError:
        return False
    
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
ano = int(input("Ingrese el año: "))

if fecha(dia, mes, ano):
    print("La fecha es valida.")
else:
    print("La fecha no es valida.")
