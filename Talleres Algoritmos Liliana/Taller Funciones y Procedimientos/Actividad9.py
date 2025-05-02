# Escribir una función booleana Digito que determine si un carácter es uno de los
# dígitos 0 al 9.

def dig(caracter):
    return caracter.isdigit()

user = input("Ingrese un caracter o digito: ")

resultado = dig(user)

if resultado:
    print(f"'{user}' es un digito.")
else:
    print(f"'{user}' no es un digito.")
