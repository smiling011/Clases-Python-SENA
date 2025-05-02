# Conectar al SC-AKX57
# Confirma que puedes conectarte al equipo. Usa la dirección Bluetooth obtenida en el paso anterior.

# Código para probar la conexión:
from bleak import BleakClient

# Reemplaza con la dirección del SC-AKX57
device_address = "67:E1:23:31:37:28"

async def conectar_dispositivo():
    async with BleakClient(device_address) as client:
        if client.is_connected:
            print("Conectado al SC-AKX57.")
        else:
            print("No se pudo conectar al dispositivo.")

# Ejecutar la función de conexión
import asyncio
asyncio.run(conectar_dispositivo())
