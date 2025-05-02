import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular_costo():
    try:
        plato_principal = variable_plato.get()
        ingrediente = variable_ingrediente.get()
        cantidad = int(entrada_cantidad.get())

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número entero positivo.")

        costo_base = precios_platos[plato_principal]
        costo_extra = precios_ingredientes.get(ingrediente, 0)  # 0 si no se selecciona ingrediente
        costo_subtotal = (costo_base + costo_extra) * cantidad
        impuesto = costo_subtotal * 0.19
        costo_total = costo_subtotal + impuesto

        etiqueta_resultado.config(text=f"Costo total: ${costo_total:.2f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Datos del restaurante (puedes personalizarlos)
precios_platos = {
    "Pizza": 15000,
    "Pollo": 12000,
    "Hamburguesa": 10000,
    "Pasta": 18000,
    "Perro": 8000,
}

precios_ingredientes = {
    "Queso extra": 2000,
    "Tocineta extra": 3000,
    "Ensalada": 3500,
    "Papas a la francesa": 4000,
}

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Costo de Pedido")

# Menú desplegable para platos principales
tk.Label(ventana, text="Plato principal:").grid(row=0, column=0, padx=5, pady=5)
variable_plato = tk.StringVar(ventana)
variable_plato.set("Pizza")  # Valor por defecto
menu_platos = tk.OptionMenu(ventana, variable_plato, *precios_platos.keys())
menu_platos.grid(row=0, column=1, padx=5, pady=5)

# Menú desplegable para ingredientes
tk.Label(ventana, text="Ingrediente extra:").grid(row=1, column=0, padx=5, pady=5)
variable_ingrediente = tk.StringVar(ventana)
variable_ingrediente.set("")  # Valor por defecto (ninguno)
menu_ingredientes = tk.OptionMenu(ventana, variable_ingrediente, "", *precios_ingredientes.keys())
menu_ingredientes.grid(row=1, column=1, padx=5, pady=5)

# Entrada para cantidad
tk.Label(ventana, text="Cantidad:").grid(row=2, column=0, padx=5, pady=5)
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.grid(row=2, column=1, padx=5, pady=5)

# Botón de calcular
boton_calcular = ttk.Button(ventana, text="Calcular", command=calcular_costo)
boton_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
