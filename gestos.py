import json
import subprocess as sp
import os 
import time as t
# hice esto aqui y no en main.py porque no quiero que se repita el codigo. en main va para la actualizacion jajaj 

def obtener_emuladores_activos():
    resultado = sp.run(["adb", "devices"], capture_output=True, text=True)
    lineas = resultado.stdout.strip().split("\n")[1:]
    emuladores = [linea.split("\t")[0] for linea in lineas if "emulator" in linea]
    return emuladores

def escribir(texto,emulador):
    try:
        sp.run(["adb", "-s", emulador, "shell", "input", "text", texto])
        print(f"✍️ Escribiendo '{texto}' en {emulador}")
    except Exception as e:
        print(f"❌ Error escribiendo en {emulador}: {e}")
        
def hacer_tap(en_emulador, x, y):
    try:
        sp.run(["adb", "-s", en_emulador, "shell", "input", "tap", str(x), str(y)])
        print(f"👆 Tap en ({x},{y}) en {en_emulador}")
    except Exception as e:
        print(f"❌ Error haciendo tap en {en_emulador}: {e}")
def normalizar(e):
    #usamos el boton de inicio del emulador para que lleve todos emuladores a la pantalla de inicio
    sp.run(["adb", "-s", e, "shell", "input", "keyevent", "3"])# esto es para el boton de inicio
    # Esperar 2 milisegundos para asegurarse de que la pantalla de inicio esté completamente cargada    
        
    #llevar todos los emuladores a la pantalla de las apks instaladas
    sp.run(["adb", "-s", e, "shell", "input", "swipe", "300", "1500", "300", "1000"])
    # Esperar 2 milisegundos para asegurarse de que la pantalla de inicio esté completamente cargada    
    t.sleep(1)
def procesar_taps_solo_apk(nombre_apk,emulador, path_json="registro_iconos.json"):
    if not os.path.exists(path_json):
        print("❌ No se encontró el archivo de coordenadas.")
        return

    with open(path_json, "r") as file:
        try:
            registros = json.load(file)
        except json.JSONDecodeError:
            print("❌ Error al leer el JSON.")
            return

    emuladores_activos = obtener_emuladores_activos()

    if not emuladores_activos:
        print("⚠️ No hay emuladores ADB activos.")
        return

    print(f"\n🔍 Buscando coordenadas para '{nombre_apk}'...\n")
    
    #for emulador in emuladores_activos:
    if emulador in registros and nombre_apk in registros[emulador]:
        normalizar(emulador)
        coords = registros[emulador][nombre_apk]
        x, y = coords["x"], coords["y"]
        hacer_tap(emulador, x, y)
    else:
        print(f"⚠️ No hay coordenadas guardadas para '{nombre_apk}' en {emulador}.")

