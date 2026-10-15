#ejercicio 1 recorre esta lista e imprime solo los numeros pares
#if dentro de for
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)

print("----------------------")
#ejercicio 2 while con if dentro
#crea un contador del 1 al 10  y si es multiplo de 3
#imprime multiplo

cont = 0
while cont < 10:
    cont +=1
    if cont % 3 == 0:
        print("múltiplo!")
    else:
        print(cont)

#ejercio 3 for con while / el for ya recorre la lista que en este caso se encuentra en jugadores
jugadores = ["Ana", "Carlos", "María"]

for jugada in jugadores:
        contador = 1
        while contador <= 3:
            print(f"{jugada} lanza dado {contador}")
            contador +=1
    