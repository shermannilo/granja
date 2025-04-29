from openai import OpenAI
import os
import base64
import json
from dotenv import load_dotenv
from PIL import Image

#Esto esta hecho solo para que observen el dominio de una api y el uso de .env para guardar la api key
# y el uso de la libreria openai para interactuar con la api de gpt-4
#funciona el codigo pero no el mathcing de imagenes porque no esta entrenado para eso
#se puede usar para letras o cosas que no sean iconos de aplicaciones

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

def recortar_icono(imagen_path, coords, nombre_icono_salida):
    img = Image.open(imagen_path)
    x, y, w, h = coords["x"], coords["y"], coords["w"], coords["h"]
    icono = img.crop((x, y, x + w, y + h))
    icono.save(nombre_icono_salida)
    print(f"📸 Icono guardado como: {nombre_icono_salida}")

def detectar_apk_con_gpt(emulador, apk, carpeta="captura", salida="deteccion_gpt.json", carpeta_iconos_recortados="iconos_detectados"):
    imagen_path = os.path.join(carpeta, f"{emulador}_screenshot.png")
    if not os.path.exists(imagen_path):
        print(f"❌ Captura no encontrada: {imagen_path}")
        return

    if not os.path.exists(carpeta_iconos_recortados):
        os.makedirs(carpeta_iconos_recortados)

    imagen_base64 = encode_image_to_base64(imagen_path)

    prompt = f"""
    Observa esta captura de pantalla de un emulador Android. 
    ¿Puedes decirme si ves el ícono de la aplicación '{apk}'?
    Si sí, dime las coordenadas (x, y) de la esquina superior izquierda del ícono, su ancho y su alto.
    Responde solo con un JSON así: {{"apk": "instagram", "x": 100, "y": 200, "w": 150, "h": 150}}
    Si no lo ves, responde: null
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": [
                    { "type": "text", "text": prompt },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{imagen_base64}"
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    respuesta = response.choices[0].message.content.strip()
    print(f"📍 Respuesta de GPT: {respuesta}")

    try:
        resultado = json.loads(respuesta)
    except json.JSONDecodeError:
        resultado = None

    if os.path.exists(salida):
        with open(salida, "r") as f:
            data = json.load(f)
    else:
        data = {}

    if resultado:
        if emulador not in data:
            data[emulador] = []
        data[emulador].append(resultado)
        with open(salida, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Coordenadas guardadas en {salida}")

        nombre_icono = os.path.join(carpeta_iconos_recortados, f"icono_{apk}_{emulador}.png")
        recortar_icono(imagen_path, resultado, nombre_icono)
    else:
        print(f"❌ No se detectó la app {apk} en {emulador}")

