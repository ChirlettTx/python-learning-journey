def comparar_longitud(palabra1, palabra2):
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
    
    return longitud1 == longitud2
     
resultado = comparar_longitud("gato", "perro")
print(f'¿Son "gato" y "perro" dos palabras con la misma longitud? {resultado}')