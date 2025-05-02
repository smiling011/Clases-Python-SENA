# Crea una lista llamada numeros_pares con los números pares del 1 al 10 utilizando una lista por comprensión.
numeros_pares = [1,2,3,4,5,6,7,8,9,10]
numeros_pares = [i for i in numeros_pares if i % 2 ==0]
print(numeros_pares)