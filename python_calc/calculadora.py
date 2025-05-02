#Te amo muchooooooooooooo mi amor :3
#Libreria tk
import tkinter as tk 
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("520x520")

#Columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)
ventana.columnconfigure(4, weight=1)

#Filas
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1)

#Creacion de la entrada
entrada = tk.Entry(ventana, width=20, font=("Arial", 24), justify=tk.RIGHT)
entrada.grid(column=0, row=0, columnspan=4, pady=10)

#(funcion) Actualizar entrada de texto 
def actualizar_entrada(texto):
    entrada.insert(tk.END, texto)
    
    
#Metodo que se encarga de realizar operaciones
def evaluar():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
        
        
#Metodo para limpiar entrada
def limpiar():
    entrada.delete(0, tk.END)
    
#Botones de la calculadora
#Numeros 1,2,3
boton_1 = ttk.Button(ventana, text= "1", command=lambda: actualizar_entrada("1"))
boton_1.grid(column=0, row=1, sticky="nsew")

boton_2 = ttk.Button(ventana, text= "2", command=lambda: actualizar_entrada("2"))
boton_2.grid(column=1, row=1, sticky="nsew")

boton_3 = ttk.Button(ventana, text= "3", command=lambda: actualizar_entrada("3"))
boton_3.grid(column=2, row=1, sticky="nsew")

#Suma
boton_mas = ttk.Button(ventana, text="suma (+)", command=lambda: actualizar_entrada("+"))
boton_mas.grid(column=3, row=1, sticky="nsew")

#Numeros 4,5,6
boton_4 = ttk.Button(ventana, text= "4", command=lambda: actualizar_entrada("4"))
boton_4.grid(column=0, row=2, sticky="nsew")

boton_5 = ttk.Button(ventana, text= "5", command=lambda: actualizar_entrada("5"))
boton_5.grid(column=1, row=2, sticky="nsew")

boton_6 = ttk.Button(ventana, text= "6", command=lambda: actualizar_entrada("6"))
boton_6.grid(column=2, row=2, sticky="nsew")

#Resta
boton_menos = ttk.Button(ventana, text="resta (-)", command=lambda: actualizar_entrada("-"))
boton_menos.grid(column=3, row=2, sticky="nsew")

#Numeros 7,8,9
boton_7 = ttk.Button(ventana, text= "7", command=lambda: actualizar_entrada("7"))
boton_7.grid(column=0, row=3, sticky="nsew")

boton_8 = ttk.Button(ventana, text= "8", command=lambda: actualizar_entrada("8"))
boton_8.grid(column=1, row=3, sticky="nsew")

boton_9 = ttk.Button(ventana, text= "9", command=lambda: actualizar_entrada("9"))
boton_9.grid(column=2, row=3, sticky="nsew")

#Multiplicacion
boton_por = ttk.Button(ventana, text="multiplicacion (*)", command=lambda: actualizar_entrada("*"))
boton_por.grid(column=3, row=3, sticky="nsew")

#Numero 0
boton_0 = ttk.Button(ventana, text= "0", command=lambda: actualizar_entrada("0"))
boton_0.grid(column=1, row=4, sticky="nsew")

#Division
boton_div = ttk.Button(ventana, text="division (/)", command=lambda: actualizar_entrada("/"))
boton_div.grid(column=3, row=4, sticky="nsew")




#Punto para decimales
boton_punto = ttk.Button(ventana, text= ".", command=lambda: actualizar_entrada("."))
boton_punto.grid(column=2, row=4, sticky="nsew")

#Boton igual
boton_igual = ttk.Button(ventana, text= "=", command=evaluar)
boton_igual.grid(column=0, row=6, columnspan=4, sticky="nsew")

#Parentesis
boton_abrir_parentesis = ttk.Button(ventana, text= "(", command=lambda: actualizar_entrada("("))
boton_abrir_parentesis.grid(column=0, row=5, columnspan=2, sticky="nsew")

boton_cerrar_parentesis = ttk.Button(ventana, text= ")", command=lambda: actualizar_entrada(")"))
boton_cerrar_parentesis.grid(column=2, row=5, columnspan=2, sticky="nsew")

#Crear variable para boton limpiar
boton_limpiar = ttk.Button(ventana, text= "Limpiar", command=limpiar)
boton_limpiar.grid(column=0, row=4, sticky="nsew")

#Lanzar la ventana
ventana.mainloop()


