#acceder a elementos de una lista
frutas = ["manzana", "pera", "uva", "sandia", "kiwi"]
print(frutas[0])
print(frutas[-1])
print(frutas[2])

#modificar una lista
colores = ["rojo", "azul", "verde"]
colores.append("amarillo")
print(colores)
print(len(colores))

#funcion con lista
def analizar_lista(nombres):
    print(f"primer nombre: {nombres[0]}")
    print(f"primer ultimo nombre: {nombres[-1]}")
    print(f"Cantidad total de nombres: {len(nombres)}")
    
analizar_lista(["ana", "carlos", "maria", "pedro", "lucia"])