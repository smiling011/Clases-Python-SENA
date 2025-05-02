import tkinter as tk
from tkinter import messagebox
import math

def actualizar_campos(*args):
    figura = variable_figura.get()
    operacion = variable_operacion.get()

    etiqueta_radio.grid_forget()
    entrada_radio.grid_forget()
    etiqueta_base.grid_forget()
    entrada_base.grid_forget()
    etiqueta_altura.grid_forget()
    entrada_altura.grid_forget()
    etiqueta_lado.grid_forget()
    entrada_lado.grid_forget()
    etiqueta_apotema.grid_forget()
    entrada_apotema.grid_forget()

    if figura == "Círculo" and operacion:
        etiqueta_radio.grid(row=2, column=0, padx=5, pady=5)
        entrada_radio.grid(row=2, column=1, padx=5, pady=5)
    elif figura == "Triángulo":
        if operacion == "Área":
            etiqueta_base.grid(row=2, column=0, padx=5, pady=5)
            entrada_base.grid(row=2, column=1, padx=5, pady=5)
            etiqueta_altura.grid(row=3, column=0, padx=5, pady=5)
            entrada_altura.grid(row=3, column=1, padx=5, pady=5)
        elif operacion == "Perímetro":
            etiqueta_lado.grid(row=2, column=0, padx=5, pady=5)
            entrada_lado.grid(row=2, column=1, padx=5, pady=5)
    elif figura == "Cuadrado" and operacion:
        etiqueta_lado.grid(row=2, column=0, padx=5, pady=5)
        entrada_lado.grid(row=2, column=1, padx=5, pady=5)
    elif figura == "Pentágono":
        if operacion == "Área":
            etiqueta_lado.grid(row=2, column=0, padx=5, pady=5)
            entrada_lado.grid(row=2, column=1, padx=5, pady=5)
            etiqueta_apotema.grid(row=3, column=0, padx=5, pady=5)
            entrada_apotema.grid(row=3, column=1, padx=5, pady=5)
        elif operacion == "Perímetro":
            etiqueta_lado.grid(row=2, column=0, padx=5, pady=5)
            entrada_lado.grid(row=2, column=1, padx=5, pady=5)
    elif figura == "Hexágono":
        if operacion == "Área":
            etiqueta_lado.grid(row=2, column=0, padx=5, pady=5)
            entrada_lado.grid(row=2, column=1, padx=5, pady=5)
            etiqueta_apotema.grid(row=3, column=0, padx=5, pady=5)
            entrada_apotema.grid(row=3, column=1, padx=5, pady=5)
        elif operacion == "Perímetro":
            etiqueta_lado.grid(row=2, column=0, padx=5, pady=5)
            entrada_lado.grid(row=2, column=1, padx=5, pady=5)

def calcular():
    figura = variable_figura.get()
    operacion = variable_operacion.get()

    try:
        if figura == "Círculo":
            radio = float(entrada_radio.get())
            if operacion == "Área":
                resultado = math.pi * radio**2
            elif operacion == "Perímetro":
                resultado = 2 * math.pi * radio
        elif figura == "Triángulo":
            if operacion == "Área":
                base = float(entrada_base.get())
                altura = float(entrada_altura.get())
                resultado = (base * altura) / 2
            elif operacion == "Perímetro":
                lado = float(entrada_lado.get())
                resultado = 3 * lado
        elif figura == "Cuadrado":
            lado = float(entrada_lado.get())
            if operacion == "Área":
                resultado = lado**2
            elif operacion == "Perímetro":
                resultado = 4 * lado
        elif figura == "Pentágono":
            if operacion == "Área":
                lado = float(entrada_lado.get())
                apotema = float(entrada_apotema.get())
                resultado = (5 * lado * apotema) / 2
            elif operacion == "Perímetro":
                lado = float(entrada_lado.get())
                resultado = 5 * lado
        elif figura == "Hexágono":
            if operacion == "Área":
                lado = float(entrada_lado.get())
                apotema = float(entrada_apotema.get())
                resultado = (3 * lado * apotema) / 2
            elif operacion == "Perímetro":
                lado = float(entrada_lado.get())
                resultado = 6 * lado

        etiqueta_resultado.config(text=f"Resultado: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")

ventana = tk.Tk()
ventana.title("Calculadora de Figuras Geométricas")

tk.Label(ventana, text="Selecciona la figura:").grid(row=0, column=0, padx=10, pady=10)
variable_figura = tk.StringVar(ventana)
figura_menu = tk.OptionMenu(ventana, variable_figura, "Círculo", "Triángulo", "Cuadrado", "Pentágono", "Hexágono", command=actualizar_campos)
figura_menu.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Selecciona la operación:").grid(row=1, column=0, padx=10, pady=10)
variable_operacion = tk.StringVar(ventana)
operacion_menu = tk.OptionMenu(ventana, variable_operacion, "Área", "Perímetro", command=actualizar_campos)
operacion_menu.grid(row=1, column=1, padx=10, pady=10)

etiqueta_radio = tk.Label(ventana, text="Radio:")
entrada_radio = tk.Entry(ventana)

etiqueta_base = tk.Label(ventana, text="Base:")
entrada_base = tk.Entry(ventana)
etiqueta_altura = tk.Label(ventana, text="Altura:")
entrada_altura = tk.Entry(ventana)

etiqueta_lado = tk.Label(ventana, text="Lado:")
entrada_lado = tk.Entry(ventana)

etiqueta_apotema = tk.Label(ventana, text="Apotema:")
entrada_apotema = tk.Entry(ventana)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
