print("         Escalas de Temperaturas")
print("Escribe A para Celcius a kelvin")
print("Escribe B para Celcius a Fahrenheit")
print("Escribe C para Fahrenheit a Celcius")
print("Escribe D para Fahrenheit a Kelvin")
print("Escribe E para kelvin a Celcius")
print("Escribe F para Kelvin a Fahrenheit")

tipo_tem = str(input("Escriba el tipo de temperatura: "))

if tipo_tem == "a":
    print("Calcular de grados Celcius a Kelvin")
    c = int(input("Escriba la temperatura de en grados Celcius: "))
    gk = c + 273.15
    print(f"De {c} grados celcius son {gk} grados kelvin")
    
elif tipo_tem == "b":
    print ("Calcular de grados Celcius a Fahrenheit")
    c = int(input("Escriba la temperatura en grados Celcius: "))
    gf = c * 9/5 + 32
    print(f"De {c} grados celcius son {gf} grados Fahrenheit")
    
elif tipo_tem == "c":
    print ("Calcular de grados Fahrenheit a Celcius")
    f = int(input("Escriba la temperatura en grados Fahrenheit: "))
    gc = (f - 32) * 5/9
    print(f"De {f} grados Fahrenheit son {gc} grados celcius")

elif tipo_tem == "d":
    print("Calcular de grados Fahrenheit a kelvin")
    f = int(input("Escriba la temperatura en grados Fahrenheit: "))
    gk = (f - 32) * 5/9 + 273.15
    print(f"De {f} grados Fahrenheit son {gk} grados kelvin")
    
elif tipo_tem == "e":
    print("Calcular de grados Kelvin a Celcius")
    k = int(input("Escribe la temperatura en grados kelvin: "))
    gc = k  - 273.15 
    print(f"De {k} grados kelvin son {gc} grados celcius")
    
elif tipo_tem == "f":
    print("Calcular de grados Kelvin a Farenheit")
    k = int(input("Escribe la temperatura en grados kelvin: "))
    gf = (k - 273.15) * 9/5 + 32
    print(f"De {k} grados kelvin son {gf} en grados farenheit")
    