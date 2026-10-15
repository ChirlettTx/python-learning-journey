#ejercicio 1 if
numeros = [5, 12, 8, 3, 19, 7, 14]
print("Los numeros mayores son: ")

for valores in numeros:
    if valores > 10:
        print(f"{valores}")

#ejercicio 2 for

palabras = ["gato", "elefante", "sol", "computadora", "paz"]

for palabra in palabras:
    if len(palabra) > 4:
        print(f"{palabra} tiene {len(palabra)} letras")

#ejercicio 3 while
cont = 0
while  cont <5:
    cont += 1
    print(f"{cont}")

print("Fin del contador")

#ejercicio 4 while con condicion
cont = 10
while cont > 0:
    cont -=2
    if cont % 2 == 0:
        print(f"{cont}")    
print("¡Llegué a cero!")

#ejercicio 5 for + while
tareas = ["estudiar", "hacer ejercicio", "cocinar", "leer"]

for lista in tareas:
    if lista == "cocinar":        # si es cocinar
        contador = 1
        while contador <= 3:
            print(f"cocinando... {contador}")
            contador += 1
    else:                         # si NO es cocinar
        print(f"{lista}")