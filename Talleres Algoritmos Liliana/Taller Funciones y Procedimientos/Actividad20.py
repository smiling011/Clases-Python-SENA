# diseñar un algoritmo de una fusión que convierta una cadena en mayúscula y
# otra que la convierta minúscula.

def may(cadena):
    return cadena.upper()

def min(cadena):
    return cadena.lower()

cadena = input("Ingresa un texto o palabra: ")
opcion = input("¿Quieres convertirla a mayusculas o minusculas? (m para mayusculas, n para minusculas): ")

if opcion.lower() == 'm':
    print("En mayusculas:", may(cadena))
elif opcion.lower() == 'n':
    print("En minusculas:", min(cadena))
else:
    print("Opcion no valida. Por favor, ingresa 'm' para mayusculas o 'n' para minusculas.")
