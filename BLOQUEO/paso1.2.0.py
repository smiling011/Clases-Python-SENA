import bluetooth

print("Escaneando dispositivos Bluetooth clásicos...")
dispositivos = bluetooth.discover_devices(duration=8, lookup_names=True)

for addr, name in dispositivos:
    print(f"Dirección: {addr}, Nombre: {name}")
