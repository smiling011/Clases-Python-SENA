# dentificar el dispositivo Bluetooth
# Usa Python para escanear dispositivos Bluetooth cercanos y obtener la dirección del SC-AKX57.

# Código para escanear dispositivos Bluetooth:

import asyncio
from bleak import BleakScanner

async def escanear_dispositivos():
    print("Escaneando dispositivos Bluetooth...")
    dispositivos = await BleakScanner.discover()
    for dispositivo in dispositivos:
        print(f"Nombre: {dispositivo.name}, Dirección: {dispositivo.address}")

# Ejecutar la función de escaneo
asyncio.run(escanear_dispositivos())

# Resultado esperado:
# Encuentra el dispositivo SC-AKX57 y anota su dirección Bluetooth (algo como XX:XX:XX:XX:XX:XX).