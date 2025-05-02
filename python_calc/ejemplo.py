import tkinter as tk
from tkinter import messagebox

platos = {
    "Pizza": 3000,
    "Pollo": 10000,
    "Hamburguesa": 10000,
    "Pasta": 35000,
    "Perro": 5000
}

ingredientes = {
    "Ninguno": 0,
    "Porción adicional de queso": 2000,
    "Porción adicional de tocineta": 3000,
    "Ensalada": 2500,
    "Papas a la francesa": 2500
}

def actualizar_campos(*args):
    pass

def calcular_costo():
    try:
        cantidad = int(entrada_cantidad.get())
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida (entero positivo).")
        return

    plato = variable_plato.get()
    ingrediente = variable_ingrediente.get()
    cantidad_ing = entrada_cantidad_ing.get()
    
    costo_base = platos[plato] * cantidad
    costo_ingrediente = ingredientes[ingrediente] * cantidad
    subtotal = costo_base + costo_ingrediente
    impuesto = subtotal * 0.19
    total = subtotal + impuesto
    
    etiqueta_resultado.config(text=f"Subtotal: ${subtotal:.2f}\nImpuesto (19%): ${impuesto:.2f}\nTotal: ${total:.2f}")


ventana = tk.Tk()
ventana.title("Calculadora de Costo de Pedido")


variable_plato = tk.StringVar(ventana)
variable_ingrediente = tk.StringVar(ventana)
variable_plato.set(list(platos.keys())[0])
variable_ingrediente.set(list(ingredientes.keys())[0])


tk.Label(ventana, text="Seleccione el plato principal:").grid(row=0, column=0, padx=10, pady=10)
plato_menu = tk.OptionMenu(ventana, variable_plato, *platos.keys(), command=actualizar_campos)
plato_menu.grid(row=0, column=1, padx=10, pady=10)


tk.Label(ventana, text="Seleccione un ingrediente adicional:").grid(row=1, column=0, padx=10, pady=10)
ingrediente_menu = tk.OptionMenu(ventana, variable_ingrediente, *ingredientes.keys(), command=actualizar_campos)
ingrediente_menu.grid(row=1, column=1, padx=10, pady=10)


tk.Label(ventana, text="Cantidad de platos:").grid(row=2, column=0, padx=10, pady=10)
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="Cantidad de ingredientes:").grid(row=3, column=0, padx=10, pady=10)
entrada_cantidad_ing = tk.Entry(ventana)
entrada_cantidad_ing.grid(row=3, column=1, padx=10, pady=10)


boton_calcular = tk.Button(ventana, text="Calcular Costo", command=calcular_costo)
boton_calcular.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
