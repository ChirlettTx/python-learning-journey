def analizar_palabra(palabra):
    mayusculas=palabra.upper()
    minusculas=palabra.lower()
    longitud = len(palabra)

    print(f"palabra original: {palabra}")
    print(f"palabra mayuscula: {mayusculas}")
    print(f"palabra minuslcula: {minusculas}")
    print(f"longitud: {longitud}")

analizar_palabra("python")

print("--------------------------")

def operar_numeros(num1, num2):
    suma = num1+num2
    resta = num1-num2
    multi= num1*num2
    division = num1/num2

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multi}")
    print(f"División: {division:.2f}")

operar_numeros(10,3)