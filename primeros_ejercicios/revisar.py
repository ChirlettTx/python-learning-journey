# 1. variable global
recursos_ecosistema = {"agua": 1000, "alimento": 800}

# 2. función animal_interactua
def animal_interactua(tipo_animal, alimento, agua=None):
    global recursos_ecosistema
    
    # verificar recursos suficientes
    if recursos_ecosistema["alimento"] < alimento:
        print("Recursos insuficientes en el ecosistema")
        return

    if agua is not None and recursos_ecosistema["agua"] < agua:
        print("Recursos insuficientes en el ecosistema")
        return
    
    # si es herbívoro resta agua Y alimento
    if tipo_animal == "herbívoro":
        recursos_ecosistema["agua"] -= agua
        recursos_ecosistema["alimento"] -= alimento
        print(f"Un herbívoro ha consumido {agua} de agua y {alimento} de alimento.")
    
    # si es carnívoro resta solo alimento
    elif tipo_animal == "carnívoro":
        recursos_ecosistema["alimento"] -= alimento
        print(f"Un carnívoro ha consumido {alimento} de alimento.")
    
    # mostrar estado actual
    print(f"Estado actual del ecosistema: {recursos_ecosistema}")

# 3. función lluvia
def lluvia(cantidad):
    global recursos_ecosistema
    recursos_ecosistema["agua"] += cantidad
    print(f"¡Ha llovido! Se añadieron {cantidad} unidades de agua al ecosistema.")

# 4. fuera de las funciones
print(f"Inicio del día en el ecosistema: {recursos_ecosistema}")

animal_interactua("herbívoro", 100, 200)
animal_interactua("carnívoro", 50)

lluvia(200)

print(f"Fin del día en el ecosistema: {recursos_ecosistema}")