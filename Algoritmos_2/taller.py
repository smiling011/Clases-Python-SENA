import tkinter as tk
from tkinter import ttk, messagebox

# Precios base de los platos principales
platos = {
    "Pizza": 8000,
    "Pollo": 12000,
    "Hamburguesa": 10000,
    "Pasta": 9000,
    "Perro": 7000
}

# Precios de los ingredientes adicionales
ingredientes = {
    "Ninguno": 0,
    "Porción adicional de queso": 2000,
    "Porción adicional de tocineta": 3000,
    "Ensalada": 2500,
    "Papas a la francesa": 1500
}

def calcular_costo():
    try:
        cantidad = int(cantidad_entry.get())
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida (entero positivo).")
        return

    plato = plato_var.get()
    ingrediente = ingrediente_var.get()
    
    costo_base = platos[plato] * cantidad
    costo_ingrediente = ingredientes[ingrediente] * cantidad
    subtotal = costo_base + costo_ingrediente
    impuesto = subtotal * 0.19
    total = subtotal + impuesto
    
    resultado.set(f"Subtotal: ${subtotal:.2f}\nImpuesto (19%): ${impuesto:.2f}\nTotal: ${total:.2f}")


root = tk.Tk()
root.title("Costo de Pedido")


plato_var = tk.StringVar(value=list(platos.keys())[0])
ingrediente_var = tk.StringVar(value=list(ingredientes.keys())[0])
cantidad_var = tk.StringVar()
resultado = tk.StringVar()

# Menú desplegable para seleccionar el plato principal
ttk.Label(root, text="Seleccione el plato principal:").grid(column=0, row=0, padx=10, pady=10, sticky="W")
plato_menu = ttk.OptionMenu(root, plato_var, *platos.keys())
plato_menu.grid(column=1, row=0, padx=10, pady=10, sticky="EW")

# Menú desplegable para seleccionar el ingrediente adicional
ttk.Label(root, text="Seleccione un ingrediente adicional:").grid(column=0, row=1, padx=10, pady=10, sticky="W")
ingrediente_menu = ttk.OptionMenu(root, ingrediente_var, *ingredientes.keys())
ingrediente_menu.grid(column=1, row=1, padx=10, pady=10, sticky="EW")

# Campo de entrada de texto para ingresar la cantidad
ttk.Label(root, text="Cantidad de platos:").grid(column=0, row=2, padx=10, pady=10, sticky="W")
cantidad_entry = ttk.Entry(root, textvariable=cantidad_var)
cantidad_entry.grid(column=1, row=2, padx=10, pady=10, sticky="EW")

# Botón para calcular el costo total
calcular_button = ttk.Button(root, text="Calcular Costo", command=calcular_costo)
calcular_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
resultado_label = ttk.Label(root, textvariable=resultado, font=("Arial", 12))
resultado_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

root.mainloop()