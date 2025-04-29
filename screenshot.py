import subprocess as sp
import os 
import time as t
import gestos as ge
import cv2

if not os.path.exists("captura"):
    os.mkdir("captura")
    print(f"Carpeta '{"captura"}' creada.")
else:
    print(f"La carpeta '{"captura"}' ya existe.")

# Definir la función para tomar la captura de pantalla
def tomar_captura(emulador):
    #jajjaj no se como funciona(si se) entra un emulador y recorre cada palabra pero al final hace lo que debe hacer asi
    #que el codigo no se toca 
    for e in emulador:# esto solo toma capturas a las apk instaladas en el emulador si estamos desde main menu 
        #Pero hay solucion a todo 
       
        # Tomar la captura de pantalla
        sp.run(["adb", "-s", e, "shell", "screencap", "-p", "/sdcard/screenshot.png"])
        
        # Descargar la captura de pantalla al directorio actual
        sp.run(["adb", "-s", e, "pull", "/sdcard/screenshot.png", f"captura/{e}_screenshot.png"])
        
        # Eliminar la captura de pantalla del emulador
        sp.run(["adb", "-s", e, "shell", "rm", "/sdcard/screenshot.png"])
        
        print(f"Captura de pantalla guardada como {e}_screenshot.png en la carpeta 'captura'.")
        # Esperar un segundo antes de tomar la siguiente captura  en caso de que no funcione el pull
        #t.sleep(1)  

def tomar_video(emulador, tiempo):
    for e in emulador:
        # Iniciar la grabación de pantalla
        sp.run(["adb", "-s", e, "shell", "screenrecord", "--time-limit", str(tiempo), "/sdcard/screenrecord.mp4"])
        
        # Descargar el video al directorio actual
        sp.run(["adb", "-s", e, "pull", "/sdcard/screenrecord.mp4", f"captura/videos/{e}_screenrecord.mp4"])
        
        # Eliminar el video del emulador
        sp.run(["adb", "-s", e, "shell", "rm", "/sdcard/screenrecord.mp4"])
        print(f"Video guardado como {e}_screenrecord.mp4 en la carpeta 'captura/videos'.")
    



def identificar_pantalla():
    emuladores = ge.obtener_emuladores_activos()
    tomar_captura(emuladores)  # Captura actual de todos los emuladores

    resultado = {}

    for nombre_emulador in emuladores:
        ruta_captura = f"captura/{nombre_emulador}_screenshot.png"
        if not os.path.exists(ruta_captura):
            print(f"❌ No se encontró la captura para {nombre_emulador}")
            resultado[nombre_emulador] = "captura_no_encontrada"
            continue

        captura = cv2.imread(ruta_captura)
        if captura is None:
            print(f"❌ No se pudo leer la imagen para {nombre_emulador}")
            resultado[nombre_emulador] = "error_lectura"
            continue

        mejor_valor = 0
        mejor_nombre = "desconocida"

        for plantilla_archivo in os.listdir("pantallas_referencia"):
            if not plantilla_archivo.endswith(".png"):
                continue

            ruta_plantilla = os.path.join("pantallas_referencia", plantilla_archivo)
            plantilla = cv2.imread(ruta_plantilla)

            if plantilla is None or captura.shape[0] < plantilla.shape[0] or captura.shape[1] < plantilla.shape[1]:
                continue

            resultado_match = cv2.matchTemplate(captura, plantilla, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(resultado_match)

            if max_val > mejor_valor:
                mejor_valor = max_val
                mejor_nombre = plantilla_archivo.replace(".png", "")

        print(f"🧭 {nombre_emulador} está en: {mejor_nombre} (confianza: {mejor_valor:.2f})")
        resultado[nombre_emulador] = mejor_nombre

    return resultado

tomar_captura(ge.obtener_emuladores_activos())  # Captura actual de todos los emuladores