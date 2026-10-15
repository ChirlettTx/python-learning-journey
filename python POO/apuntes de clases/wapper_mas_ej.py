def mi_funcion():
    print("hola mundo")

def mi_decorator(func):
    def wrapper():
        if var < 5:
            func()
        else: 
            print("No se puede ejecutar la funcion")
    return wrapper

mi_funcion = mi_decorator(mi_funcion)
var = 3
mi_funcion()
var = 10
mi_funcion()
#syntactic sugar una version mas corta de hacer el uso de decorators con wrapper

def mi_decorator(func):
    def wrapper():
        print("Antes de llamar a la funcion")
        func()
        print("Después de llamar a la funcion")
    return wrapper

@mi_decorator
def mi_nuevafuncion():
    print("Hola mundo")

mi_nuevafuncion()