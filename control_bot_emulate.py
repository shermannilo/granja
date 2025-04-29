import subprocess
import json
import os


def cargar_base_de_datos():
    registros = set()
    if os.path.exists("emuladores.txt"):
        with open("emuladores.txt", "r") as file:
            for line in file:
                registros.add(line.strip())
    return registros

def guardar_instalacion(app, emulator):
    with open("emuladores.txt", "a") as file:
        file.write(f"{app} installed on {emulator}\n")

def instalar_apk(emuladors, apk_name, dt, registros):
    for emulator in emuladors:
        print(f"\n📲 Instalando en {emulator}:")
        registro_clave = f"{apk_name} installed on {emulator}"
        
        if registro_clave in registros:
            print(f"✅ {apk_name} ya estaba instalada en {emulator}. Se omite.")
            continue
        
        path = dt[apk_name].strip('"')
        print(f"Instalando {apk_name} desde {path}...")
        resultado = subprocess.run(["adb", "-s", emulator, "install", path], capture_output=True, text=True)
        
        if "Success" in resultado.stdout:
            print(f"✅ {apk_name} instalada correctamente en {emulator}.")
            guardar_instalacion(apk_name, emulator)
        else:
            print(f"❌ Error instalando {apk_name} en {emulator}:\n{resultado.stdout}\n{resultado.stderr}")

    print("\n🚀 Instalación finalizada.")
    print("--------------------------------------------------")

   
