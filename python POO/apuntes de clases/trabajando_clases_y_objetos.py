#trabajando con clases y objetos
#Definiendo una clase
class coche():
    """
    Esta clase representa un coche
    """
    def __init__(self, modelo, potencia, consumo):
        """
        inicializa los tributos de instancia.
        argumentos posicionales:
        modelo -- string nombre del coche
        potencia -- int potencia del coche en cv
        consumo -- int consumo medio del coche en 1/100km
        """
        self._modelo = modelo
        self._potencia = potencia
        self._consumo = consumo

    def especificaciones(self): 
        """"metodo para imprimir las especificaciones del coche"""
        print("Modelo:", self._modelo, 
              "\nPotencia: {} cv ".format(self._potencia),
              "\nConsumo: {} 1/100km".format(self._consumo))    

mercedes = coche("mercedes c200", 180, 7)
mercedes.especificaciones()
print("-----------------")
##Atributos  con valores por defecto/ es aquel que ya tiene un valor definido
class coche():
    """
    Esta clase representa un coche
    """
    def __init__(self, modelo, potencia, consumo):
        """
        inicializa los tributos de instancia.
        argumentos posicionales:
        modelo -- string nombre del coche
        potencia -- int potencia del coche en cv
        consumo -- int consumo medio del coche en 1/100km
        """
        self._modelo = modelo    #se utiliza un barra baja para indicar la variable es privado, de uso interno
        self._potencia = potencia
        self._consumo = consumo
        self._km_actuales = 0

    def especificaciones(self): 
        """"metodo para imprimir las especificaciones del coche"""
        print("Modelo:", self._modelo, 
              "\nPotencia: {} cv ".format(self._potencia),
              "\nConsumo: {} 1/100km".format(self._consumo),    
              "\nKm actuales: ", self._km_actuales)

    def actualizar_kilometros(self, kilometros):
        """
        metodo para actualizar los kilometros actuales del coche
        argumentos posicionales:
        kilometros -- int kilometros actuales
        """
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else: 
            print("Error: no se puede establecer un número de kilometros menor al actual")

audi = coche("audi b4", 120, 5)
audi.actualizar_kilometros(300)
audi.especificaciones()
print("-----------------")
mercedes = coche("mercedes b200", 180, 7)
mercedes.actualizar_kilometros(1000)
mercedes.actualizar_kilometros(500)
mercedes.especificaciones()
print("-----------------"*20)
#extencion de la funcionalidad de la clase
#esto se refiere a la posibilidad de agregar nuevos metodos a una clase existente
class coche():
    """
    Esta clase representa un coche
    """
    def __init__(self, modelo, potencia, consumo):
        """
        inicializa los tributos de instancia.
        argumentos posicionales:
        modelo -- string nombre del coche
        potencia -- int potencia del coche en cv
        consumo -- int consumo medio del coche en 1/100km
        """
        self._modelo = modelo    #se utiliza un barra baja para indicar la variable es privado, de uso interno
        self._potencia = potencia
        self._consumo = consumo
        self._km_actuales = 0

    def especificaciones(self): 
        """"metodo para imprimir las especificaciones del coche"""
        print("Modelo:", self._modelo, 
              "\nPotencia: {} cv ".format(self._potencia),
              "\nConsumo: {} 1/100km".format(self._consumo),    
              "\nKm actuales: ", self._km_actuales)

    def actualizar_kilometros(self, kilometros):
        """
        metodo para actualizar los kilometros actuales del coche
        argumentos posicionales:
        kilometros -- int kilometros actuales
        """
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else: 
            print("Error: no se puede establecer un número de kilometros menor al actual")
    def consumo_total(self):
        """
        Muestra el consumo total del coche desde el km 0
        """
        consumo_total = (self._km_actuales / 100) * self._consumo
        print("el consumo total es de {} litros". format(consumo_total))
lamborgini = coche("lamborgini", 600, 10)
lamborgini.consumo_total()
lamborgini.especificaciones()
lamborgini.actualizar_kilometros(100)
lamborgini.especificaciones()
lamborgini.consumo_total()
print("-----------------")
lamborgini.actualizar_kilometros(300)
lamborgini.especificaciones()
lamborgini.consumo_total()
print("-----------------")
lamborgini.actualizar_kilometros(10)
lamborgini.especificaciones()
lamborgini.consumo_total()