# Crea una lista llamada pares con todos los pares clave-valor del diccionario persona.

persona = {"nombre":"vicky", "edad":19, "ciudad":"San Antonio de los Altos"}
pares = list(persona.items()) # con "items" imprime tanto el campo como el valor
print(pares)