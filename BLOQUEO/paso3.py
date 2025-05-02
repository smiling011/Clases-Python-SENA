# Descubrir Servicios y Características
# Los dispositivos Bluetooth ofrecen servicios y características para el control. Necesitamos identificar cuáles están disponibles en el SC-AKX57.

# Código para listar servicios y características:

async def listar_servicios():
    async with BleakClient(device_address) as client:
        if client.is_connected:
            print("Servicios y características disponibles:")
            servicios = await client.get_services()
            for servicio in servicios:
                print(f"Servicio: {servicio.uuid}")
                for caracteristica in servicio.characteristics:
                    print(f"  Característica: {caracteristica.uuid}, Propiedades: {caracteristica.properties}")

asyncio.run(listar_servicios())


# Resultado esperado:
# Obtendrás una lista de servicios (UUIDs) y características. 
# Busca una que esté relacionada con la conectividad Bluetooth o el control del dispositivo.