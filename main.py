import json
import os

def cargar_recetas(ruta_archivo):
    #Por si acaso
    if not os.path.exists(ruta_archivo):
        print(f"El archivo {ruta_archivo} no existe. Se devolverá una lista vacía.")
        return []
        
    #Parseamos de JSON a Python
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        recetas = json.load(archivo)
        return recetas

def imprimir_recetas(recetas):
    if not recetas:
        print("No hay recetas para mostrar.")
        return

    print("\n" + "="*40)
    print(" 🍽️ RECETAS 🍽️ ")
    print("="*40)
    
    for receta in recetas:
        print(f"\nID: {receta['id']} | {receta['nombre'].upper()}")
        print(f"  🍲 Tipo: {receta['tipo']}")
        print(f"  ⏱️ Tiempo: {receta['tiempo']} min")
        print(f"  🏷️ Etiquetas: {', '.join(receta['etiquetas'])}")
        print(f"  🛒 Ingredientes: {', '.join(receta['ingredientes'])}")
        
    print("\n" + "="*40 + "\n")




#MAIN
if __name__ == "__main__":
    #Cargamos los datos
    base_datos = 'recetas.json'
    mis_recetas = cargar_recetas(base_datos)
    
    #Mostramos por consola
    imprimir_recetas(mis_recetas)