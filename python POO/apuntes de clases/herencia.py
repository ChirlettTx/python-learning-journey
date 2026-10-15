#Que sicede si quiero representar um conche electrico?

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
        consumo -- int consumo 
        """
        self._modelo = modelo    #se utiliza un barra baja para indicar la variable es privado, de uso interno
        self._potencia = potencia
        self._consumo = consumo
        self._km_actuales = 0
        self._combustible = "1/100km"

    def especificaciones(self): 
            """"metodo para imprimir las especificaciones del coche"""
            print("Modelo:", self._modelo, 
                  "\nPotencia: {} cv ".format(self._potencia),
                  "\nConsumo: {} {}".format(self._consumo, self._combustible),    
                  "\nKm actuales: ", self._km_actuales)
    @property
    def kilometros(self):
        return self._km_actuales
    @kilometros.setter
    def kilometros(self, kilometros):
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
tesla = coche("tesla model 3", 300, 15) # consumo: 15 kw/100km
tesla.especificaciones()
print("----------------")
### herencia
class cocheElectrico(coche):
    """
    Esta clase representa un coche electrico
    """
    def __init__(self, modelo, potencia, consumo):
        """
        inicializa los tributos de la clase padre.
        """
        super().__init__(modelo, potencia, consumo)
        self._combustible = "KWh/100km"
        
BMW = cocheElectrico("BMW model 3", 300, 15)
BMW.especificaciones()
#definicion de atributos y metodos propios de la clase hija
# se puden extender sus metodos y atributos

print("-------------------")

class cocheElectrico(coche):
    def __init__(self, modelo, potencia, consumo, capacidad_bateria):
        super().__init__(modelo, potencia, consumo)
        self._combustible = "KWh/100km"
        self._capacidad_bateria = capacidad_bateria

    def detalles_bateria(self):
        """"
        Muestra los detalles de la bateria del coche electrico
        """
        print("El tamaño de la bateria es: {}kWh".format(self._capacidad_bateria))

tesla = cocheElectrico("tesla model 4", 300, 15, 500)
tesla.especificaciones()
tesla.detalles_bateria()
print("-------------------")
#sobre escribir metodos de la clase padre
"""
en algunas ocaciones es posible que alguno de los metodos de la clase padre no se cumplan con las necesidades de la clase hija
que se ha definido. En estos casos podemos sobreescribir el metodo de la lase padre dentro de la clase hija.
"""

print("-------------------")
#se sobreescribira a la hija en la parte del metodo, se modifica el  consumo total del padre en la hija y se sobre escribe 
class cocheElectrico(coche):
    def __init__(self, modelo, potencia, consumo, capacidad_bateria):
        super().__init__(modelo, potencia, consumo)
        self._combustible = "KWh/100km"
        self._capacidad_bateria = capacidad_bateria

    def detalles_bateria(self):
        """"
        Muestra los detalles de la bateria del coche electrico
        """
        print("El tamaño de la bateria es: {}kWh".format(self._capacidad_bateria))
    def consumo_total(self):
            """
            Muestra el consumo total del coche desde el km 0
            """
            consumo_total = (self._km_actuales / 100) * self._consumo
            print("el consumo total es de {} KWh". format(consumo_total))

tesla = cocheElectrico("tesla model 4", 300, 15, 50)
tesla.kilometros = 100
tesla.consumo_total()

print("-------------------")
#objetos dentro de una clase
""""
Es posible que en algunos casos de uso, determinadas 
propiedades de una clase tenga suficiente entidad como para convertirse en una clase propia. En estos casos podemos asignar
un objeto de esta segunda a clase a cun atributo de la primera
"""
class Bateria:
    """Esta clase va a representar una bateria de un coche electrico"""
    def __init__(self, capacidad, tipo_pila, num_pilas, peso):
        self._capacidad = capacidad
        self._tipo_pila = tipo_pila
        self._num_pilas = num_pilas
        self._peso = peso
    def especificaciones(self):
        print("capacidad {} KWh".format(self._capacidad),
              "\nTipo de pilas: ", self._tipo_pila,
              "\nNumero de pilas: ", self._num_pilas,
              "\nPeso de la bateria: {}".format(self._peso))

bateria_tesla_modelS = Bateria(80, 2170, 203_136, 480)
bateria_tesla_modelS.especificaciones()
print("-------------------")
print("Coche electrico con bateria:")
#vamos a llamar la clase hija que tedra la clase bateria dentro, aqui bateria es un objeto ahora 
class cocheElectrico(coche):
    def __init__(self, modelo, potencia, consumo, bateria):
        super().__init__(modelo, potencia, consumo)
        self._combustible = "KWh/100km"
        self._bateria = bateria

    def detalles_bateria(self):
        """"
        Muestra los detalles de la bateria del coche electrico
        """
        self._bateria.especificaciones()
    def consumo_total(self):
            """
            Muestra el consumo total del coche desde el km 0
            """
            consumo_total = (self._km_actuales / 100) * self._consumo
            print("el consumo total es de {} KWh". format(consumo_total))
tesla = cocheElectrico("tesla model s", 400, 20, bateria_tesla_modelS)
tesla.detalles_bateria()
