import itertools

# Definir los caracteres posibles (mayúsculas, minúsculas, números, signos)
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Rango de longitud de las contraseñas (por ejemplo, entre 4 y 6 caracteres)
min_length = 8
max_length = 15

# Crear el archivo de salida
with open("wordlist.txt", "w") as file:
    for length in range(min_length, max_length + 1):
        # Generar todas las combinaciones para la longitud actual
        for combination in itertools.product(characters, repeat=length):
            password = "".join(combination)
            file.write(password + "\n")

print("Wordlist generada y guardada en wordlist.txt")
