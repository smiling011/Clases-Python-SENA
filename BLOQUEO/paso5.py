# Bloquear el Bluetooth
# Si el SC-AKX57 soporta desactivar Bluetooth mediante comandos:

# Usa el mismo enfoque del paso anterior.
# Encuentra la característica correspondiente para desactivar Bluetooth.
# Código para desactivar el Bluetooth:

async def bloquear_bluetooth():
    async with BleakClient(device_address) as client:
        if client.is_connected:
            # Reemplaza con la UUID correcta
            uuid_caracteristica = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
            comando_bloqueo = b'\x01'  # Comando para desactivar Bluetooth
            await client.write_gatt_char(uuid_caracteristica, comando_bloqueo)
            print("Bluetooth desactivado en el SC-AKX57.")
        else:
            print("No se pudo conectar al dispositivo.")

asyncio.run(bloquear_bluetooth())
