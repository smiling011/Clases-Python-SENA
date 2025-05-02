# escribir un algoritmo para contar el numero de ocurrencias de cada una de las
# palabras ‘a’, ‘an’,’and’ en las diferentes líneas de texto.

def pal(texto):
    palabras = texto.lower().split()
    return {
        'a': palabras.count('a'),
        'an': palabras.count('an'),
        'and': palabras.count('and')
    }

texto = "Vivienne Westwood was an iconic designer. She played a key role in the punk fashion movement."
ocurrencias = pal(texto)
print(ocurrencias)
