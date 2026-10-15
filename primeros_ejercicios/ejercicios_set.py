# Coleccion de arte con elementos duplicados
coleccion = [
    "Mona Lisa", "El Grito", "Mona Lisa", "La Noche Estrellada",
    "Las Meninas", "Guernica", "La Última Cena", "La Creación de Adán",
    "La Persistencia de la Memoria", "La Libertad guiando al pueblo",
    "El Beso", "Nacimiento de Venus", "El Jardín de las Delicias",
    "La Joven de la Perla", "El David",
    "Los Girasoles", "La Gran Ola de Kanagawa",
    "La Ronda Nocturna", "American Gothic",
    "Los Jugadores de Cartas", "La Noche Estrellada",
    "La Última Cena", "Guernica", "Las Meninas",
    "La Persistencia de la Memoria", "Mona Lisa"
]

def revisar_coleccion(coleccion):
    sin_duplicado = set(coleccion)
    coleccion_limpia = list(sin_duplicado)
    return coleccion_limpia
    
print(f"Colección antes de la revisión: {coleccion}")
print("\n")
print(f"Colección después de la revisión: {revisar_coleccion(coleccion)}")
    