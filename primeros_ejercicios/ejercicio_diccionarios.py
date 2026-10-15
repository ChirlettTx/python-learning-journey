#acceder a valores
pelicula = {
    "titulo": "El rey leon",
    "año": 1994,
    "director": "Roger allers",
    "genero": "Animacion"
}
print(f"titulo: {pelicula['titulo']}")
print(f"el año: {pelicula['año']}")
print(f"el director: {pelicula['director']}")
print("\n")
#Agregar y modificar valores
jugador = {
    "nombre": "carlos",
    "puntaje":100,
    "nivel": 1
}
jugador["vidas"] = 3
jugador["puntaje"] = 250
print(f"el diccionario completo es: {jugador}")
print("\n")
#diccionario con listas dentro
curso = {
    "nombre":"python desde cero",
    "profesor": "juan",
    "estudiantes": ["ana", "carlos", "maria"]
}
def nuevo_estudiante(curso, estudiantes):
    curso["estudiantes"].append(estudiantes)
    return curso
actualizar_curso = nuevo_estudiante(curso, "pedro")
print(f"lista de estudiantes: {curso['estudiantes']}")
print(len(curso['estudiantes']))