

def añadir_tarea(tarea):
    archivo = open("tareas.txt")
    tareas = archivo.read().splitlines()
    archivo.close()

    tareas.append(tarea)
    return tareas

def gestionar_tareas(tarea):
    print("tareas pendientes de realizar: ")

    for indice, tarea in enumerate(tareas, 1):
        print(f"{indice}. {tarea}")
    print (f"Hay {len(tareas)} tareas pendientes de realizar.")

tareas = añadir_tarea("Pagar la cuota de multa")
gestionar_tareas(tareas)