# Elimina la clave "ciudad" del diccionario persona.

persona = {"nombre":"vicky", "edad":int(input("Escribe tu edad: ")), "ciudad":"San Antonio de los Altos"}
del persona["ciudad"] # el "del" elimina una entrada especifica del diccionario
print(persona)

# persona = {"nombre":"vicky", "edad":int(input("Escribe tu edad: ")), "ciudad":"San Antonio de los Altos"}
# del persona["nombre"] 
# print(persona)