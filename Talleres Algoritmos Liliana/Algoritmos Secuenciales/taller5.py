#Convertir una temperatura de grados Celsius a Fahrenheit
# formula = (0 °C × 9/5) + 32 = 32 °F

print("Calcular de Celsius a Fahrenheit")
cel = float(input("Temperatura en C°: "))
fah = (cel * 9/5) +32
print(f"La temperatura de {cel}C° es {fah}F°")