# Diseñar un procedimiento que acepte un numero de mes, un numero de día y
# un numero de año y los visualice en el formato dd/mm/aa Por ejemplo, los
# valores 19,09,1987 se visualizarían así: 19/9/87 y para los valores 3,9, y 1905
# así: 3/9/05.

def fecha(dia, mes, ano):
    print(f"{dia}/{mes}/{ano % 100:02d}")

fecha(19, 9, 1987)
