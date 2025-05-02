# datos del cuidador
class PerfilDueño:
    def __init__(self, id_perfil_dueño, nombre, apellido, email, num_tel, num_cel):
        self.id_perfil_dueño = id_perfil_dueño
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.num_tel = num_tel
        self.num_cel = num_cel
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_info(self):
        print(f"Dueño: {self.nombre} {self.apellido}")

#hoja de vida de la mascota
class PerfilMascota:
    def __init__(self, id_mascota, nombre, raza, peso, altura, edad, dueño):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        self.altura = altura
        self.edad = edad
        self.dueño = dueño
        self.vacunas = []

    def agregar_vacuna(self, vacunas):
        for vacuna in vacunas:
            self.vacunas.append(vacuna)

    def mostrar_info(self):
        print(f"Mascota: {self.nombre}, Raza: {self.raza}, Peso: {self.peso} kg, Altura: {self.altura} cm, Edad: {self.edad} años")

#rastrea la mascota
class DispositivoGPS:
    def __init__(self, id_dispositivo, mascota):
        self.id_dispositivo = id_dispositivo
        self.mascota = mascota

    def rastrear(self):
        print(f"Rastreando a {self.mascota.nombre}") 

#vacunas de la mascota
class Vacuna:
    def __init__(self, id_vacuna, nombre_vacuna):
        self.id_vacuna = id_vacuna
        self.nombre_vacuna = nombre_vacuna

    def mostrar_info(self):
        print(f"Vacunas: {self.nombre_vacuna}")



# info de cada clase

dueño1 = PerfilDueño(1, "Vicky", "Vielma", "vickytory@gmail.com", 123456789, 123456789)


mascota1 = PerfilMascota(1, "Mafalda", "husky", 30, 60, 12, dueño1)
dueño1.agregar_mascota(mascota1)


gps1 = DispositivoGPS(1, mascota1)


vacuna1 = Vacuna(1, "Rabia")
vacuna2 = Vacuna(2, "Coronavirus")
mascota1.agregar_vacuna([vacuna1 , vacuna2])


# muestra la info
dueño1.mostrar_info()
mascota1.mostrar_info()
gps1.rastrear()


# muestra las vacunas de las mascotas
for vacuna in mascota1.vacunas:
    vacuna.mostrar_info()
