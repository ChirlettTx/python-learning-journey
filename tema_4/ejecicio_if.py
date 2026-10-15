def recomendar_pelicula(genero, edad):
    if genero == "acción" and edad >= 13:
        recomendacion = "Deadpool"
    elif genero == "acción" and edad < 13:
        recomendacion = "Regreso al futuro"
    elif genero == "comedia":
        recomendacion ="Aterriza como puedas"
    else:
        recomendacion = "Explorar otros géneros"
    return recomendacion
genero = input("¿Cuál es tu género favorito?")
edad = int(input("¿Cuántos años tienes?"))
recomendacion = recomendar_pelicula(genero, edad)
print(f"Teniendo en cuenta tu edad {edad} y género favorito {genero}, te recomiendo la siguiente pelicula: {recomendacion} ")