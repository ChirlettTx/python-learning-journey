#tomar un archivo txt, abrirlo, leerlo, vooverlo una lista, cerrarlo y luego se agrega al final un nuevo libro.
#liego llamamos al primer libro de la lista, para despues agregar uno mas y por ultimo imprimir los resultados 
def aumentar_biblioteca(nuevo_libro):
    archivo = open("libros.txt")
    libros = archivo.read().splitlines()
    archivo.close()
    libros.append(nuevo_libro)
    return libros
    
def primer_libro_leido(libros):
    primer_libro = libros[0]
    return primer_libro
    
biblioteca = aumentar_biblioteca("Las Aventuras de Huckleberry Finn")

print("La biblioteca de libros leídos es: ")
print(biblioteca)

primer_libro = primer_libro_leido(biblioteca)
print(f'El primer libro que he leído es: "{primer_libro}" ')