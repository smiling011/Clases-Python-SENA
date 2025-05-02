import tkinter as tk
from tkinter import ttk


#crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("520x520")
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)
ventana.columnconfigure(4, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1) 
# Crear la entrada
entrada = tk.Entry(ventana, width=20, font=("Arial", 24), justify=tk.RIGHT)
entrada.grid(column=0,row=0, columnspan=4, pady=10)
#Funcion para catualizar entrada
def actualizar_entrada(texto):
    entrada.insert(tk.END, texto)
    
def evaluar():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
#funcion para limpiar la entrada
def limmpiar():
    entrada.delete(0, tk.END)
    
#botones d ela calculadora
boton_1 = ttk.Button(ventana, text='1', command=lambda: actualizar_entrada('1'))
boton_1.grid(column=0, row=1, sticky='nsew')
boton_2 = ttk.Button(ventana, text='2', command=lambda: actualizar_entrada('2'))
boton_2.grid(column=1, row=1, sticky='nsew')
boton_3 = ttk.Button(ventana, text='3', command=lambda: actualizar_entrada('3'))
boton_3.grid(column=2, row=1, sticky='nsew')

boton_mas = ttk.Button(ventana, text='Suma (+)', command=lambda: actualizar_entrada('+'))
boton_mas.grid(column=3, row=1, sticky='nsew')

boton_4 = ttk.Button(ventana, text='4', command=lambda: actualizar_entrada('4'))
boton_4.grid(column=0, row=2, sticky='nsew')
boton_5 = ttk.Button(ventana, text='5', command=lambda: actualizar_entrada('5'))
boton_5.grid(column=1, row=2, sticky='nsew')
boton_6 = ttk.Button(ventana, text='6', command=lambda: actualizar_entrada('6'))
boton_6.grid(column=2, row=2, sticky='nsew')

boton_menos = ttk.Button(ventana, text='Resta (-)', command=lambda: actualizar_entrada('-'))
boton_menos.grid(column=3, row=2, sticky='nsew')

boton_7 = ttk.Button(ventana, text='7', command=lambda: actualizar_entrada('7'))
boton_7.grid(column=0, row=3, sticky='nsew')
boton_8 = ttk.Button(ventana, text='8', command=lambda: actualizar_entrada('8'))
boton_8.grid(column=1, row=3, sticky='nsew')
boton_9 = ttk.Button(ventana, text='9', command=lambda: actualizar_entrada('9'))
boton_9.grid(column=2, row=3, sticky='nsew')

boton_por = ttk.Button(ventana, text='Multiplicacion (*)', command=lambda: actualizar_entrada('*'))
boton_por.grid(column=3, row=3, sticky='nsew')

boton_0 = ttk.Button(ventana, text='0', command=lambda: actualizar_entrada('0'))
boton_0.grid(column=1, row=4, sticky='nsew')

boton_div = ttk.Button(ventana, text='Divison (/)', command=lambda: actualizar_entrada('/'))
boton_div.grid(column=3, row=4, sticky='nsew')

boton_punto = ttk.Button(ventana, text='.', command=lambda: actualizar_entrada('.'))
boton_punto.grid(column=2, row=4, sticky='nsew')

boton_igual = ttk.Button(ventana, text='=', command=evaluar)
boton_igual.grid(column=0, row=6, columnspan=4, sticky='nsew')

boton_abrir_parentesis = ttk.Button(ventana, text='(', command=lambda: actualizar_entrada('('))
boton_abrir_parentesis.grid(column=0, row=5, columnspan=2, sticky='nsew')

boton_cerrar_parentesis = ttk.Button(ventana, text=')', command=lambda: actualizar_entrada(')'))
boton_cerrar_parentesis.grid(column=2, row=5, columnspan=2, sticky='nsew')

boton_limpiar = ttk.Button(ventana, text='Limpiar', command=limmpiar)
boton_limpiar.grid(column=0, row=4, sticky='nsew')

ventana.mainloop()