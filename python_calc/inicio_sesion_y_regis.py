import tkinter as tk
from tkinter import ttk
import re

class AplicacionLogin:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Inicio de Sesion')
        
        #Variables para almacenar los datos del formilario
        self.usuario_var = tk.StringVar()
        self.contrasena_var = tk.StringVar()
        
        # Crear etiquetas y los campos de entrada para el inicio de sesion
        self.etiqueta_usuario = ttk.Label(ventana, text='Usuario: ')
        self.etiqueta_usuario.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        
        self.entrada_usuario = ttk.Entry(ventana, textvariable=self.usuario_var)
        self.entrada_usuario.grid(row=0, column=1, padx=10, pady=5)
        
        self.etiqueta_contarsena = ttk.Label(ventana, text='Contraseña')
        self.etiqueta_contarsena.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        self.entrada_contrasena = ttk.Entry(ventana, textvariable=self.contrasena_var, show='*')
        self.entrada_contrasena.grid(row=1, column=1, padx=10, pady=5)
        
        self.btn_ingresar = ttk.Button(ventana, text='Ingresar', command=self.ingresar)
        self.btn_ingresar.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        
        self.btn_registrar = ttk.Button(ventana, text='Registrar Usuario', command=self.registrar)
        self.btn_registrar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    
    def ingresar(self):
        usuario = self.usuario_var.get()
        contrasena = self.contrasena_var.get()
        
        if usuario == 'admin' and contrasena == 'A1234$5678s':
            print('Inicio de Sesion Exitoso')
        else:
            print('Las credenciales ingresadas son incorrectas')
            
    def registrar(self):
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title('Registro de Usuario')
        
        #Las variables para almacenar los datos del formulario de registro
        self.nombre_var = tk.StringVar()
        self.apellido_var = tk.StringVar()
        self.correo_var = tk.StringVar()
        self.nueva_contrasena_var = tk.StringVar()
        
        #Etiquetas y campos pra  el formulario de registro
        ttk.Label(ventana_registro, text='Nombre: ').grid(row=0, column=0, padx=10, pady=5, sticky="e")
        ttk.Entry(ventana_registro, textvariable=self.nombre_var).grid(row=0,  column=1, padx=10, pady=5)
        
        ttk.Label(ventana_registro, text='Apellido: ').grid(row=1, column=1, padx=10, pady=5, sticky="e")
        ttk.Entry(ventana_registro, textvariable=self.apellido_var).grid(row=1,  column=1, padx=10, pady=5)
        
        ttk.Label(ventana_registro, text='Correo Electronico: ').grid(row=2, column=0, padx=10, pady=5, sticky="e")
        ttk.Entry(ventana_registro, textvariable=self.correo_var).grid(row=2,  column=1, padx=10, pady=5)
        
        ttk.Label(ventana_registro, text='Contrasena: ').grid(row=3, column=0, padx=10, pady=5, sticky="e")
        ttk.Entry(ventana_registro, textvariable=self.contrasena_var).grid(row=3,  column=1, padx=10, pady=5)
        
        ttk.Button(ventana_registro, text='Registrar Usuario', command=self.validar_registro).grid(row=4, column=0, padx=10, pady=5)
        
    def validar_registro(self):
        nombre = self.nombre_var.get()
        apellido = self.apellido_var.get()
        correo = self.correo_var.get()
        nueva_contrasena = self.nueva_contrasena_var.get()
        
        #validar contraseña 
        if (len(nueva_contrasena) >= 10 and re.search(r"[a-z]", nueva_contrasena) and re.search(r"[A-Z]", nueva_contrasena) and re.search(r"[\d]", nueva_contrasena)
        and re.search(r"[$%.;]", nueva_contrasena)):
            print('Registro Exitoso')
            print('Nombres: ', nombre)
            print('Apellidos: ', apellido)
            print('Correo Electronico: ', correo)
            print('Contraseña: ', nueva_contrasena)
        else:
            print('La contraseña no cumple con los requisitos')
            
# crear la aplicacion
ventana_principal = tk.Tk()
app = AplicacionLogin(ventana_principal)
ventana_principal.mainloop()
                        