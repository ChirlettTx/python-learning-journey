"""
1) Crea un decorator llamado separador que imprima
 "---inicio---" antes y "---fin---" después de cualquier función. Aplícalo a esta función:
"""
def saludar():
    print("Hola, bienvenido")

def midecorador(func):
    def wrapper():
        print("---inicio---")
        func()
        print("---fin---")
    return wrapper

saludar = midecorador(saludar)
saludar()
print("_____________________")

"""
Ejercicio 2: decorator con argumento

Crea un decorator llamado mayusculas que convierta 
el resultado de una función a mayúsculas. Aplícalo a esta función:
"""
print("-------------------")
def mensaje(texto):
    print(texto)

def mayusculas(func):
    def wrapper(texto):
        resultado = texto.upper()
        func(resultado)
    return wrapper

mensaje = mayusculas(mensaje)
mensaje("hola mundo")

print("-------------------")
"""
Ejercicio 3: decorator con clase (sin método)
Crea un decorator cronometro que imprima:
⏱ Iniciando...
# aquí va lo que hace la función
⏱ Finalizado!
y aplicalo a la siguiente clase

"""
def cronometro(func):
    def wrapper(self):
        print("⏱ Iniciando...")
        func(self)
        print("⏱ Finalizado!")
    return wrapper  
class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
    
    @cronometro
    def ejecutar(self):
        print(f"Ejecutando tarea: {self.nombre}")
tarea = Tarea("lavar platos")
tarea.ejecutar()


print("-------------------")

"""
Ejercicio 4: igual al ejercicio del curso pero más simple
Crea un decorator formato que imprima "=== inicio ===" y "=== fin ===" alrededor de un mensaje. Aplícalo a este método:
"""
def decorator3(func):
    def wrapper(self, destinatario):
        print("=== inicio ===")
        func(self, destinatario)
        print("=== fin ===")
    return wrapper
class Mensaje:
    def __init__(self, texto):
        self.texto = texto
    @decorator3
    def enviar(self, destinatario):
        print(f"Mensaje para {destinatario}: {self.texto}")



mensaje = Mensaje("Hola!")
mensaje.enviar("Ana")
"""
SIEMPRE es así, sin excepción
def mi_decorator(func):        # 1. recibe la función
    def wrapper(argumentos):   # 2. wrapper tiene los mismos argumentos que la función
        # antes
        func(argumentos)       # 3. llama la función original
        # después
    return wrapper             # 4. retorna el wrapper
Los tres casos que existen para su uso
# Caso 1: función sin argumentos
def wrapper():
    func()

# Caso 2: función con argumentos
def wrapper(arg1, arg2):
    func(arg1, arg2)

# Caso 3: método de clase
def wrapper(self):           # sin otros args
    func(self)

def wrapper(self, arg):      # con otros args
    func(self, arg)

"""