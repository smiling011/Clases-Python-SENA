# Desconectar dispositivos conectados
# Una vez que hayas identificado la característica que controla las conexiones Bluetooth:

# Encuentra el UUID de la característica relevante.
# Envía el comando para desconectar.
# Código para desconectar dispositivos:

async def desconectar_dispositivo():
    async with BleakClient(device_address) as client:
        if client.is_connected:
            # Reemplaza con la UUID de la característica que controla el Bluetooth
            uuid_caracteristica = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
            comando_desconectar = b'\x00'  # Comando para desconectar (ajusta según el dispositivo)
            await client.write_gatt_char(uuid_caracteristica, comando_desconectar)
            print("Dispositivo desconectado.")
        else:
            print("No se pudo conectar al dispositivo.")

asyncio.run(desconectar_dispositivo())
