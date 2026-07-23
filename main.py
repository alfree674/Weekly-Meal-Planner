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

def guardar_recetas(recetas, ruta_archivo):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        # indent=4 para formatearlo, ensure_ascii=False para dejar tildes y ñ
        json.dump(recetas, archivo, indent=4, ensure_ascii=False)

def anadir_receta(recetas, ruta_archivo):
    print("\n--- 🍳 AÑADIR NUEVA RECETA ---")
    nombre = input("Nombre del plato: ").strip().capitalize()
    #Comprobamos que no sea duplicado
    duplicado= False
    duplicado_id= -1
    for receta in recetas:
        if receta["nombre"].strip().capitalize() == nombre:
            duplicado = True
            duplicado_id = receta["id"]
            break
    if duplicado:
        print(f"La receta '{nombre}' ya existe en tu recetario con id '{duplicado_id}'")
        return 
    else: #si no existe, continuamos pidiendo el resto de datos
        #El tipo debe ser una de las opciones
        opciones_validas = ["Desayuno", "Comida", "Merienda", "Cena"]
        es_tipo_valido = False
        while not es_tipo_valido:
            tipo= input(f"Tipo de comida {opciones_validas}: ").strip().capitalize()
            if tipo in opciones_validas:
                es_tipo_valido = True
            else:
                print("Error: Por favor, escribe una de las opciones válidas.")
    
        #El tiempo debe ser un número  
        es_num = False
        while not es_num:
            try:
                tiempo = int(input("Introduce el tiempo de preparación: "))
                if tiempo > 0:
                    es_num = True
                else:
                    print("Debe ser mayor que cero.")
            except ValueError:
                print("Error: Introduce un número.")

        #Pedimos los ingredientes separados por comas y lo convertimos a lista
        ingredientes_input = input("Ingredientes (separados por coma): ")
        ingredientes = [i.strip().capitalize() for i in ingredientes_input.split(",") if i.strip()]
    
        #Igual con las etiquetas
        etiquetas_input = input("Etiquetas (separadas por coma, ej: Rápido, Tupper, Pasta): ")
        etiquetas = [e.strip().capitalize() for e in etiquetas_input.split(",") if e.strip()]

        # Calculamos el ID: CAMBIAR EN FUTURO, N-1 COMPARACIONES INNECESARIAS 
        nuevo_id = max([r['id'] for r in recetas], default=0) + 1

        nueva_receta = {
            "id": nuevo_id,
            "nombre": nombre,
            "tipo": tipo,
            "tiempo": tiempo,
            "ingredientes": ingredientes,
            "etiquetas": etiquetas
        }

        # Añadimos a la lista en memoria y luego guardamos en el archivo
        recetas.append(nueva_receta)
        guardar_recetas(recetas, ruta_archivo)
    
        print(f"\n✅ ¡Receta '{nombre}' añadida y guardada con éxito en el JSON!")





#MAIN
if __name__ == "__main__":
    #Cargamos los datos
    base_datos = 'recetas.json'
    mis_recetas = cargar_recetas(base_datos)
    
    #Bucle principal para el menú interactivo)
    while True:
        print("\n" + "*"*40)
        print(" 📅 ORGANIZADOR DE MENÚ SEMANAL 📅 ")
        print("*"*40)
        print("1. Ver todas las recetas")
        print("2. Añadir nueva receta")
        print("3. Salir")
        
        opcion = input("\nElige una opción (1-3): ")
        
        if opcion == '1':
            imprimir_recetas(mis_recetas)
        elif opcion == '2':
            anadir_receta(mis_recetas, base_datos)
        elif opcion == '3':
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n❌ Opción no válida. Por favor, elige 1, 2 o 3.")