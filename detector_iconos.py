import cv2
import json
import os

def detectar_icono(nombre_emulador, nombre_apk):
    # 1. Ruta del ícono a usar como plantilla
    ruta_icono = f"captura/iconos/{nombre_apk}.png"
    ruta_captura = f"captura/{nombre_emulador}_screenshot.png"
    if not os.path.exists(ruta_icono):
        print(f"❌ No se encontró el ícono '{ruta_icono}'.")
        return

    if not os.path.exists(ruta_captura):
        print(f"❌ No se encontró la captura '{ruta_captura}'.")
        return

    # 2. Crear carpeta para guardar resultados si no existe
    if not os.path.exists("iconos_detectados"):
        os.makedirs("iconos_detectados")

    # 3. Cargar imágenes con OpenCV
    captura = cv2.imread(ruta_captura)
    icono = cv2.imread(ruta_icono)

    if captura is None or icono is None:
        print("❌ Error al cargar las imágenes.")
        return

    # 4. Hacer Template Matching
    resultado = cv2.matchTemplate(captura, icono, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

    umbral = 0.8  # Umbral de coincidencia (ajustable)

    if max_val < umbral:
        print(f"⚠️ Coincidencia insuficiente ({max_val:.2f}). No se detectó {nombre_apk}.")
        return

    # 5. Obtener coordenadas del ícono detectado
    x, y = max_loc
    h, w = icono.shape[:2]
    print(f"✅ {nombre_apk} detectado en {nombre_emulador} en posición: ({x}, {y}) con {max_val:.2f} de confianza")

    # 6. Recortar y guardar imagen del ícono detectado
    recorte = captura[y:y+h, x:x+w]
    nombre_archivo = f"iconos_detectados/{nombre_apk}_{nombre_emulador}.png"
    cv2.imwrite(nombre_archivo, recorte)
    print(f"🖼️ Recorte guardado en: {nombre_archivo}")

    # 7. Registrar coordenadas en JSON
    json_path = "registro_iconos.json"
    if os.path.exists(json_path):
        with open(json_path, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    if nombre_emulador not in data:
        data[nombre_emulador] = {}

    data[nombre_emulador][nombre_apk] = {"x": x+100, "y": y+100}# falta ajustar la salida de coordenadas por la terminal 
    #pero esta es la importante 

    with open(json_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"📝 Coordenadas registradas en {json_path}")


def detectar_todos_iconos(nombre_apk):
    ruta_icono = f"captura/iconos/{nombre_apk}.png"
    if not os.path.exists(ruta_icono):
        print(f"❌ No se encontró el ícono '{ruta_icono}'.")
        return
# aqui uno se queda vacio jajaj es increible lo que da pensar un poco .
    archivos = [f for f in os.listdir("captura") if f.endswith("_screenshot.png")]
    for archivo in archivos:
        nombre_emulador = archivo.replace("_screenshot.png", "")
        detectar_icono(nombre_emulador, nombre_apk)