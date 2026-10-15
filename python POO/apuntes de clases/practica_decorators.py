"""
Decorators sirven para modificar la comportamiento de una función sin modificar su código original.
"""
def mi_funcion():
    print("Hola mundo")

def mi_decorator(func):
    def wrapper():
        print("Antes de llamar a la funcion")
        func()
        print("Después de llamar a la funcion")
    return wrapper

mi_funcion_mod = mi_decorator(mi_funcion)
mi_funcion_mod()

