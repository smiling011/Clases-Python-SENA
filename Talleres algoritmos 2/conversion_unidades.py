import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Calculadora de Converison de unidades")
ventana.geometry("400x300")
ventana.configure(background='#ececec')
ventana.resizable(False, False)

#etiqueta y entrada para el valor a convertir
tk.Label(ventana, text="Valor a convertir: ").grid(column=0, row=0, padx=10, pady=10)
entrada_valor = tk.Entry(ventana, width=20)
entrada_valor.grid(column=1, row=0, padx=10, pady=10)

#Comobobox para seleccionar la categoria de conversion
tk.Label(ventana, text='Categoria: ').grid(column=0, row=1, padx=10, pady=10)
categorias = ["peso", "distancia", "temperatura"]
combo_categoria = ttk.Combobox(ventana, values=categorias)
combo_categoria.grid(column=1, row=1, padx=10, pady=10)

#combobox para seleccionar la unidad de origen y destino
tk.Label(ventana, text="De: ").grid(column=0, row=2, padx=10, pady=10)
combo_origen = ttk.Combobox(ventana)
combo_origen.grid(column=1, row=2, padx=10, pady=10)

tk.Label(ventana, text="A: ").grid(column=0, row=3, padx=10, pady=10)
combo_destino = ttk.Combobox(ventana)
combo_destino.grid(column=1, row=3, padx=10, pady=10)

#etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="", font=("Arial", 14))
resultado.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

#listas de converciones
unidades_peso = ["Kilogramos", "Libras", "Arrobas", "Quintales"]
factores_peso = [1, 2.20462, 0.0685714, 0.01]#Factores para convertir a kilogramos

unidades_distancia = ["Metros", "yardas", "Kilometros", "Millas"]
factores_distancia = [1, 1.09361, 0.001, 0.000621371]#Factores para convertir a metros


unidades_temperatura = ["Celsius", "Fahrenheit", "Kelvin"]

#Funcion para actualizar las bunidades basadas en la categoria seleccionada

def actualizar_unidades(event):
    categoria = combo_categoria.get()
    if categoria == "peso":
        combo_origen['values'] = unidades_peso
        combo_destino['values'] = unidades_peso
    elif categoria == "Distancia":
        combo_origen['values'] = unidades_distancia
        combo_destino['values'] = unidades_distancia
    elif categoria == "Temperatura":
        combo_origen['values'] = unidades_temperatura
        combo_destino['values'] = unidades_temperatura
        
#Asociar la funcion de actualizacion al cambio de seleccion en la categoria
combo_categoria.bind("<<ComboboxSelected>>", actualizar_unidades)

#Funciion para realizar la conversion 
def convertir():
    valor = float(entrada_valor.get())
    origen = combo_origen.get()
    destino = combo_destino.get()
    categoria = combo_categoria.get()
    resultado_texto = ""
    
    if categoria == "Peso":
        indice_origen = unidades_peso.index(origen)
        indice_destino = unidades_peso.index(destino)
        valor_en_kg = valor / factores_peso[indice_origen]
        valor_convertido = valor_en_kg * factores_peso[indice_destino]
        resultado_texto = f"{valor} {origen} = {valor_convertido:.2f} {destino}"
        
    elif categoria == "Distancia":
        indice_origen = unidades_distancia.index(origen)
        indice_destino = unidades_distancia.index(destino)
        valor_en_metros = valor / factores_distancia[indice_origen]
        valor_convertido = valor_en_metros * factores_distancia[indice_destino]
        resultado_texto = f"{valor} {origen} = {valor_convertido:.2f} {destino}"
    
    elif categoria == "Temperatura":
        if origen == "Celsius":
            if destino == "Fahrenheit":
                valor_convertido = valor * 9/5 + 32
            elif destino == "Kelvin":
                valor_convertido = valor + 273.15
            else:
                valor_convertido = valor
              
        elif origen == "Fahrenheint":
            if origen == "Celsius":
                valor_convertido = (valor - 32) * 5/9
            elif destino == "Kelvin":
                valor_convertido = (valor - 32) * 5/9 + 273.15
            else:
                valor_convertido = valor
            
        elif origen == "Kelvin":
            if origen == "Celsius":
                valor_convertido = valor - 273.15
            elif destino == "Kelvin":
                valor_convertido = (valor - 273.15) * 9/5 + 32
            else:
                valor_convertido = valor
                
        resultado_texto = f"{valor} {origen} = {valor_convertido:.2f} {destino}"    
    
    resultado.config(text=resultado_texto)
        
#Boton para realizar la conversion
boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

ventana.mainloop()