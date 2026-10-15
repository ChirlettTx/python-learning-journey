def compras_nuevas(compras):
    archivo = open("compras.txt")
    comprar = archivo.read().splitlines()
    archivo.close()

    comprar.append(compras)
    return comprar

def gestionar_compras(compras):
    print("la lista de compras es: ")

    for indice, compra in enumerate(compras, 1):
        print(f"{indice}. {compra}")
    print(f"hay {len(compras)} cosas por comprar")

comprar = compras_nuevas("una carcasa")
gestionar_compras(comprar)