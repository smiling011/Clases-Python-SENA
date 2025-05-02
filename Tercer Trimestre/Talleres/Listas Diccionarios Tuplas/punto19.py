# Crea un diccionario llamado personas con los nombres y edades de varias personas. Luego, crea una 
# lista llamada mayores con los nombres de las personas mayores de edad (mayores o iguales a 18 años).


personas = [
    {"Nombre": "Vicky", "Edad": 19},
    {"Nombre": "Ana", "Edad": 17},
    {"Nombre": "David", "Edad": 10},
    {"Nombre": "Arredondo", "Edad": 16}
]

for persona in personas:
    nombre = persona["Nombre"]  
    edad = persona["Edad"]      
    
    if edad >= 18:
        print(f"{nombre} es mayor de edad")
    else:
        print(f"{nombre} es menor de edad")

print(personas)







# personas = {"Nombre":"Vicky", "Edad": 19,
#             "Nombre":"Ana", "Edad": 17,
#             "Nombre":"David", "Edad": 10,
#             "Nombre":"Arredondo", "Edad": 16}
# mayores = list(personas.items(Edad))
# if mayores >= 18:
#     print(f"{personas.items(Nombre)}es mayor de edad")
# else:
#     print("Es menor de edad")
# print(personas)
