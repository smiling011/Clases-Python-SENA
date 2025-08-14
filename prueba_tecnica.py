# Prueba tecnica
# Victoria Vielma Romero
# fecha: 13/08/25

while True:
    
    print("  ")
    print("Elija una Opcion")
    print("  ")
    print("0. terminar")
    print("1. Suma de Numeros")
    print("2. Par o Impar")
    print("3. Contar vocales")
    print("4. Encontrar el número más grande")
    print("5. Eliminar duplicados de una lista")
    print("6. Clase de usuario con metodo saludo")
    print("7. Validar fortaleza de contraseña")
    print("8. Convertidor a camelCase")
    print("9. Filtrar usuarios por edad")
    print("10. Obtener estudiantes con mejores calificaciones")
    print("  ")
    
    opcion = int(input("Escribe la opcion elejida: "))
    

#listo
    if opcion == 1:
        print("1. Suma de Numeros")
        def sum_lista(num):
            return sum(num)
        lista = [2, 4, 6, 7, 12, 44, 22]
        print(f"la Suma de la lista es: {sum_lista(lista)}")
#listo    
    elif opcion == 2:
        print("2. Par o Impar")
        num = int(input("Pon un numero: "))
        
        def par_impar(num):
            if num % 2 == 0:
                return "Es par"
            else:
                return "Es impar"
        print(f"{num} es: {par_impar(num)}")
    
#listo
    elif opcion == 3:
        print("3. Contar vocales")
        user_text = input("Escribe tu texto: ")
        
        def c_vocales(texto):
            vocal = "aeiou"
            return sum(1 for letra in texto if letra in vocal)
        
        print(f"El numero de vocales es: {c_vocales(user_text)}")
        
#listo    
    elif opcion == 4:
        print("4. Encontrar el numero mas grande")
        num = [3, 9, 1, 7]
        
        def big_num(lista):
            return max(lista)
        print(f"El numero mas grande es: {big_num(num)}")
    
#listo
    elif opcion == 5:
        print("5. Eliminar duplicados de una lista")
        
        def sin_dup(lista):
            return list(set(lista))
        
        num = [1, 2, 2, 3, 1]
        print(sin_dup(num))

#listp  
    elif opcion == 6:
        print("6. Clase de usuario con metodo saludo")
        
        nom = input("Tu nombre: ")
        mail = input("Tu correo: ")
        
        class Usuario:
            def __init__(self, usuario,email):
                self.usuario = usuario 
                self.email = email
            def  saludar(self):
                return f"Holiss, me llamo {self.usuario}"
            
        user = Usuario(nom, mail)
        
        print(user.saludar())
        
#listo
    elif opcion == 7:
        print("7. Validar fortaleza de contraseña")
        
        cont = input("Escribe una contraseña: ")
        def passw(contrasena):
            
            signos = "|!#$%&/(?¡¿)"
            
            return(
                len(contrasena) >= 8 and
                any(c.isupper() for c in contrasena) and
                any(c.islower() for c in contrasena) and
                any(c.isdigit() for c in contrasena) and
                any(c in signos for c in contrasena)
            )
        if passw(cont):
            print("La contraseña es seguera :)")
        else:
            print("la contrasena no es segura :(")
#
    elif opcion == 8:
        print("Problema no resuelto a tiempo :(")
        
#
    elif opcion == 9:
        print("Problema no resuelto a tiempo :(")
        
#
    elif opcion == 10:
        print("Problema no resuelto a tiempo :(")
    
    elif opcion == 0:
        break

    else:
        print("Error o invaliso")
