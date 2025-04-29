import apiGPT as gpt
import detector_iconos as dti
import base_datos as db
import control_bot_emulate as emu
import screenshot as sc
import subprocess
import os
import json
import gestos as ge

def add_value():
    resp = input("¿Quieres ver la base de datos? o Escribir un nuevo valor ? type v or a: ").strip().lower()
    if resp == "v":
        db.mostrar_dt()
    elif resp == "a":
        key = input("Ingrese la clave: ").strip()
        value = input("Ingrese el valor: ").strip()
        db.agregar_elemento(key, value)
    else:
        print("Opción no válida. Por favor, ingrese 'v' o 'a'.")

def instalar():
    try:
        with open("dt.json", "r") as file:
            dt = json.load(file)
    except FileNotFoundError:
        print("❌ El archivo dt.json no existe. Crea al menos un registro primero.")
        return
    except json.JSONDecodeError:
        print("❌ El archivo dt.json está corrupto o tiene formato inválido.")
        return

    list_devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    list_devices = list_devices.stdout.strip().split("\n")[1:]
    emuladors = [line.split("\t")[0] for line in list_devices if "emulator" in line]

    if not emuladors:
        print("No se encontraron emuladores. Asegúrese de que los emuladores estén en ejecución.")
    else:
        print("Emuladores encontrados:")
        for emulator in emuladors:
            print(emulator)
        print("--------------------------------------------------")

        x = input("¿Qué apk quieres instalar? o deseas instalar todas las apks?: i o f ").strip().lower()
        if x == "i":
            apk_name = input("Ingrese el nombre de la APK que desea instalar: ").strip()
            if apk_name in dt:
                registros = emu.cargar_base_de_datos()
                emu.instalar_apk(emuladors, apk_name, dt, registros)
            else:
                print(f"APK {apk_name} no encontrada en la base de datos.")
        elif x == "f":
            registros = emu.cargar_base_de_datos()
            for apk_name in dt.keys():
                emu.instalar_apk(emuladors, apk_name, dt, registros)
        else:
            print("Opción no válida. Por favor, ingrese 'i' o 'f'.")

while True:
    do = input("1- Quieres agregar un nuevo valor a la base de datos?\n "
               "2-Instalar una apk?\n "
               "3-Tomar capturas de pantallas para analizar \n"
               "4-Tomar videos de pantallas para analizar \n"
               "5-Crear coordenadas en base de capturas \n"
               "6-Detectar coordenadas de iconos por cv2\n"
               "7-Hacer tap en las apk seleccionadas: ").strip().lower()

    try:
        if do == "1":
            add_value()
        elif do == "2":
            instalar()
        elif do == "3":# repito mucho estas lineas pero no tengo tiempo de refactorizarlo poner todo en funciones
            list_devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
            list_devices = list_devices.stdout.strip().split("\n")[1:]
            emuladors = [line.split("\t")[0] for line in list_devices if "emulator" in line]
            sc.tomar_captura(emuladors)
        elif do == "4":
            list_devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
            list_devices = list_devices.stdout.strip().split("\n")[1:]
            emuladors = [line.split("\t")[0] for line in list_devices if "emulator" in line]
            tiempo = int(input("¿Cuánto tiempo deseas grabar el video? (en segundos): ").strip())
            sc.tomar_video(emuladors, tiempo)
        elif do == "5":
            print("Ojo este metodo no funciona bien porque los modelos de la api no reconoce bien las imagenes " \
            "porque no estan entrenados para eso aqui esta por si quieres intentarlo funciona todo el codigo " \
            "falla el reconocimiento de imagenes")
            apk = input("¿Qué apk quieres analizar? ").strip()
            # esto es porque todos los emuladores son  iguales hasta ahora cuando tengas uno distinto solo lo pones 
            emulador = input("¿Qué emulador quieres usar? ").strip()
                #crear un .env con el token EJEMPLO: OPENAI_API_KEY=tu_token
            gpt.detectar_apk_con_gpt(emulador, apk)
        elif do == "6":
            apk = input("¿Qué apk quieres analizar? ").strip()
            emulador = input("¿Qué emulador quieres usar o quieres hacer esto en todos ? type t o nombre del emulador: ").strip()
            if emulador == "t":
                dti.detectar_todos_iconos(apk)
            else:
                dti.detectar_icono(emulador, apk)
            print("✅ Proceso completado.")
        elif do == "7":
            apk = input("🔎 Nombre de la APK para hacer tap : ").strip().lower()
            
            ge.procesar_taps_solo_apk(apk)
            print("✅ Proceso completado.")

        else:
            print("Opción no válida. Por favor, ingrese '1', '2' o '3'.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    continuar = input("¿Desea continuar? (s/n): ").strip().lower()
    if continuar != "s":
        break

print("Ejecución completada.")
