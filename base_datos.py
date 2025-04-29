import json
import os

path_dt="dt.json"

if os.path.exists(path_dt):
    with open(path_dt, "r") as file:
        dt = json.load(file)
else:
    dt = {}


def mostrar_dt():
    if dt:
        print("Contenido de dt:")
        for key, value in dt.items():
            print(f"{key}: {value}")
    else:
        print("El diccionario dt está vacío.")

def agregar_elemento(key, value):
    if key in dt:
        ans= input(f"El elemento {key} ya existe. ¿Desea sobrescribirlo? (s/n): ")
        if ans.lower() == "s":
            dt[key] = value
            print(f"Elemento sobrescrito: {key}: {value}")
            with open(path_dt, "w") as file:
                json.dump(dt, file)
    else:
        dt[key] = value
        print(f"Elemento agregado: {key}: {value}")
        with open(path_dt, "w") as file:
            json.dump(dt, file)