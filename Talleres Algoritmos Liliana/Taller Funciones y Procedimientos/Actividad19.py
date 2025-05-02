# escribir un algoritmo que convierta los números arábigos en números romanos
# y viceversa I=1, V=5, X=10, L=50,C=100, D=500 y M=1000.

def con_ar(numero):
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    resultado = ''
    for valor, letra in valores:
        while numero >= valor:
            resultado += letra
            numero -= valor
    return resultado

def con_ra(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    for i in range(len(romano)):
        if i > 0 and valores[romano[i]] > valores[romano[i - 1]]:
            resultado += valores[romano[i]] - 2 * valores[romano[i - 1]]
        else:
            resultado += valores[romano[i]]
    return resultado

entrada = input("Ingresa un numero arabigo o romano: ")

if entrada.isdigit():
    num_a = int(entrada)
    rom = con_ar(num_a)
    print(f"{num_a} en numeros romanos es: {rom}")

else:
    arab = con_ra(entrada.upper())
    print(f"{entrada.upper()} en numeros arabigos es: {arab}")
