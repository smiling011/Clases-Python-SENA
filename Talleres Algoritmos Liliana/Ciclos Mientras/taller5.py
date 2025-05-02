# Jugar un juego de adivinanzas donde el usuario debe adivinar un número secreto
# random para q el numero sea al azar, lo elige el programa
import random

num_se = random.randint (1,100)
num_us = int(input("Ingrese un numero random: "))

while num_us != (num_se):
    num_us = int(input("Ingrese otro numero: "))
print("Adivinaste el numero secreto: ",num_se)
  