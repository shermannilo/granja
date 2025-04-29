import screenshot as sc
import gestos as ge
import time as t 
import detector_iconos as dti
from dotenv import load_dotenv
import os

load_dotenv()
pantalla=sc.identificar_pantalla()

def abrir_instagram():
    for emulador in ge.obtener_emuladores_activos():
        if pantalla[emulador]=="pantalla_inicio":
            ge.normalizar(emulador)
            t.sleep(0.2)
            dti.detectar_icono(emulador,"instagram")
            ge.procesar_taps_solo_apk("instagram",emulador)

        if pantalla[emulador]=="pantalla_apk":
            t.sleep(0.2)
            dti.detectar_icono(emulador,"instagram")
            ge.procesar_taps_solo_apk("instagram",emulador)
#poner todas estas funciones en secuencia if de menor a mayor asi puede identificar la 
#parte en que esta y de ahi accederle 
def iniciar_secion():
    for emulador in ge.obtener_emuladores_activos():
        if pantalla[emulador]=="inicio_insta":
            ge.hacer_tap(emulador, 430, 998)
            ge.escribir(os.getenv("usuario"),emulador)
            ge.hacer_tap(emulador, 269, 1181)
            ge.escribir(os.getenv("password"),emulador)
        elif pantalla[emulador]=="usuario_ok":
            ge.hacer_tap(emulador, 269, 1181)
            ge.escribir(os.getenv("password"),emulador)
             
