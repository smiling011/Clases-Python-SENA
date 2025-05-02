import tkinter as tk
from tkinter import ttk
#Entrada
ventana = tk.Tk()
ventana.title("Calculadora Unidades Monetarias, Tiempo y de Almacenamiento de Datos")
ventana.geometry('800x300')
ventana.configure(background='#ececec')
ventana.resizable(False, False)

#edicion 
tk.Label(ventana, text="Valor a convertir:").grid(column=0, row=0, padx=10, pady=10)
entrada_valor = tk.Entry(ventana, width=24)
entrada_valor.grid(column=1, row=0, padx=10, pady=10)


tk.Label(ventana, text="Categoría:").grid(column=0, row=1, padx=10, pady=10)
categorias = ["Unidades Monetarias", "Unidades de Tiempo", "Unidades de Almacenamiento de Datos"]
combo_categoria = ttk.Combobox(ventana, values=categorias)
combo_categoria.grid(column=1, row=1, padx=10, pady=10)


tk.Label(ventana, text="De:").grid(column=0, row=2, padx=10, pady=10)
combo_origen = ttk.Combobox(ventana)
combo_origen.grid(column=1, row=2, padx=10, pady=10)

tk.Label(ventana, text="A:").grid(column=0, row=3, padx=10, pady=10)
combo_destino = ttk.Combobox(ventana)
combo_destino.grid(column=1, row=3, padx=10, pady=10)


resultado = tk.Label(ventana, text="", font=("Arial", 14))
resultado.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

#para elejir el proceso
unidades_monetario = ["Dólares (USD)", "Pesos (COP)", "Euros (EUR)", "Libras Esterlinas(GBP)", "Yenes (JPY)"]
factores_monetario = [1, 4164,25, 0.93, 0.79, 158.02]  

unidades_tiempo = ["Segundos (SEG)", "Minutos (MIN)", "Horas (HOR)", "Días(DIA)"]
factores_tiempo = [60, 1, 60, 24]  

unidades_dato = ["Bytes (B)", "Kilobyites (KB)", "Megabytes (MB)", "Terabytes (TB)"]
factores_dato = [1, 1024, 1048576, 1099511627776]


def actualizar_unidades(event):
    categoria = combo_categoria.get()
    if categoria == "Unidades Monetarias":
        combo_origen['values'] = unidades_monetario
        combo_destino['values'] = unidades_monetario
    elif categoria == "Unidades de Tiempo":
        combo_origen['values'] = unidades_tiempo
        combo_destino['values'] = unidades_tiempo
    elif categoria == "Unidades de Almacenamiento de Datos":
        combo_origen['values'] = unidades_dato
        combo_destino['values'] = unidades_dato


combo_categoria.bind("<<ComboboxSelected>>", actualizar_unidades)

#proceso
def convertir():
    try:
        valor = float(entrada_valor.get())
    except ValueError:
        resultado.config(text="Por favor, ingrese un valor numérico.")
        return
    
    origen = combo_origen.get()
    destino = combo_destino.get()
    if not origen or not destino:
        resultado.config(text="Por favor, seleccione las unidades de origen y destino.")
        return

    categoria = combo_categoria.get()
    resultado_texto = ""

    if categoria == "Unidades Monetarias":
        if origen not in unidades_monetario or destino not in unidades_monetario:
            resultado.config(text="Unidad Monetaria no válida.")
            return
        indice_origen = unidades_monetario.index(origen)
        indice_destino = unidades_monetario.index(destino)
        valor_en_moneda = valor / factores_monetario[indice_origen]
        valor_convertido = valor_en_moneda * factores_monetario[indice_destino]
        resultado_texto = f"{valor} {origen} = {valor_convertido:.4f} {destino}"
    
    elif categoria == "Unidades de Tiempo":
        if origen not in unidades_tiempo or destino not in unidades_tiempo:
            resultado.config(text="Unidad de distancia no válida.")
            return
        indice_origen = unidades_tiempo.index(origen)
        indice_destino = unidades_tiempo.index(destino)
        valor_en_metros = valor / factores_tiempo[indice_origen]
        valor_convertido = valor_en_metros * factores_tiempo[indice_destino]
        resultado_texto = f"{valor} {origen} = {valor_convertido:.4f} {destino}"
        
    elif categoria == "Unidades de Almacenamiento de Datos":
        if origen not in unidades_dato or destino not in unidades_dato:
            resultado.config(text="Unidad de dato no válida.")
            return
        indice_origen = unidades_dato.index(origen)
        indice_destino = unidades_dato.index(destino)
        valor_en_unidades = valor / factores_dato[indice_origen]
        valor_convertido = valor_en_unidades * factores_dato[indice_destino]
        resultado_texto = f"{valor} {origen} = {valor_convertido:.4f} {destino}"
        
    #mostrar el resultado
    resultado.config(text=resultado_texto)
#botoncito final :)
boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

ventana.mainloop()
#Con mucho esfuerzo lo logre al fin :)
#50 millones el valor de este codigo
#Si necesita a alguien para trabajar con algoritmos llamenme solo pido un sueldo de 30 millones al mes :)
#Hatsune miku iloveu