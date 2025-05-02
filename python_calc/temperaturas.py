import tkinter as tk
from tkinter import ttk

#cRear ventana principal
ventana = tk.Tk()
ventana.title('Conversor de temperaturas')
ventana.geometry("640x400")

#Crear etiqueta y entrada para temparatura
etiqueta_temp = tk.Label(ventana, text="Temperatura: ", font=("Arial", 14))
etiqueta_temp.grid(column=0, row=0, padx=10, pady=10)

entrada_temp = tk.Entry(ventana, width=10, font=("Arial", 14))
entrada_temp.grid(column=1, row=0, padx=10, pady=10)

#Crear etiqueta y entrada para el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 14))
etiqueta_resultado.grid(column=0, row=2, padx=10, pady=10)

resultado = tk.Entry(ventana, width=10, font=("Arial", 14))
resultado.grid(column=1, row=2, padx=10, pady=10)

#Opciones de conversion
opcion_origen = tk.StringVar()
opcion_origen.set('Celsius')

opcion_destino = tk.StringVar()
opcion_destino.set('Farenheith')


# crear botone de radio para las opciones origenes 
radio_c = tk.Radiobutton(ventana, text='Celsius', variable=opcion_origen, value='Celsius', font=("Arial", 12))
radio_c.grid(column=0, row=1, padx=10, pady=10)

radio_f = tk.Radiobutton(ventana, text='Farenheith', variable=opcion_origen, value='Farenheith', font=("Arial", 12))
radio_f.grid(column=1, row=1, padx=10, pady=10)

radio_k = tk.Radiobutton(ventana, text='Kelvin', variable=opcion_origen, value='Kelvin', font=("Arial", 12))
radio_k.grid(column=2, row=1, padx=10, pady=10)


# crear botones de radio para las opciones destino
radio_c_dest = tk.Radiobutton(ventana, text='Celsius', variable=opcion_destino, value='Celsius', font=("Arial", 12))
radio_c_dest.grid(column=0, row=3, padx=10, pady=10)

radio_f_dest = tk.Radiobutton(ventana, text='Farenheith', variable=opcion_destino, value='Farenheith', font=("Arial", 12))
radio_f_dest.grid(column=1, row=3, padx=10, pady=10)

radio_k_dest = tk.Radiobutton(ventana, text='Kelvin', variable=opcion_destino, value='Kelvin', font=("Arial", 12))
radio_k_dest.grid(column=2, row=3, padx=10, pady=10)

# Logica al presionar el boton de conversion
def convertir():
    temp = entrada_temp.get()
    if temp:
        temp = float(temp)
        origen = opcion_origen.get()
        destino = opcion_destino.get()
        
        if origen == "Celsius":
            if destino == "Celsius":
                temp_result = temp
            elif destino == "Farenheith":
                temp_result = (temp * 9/5) + 32
            elif destino == "Kelvin":
                temp_result = temp + 273.15
        elif origen == "Farenheith":
            if destino == "Celsius":
                temp_result = (temp - 32) * 5/9
            elif destino == "Farenheith":
                temp_result = temp
            elif destino == "Kelvin":
                temp_result = (temp - 32 ) * 5/9 + 273.15
        elif origen == "Kelvin":
            if destino == "Celsius":
                temp_result = temp - 273.15
            elif destino == "Farenheith":
                temp_result = (temp - 273.15) * 9/5 + 32
            elif destino == "Kelvin":
                temp_result = temp
        
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, str(temp_result))
        
# Boton para realizar la conversion
boton_convertir = ttk.Button(ventana, text='Convertir', command=convertir)
boton_convertir.grid(column=0, row=4, columnspan=3, pady=10) 

 
ventana.mainloop() 