"""Una persona trabaja 48 horas extras la semana, etsas 48 horas son ordinarias y
ademas trabaja 10 horas extras. 
Las horas ordinarias se pagan a 11.500/ hora
 y las horas estras tienes un 25% mas sobre el valor ordinario, Calcule el resultado """
 
""" Primero define las variables e indica el valor y/u operacion principal""" 

hora_o = 48
hora_e = 10
valor_o = 11500
valor_hora_ex = 11500 * 1.25

"""Ejecuta la operacion con el valor de las variables y da el resultado  final"""
salario = (hora_o * valor_o) + (hora_e * valor_hora_ex)

"""Imprime el resultado total de la operacion """ 
print(f"El salario total es: {salario}")
 
 