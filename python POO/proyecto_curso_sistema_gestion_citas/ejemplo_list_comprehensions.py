#Es una forma concisa y elegante de crear colecciones (listas, diccionarios, sets) en python
#en lugar de escribir bucles for con multiples lineas, puedes crear estas escrituras en una sola linea de codigo
#forma tradicional
numeros = [1,2,3,4,5]
dobles = []
for numero in numeros:
    dobles.append(numero * 2)
print(dobles)
print(f"{'='*20}")
#con list Comprehension
numeros = [1,2,3,4,5]
dobles = [numero * 2 for numero in numeros]
print(dobles)
print(f"{'='*20}")
#con condiciones (filtrado)
#solo los numeros mayores que 5
numeros = [3,7,2,9,4,10]
mayores = [n for n in numeros if n > 5]
print(mayores)
print(f"{'='*20}")
#solo palabras que comiencen con P
palabras = ["python", "java", "php", "ruby"]
con_p = [palabra for palabra in palabras if palabra.startswith('p') ]
print(con_p)
print(f"{'='*20}")
#extraer solo los nombre
estudiantes = ["Ana", "Carlos", "Maria", "Pedro"]
saludos = ["Hola" + nombre for nombre in estudiantes]
print(saludos)
print(f"{'='*20}")
#Dictionary Comprehensions (comprension de diccionarios)
#sintaxis Basica {clave: valor for elemento in iterable}
#ejemplo crear un diccionario donde la clave es el numero y el valor su doble
numeros = [1,2,3,4,5]
dobles = {n: n * 2 for n in numeros}
print(dobles)
print(f"{'='*20}")
#crear un diccionario con cada palabra y su longitud
palabras = ["hola", "mundo", "python"]
longitudes = {palabra: len(palabra) for palabra in palabras}
print(longitudes)
print(f"{'='*20}")
#con filtrado
#solo numeros pares como claves
numeros = [1,2,3,4,5,6]
pares = {n: n * 10 for n in numeros if n % 2 == 0}
print(pares)
print(f"{'='*20}")
#solo palabras cortas (menos de 5 letras)
palabras = ["sol", "mariposa", "luz", "elefante", "mar"]
cortas = {palabra: len(palabra) for palabra in palabras if len(palabra) < 5}
print(cortas)
print(f"{'='*20}")
#Modificar un diccionario existente
#Tenemos un diccionario y queremos duplicar todos sus valores
original = {"a": 1, "b": 2, "c": 3}
duplicado = {clave: valor * 2 for clave, valor in original.items()}
print(duplicado)
print(f"{'='*20}")
#set comprehencios (comprension de conjuntos)
#los sets son colecciones sin elementos dupicados
#sintaxis basica {expresion for elemento in iterable}
#ejemplos, eliminar duplicados automaticamente
numeros = [1,2,2,3,3,4,5,5]
sin_duplicados = {n for n in numeros}
print(sin_duplicados)
print(f"{'='*20}")
#obtener letras unicas de ua palabra
palabra = "banana"
letras_unicas = {letra for letra in palabra}
print(letras_unicas)
print(f"{'='*20}")
#solo numeros pares de una lista (sin duplicados)
numeros = [1,2,3,4,4,5,6,6]
pares = {n for n in numeros if n % 2 == 0}
print(pares)
print(f"{'='*20}")
#comparacion lado a lado / vemos el mismo ejemplo con las tres estructuras
numeros = [1,2,3,4,5]
#lista - mantiene orden y permite duplicados
lista = [n * 2 for n in numeros]
print(lista)
#set - sin duplicados, sin ordenar garantizado
conjunto = {n * 2 for n in numeros}
print(conjunto)
#diccionario -pares clave:valor
diccionario = {n: n * 2 for n in numeros}
print(diccionario)
#Ventajas de usar Comprehensions ✨
#Más legible: Una vez que te acostumbras, son más fáciles de leer
#Más conciso: Menos líneas de código
#Más rápido: Generalmente más eficientes que bucles tradicionales
#Más Pythónico: Sigue las convenciones del lenguaje
#cuando No usar comprehensions
#Cuando la lógica es muy compleja (mejor usa bucles tradicionales)
#Cuando afecta la legibilidad del código
#Cuando necesitas hacer varias operaciones por elemento