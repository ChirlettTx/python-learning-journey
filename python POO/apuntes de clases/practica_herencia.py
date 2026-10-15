"""
Práctica Herencia
Objetivo

Desarrolla un sistema de "gestión para un zoológico" que modele animales utilizando conceptos de herencia,
 clases padre e hijas, y composición de clases para representar diversas especies y sus hábitats.

Instrucciones
Clase Animal:
Crea una clase llamada Animal. Esta será la clase base de la que heredarán otros tipos de animales.
La clase Animal debe tener un constructor que acepte cuatro parámetros: nombre, especie, edad y hábitat. 
Estos atributos deben ser almacenados como atributos de instancia. 
El atributo hábitat será a la vez un objeto procedente de una clase con el mismo nombre que se describirá más adelante.
Define un método mostrar_info() en la clase Animal que imprima el nombre, la especie, la edad del animal y 
los dos atributos de la clase hábitat que se describirán más adelante.
Clase Habitat:
Crea una clase llamada Habitat con dos atributos de instancia, tipo_habitat y temperatura.
Clases herencia de Animal:
Crea al menos dos clases derivadas que hereden de Animal: Mamifero y Ave. 
Estas clases deben añadir al menos un atributo específico (como tipo_pelaje para Mamifero y tipo_plumaje para Ave) y 
utilizar el constructor de la clase base para inicializar los atributos comunes.
Las clases derivadas deben sobrescribir el método mostrar_info() para incluir la información específica del tipo de animal 
junto con la información base. Pista: Esto puedes hacerlo creando un método dentro de la clase Mamifero y Ave llamado también 
mostrar_info que llame al método de la clase animal con el mismo nombre y que además imprima el tipo_pelaje o el tipo_plumaje.
Clase Zoologico:
Implementa una clase Zoologico que contenga dos atributos de instancia, el nombre del zoo (nombre) y una lista llamada animales. 
Esta lista almacenará instancias de diferentes animales.
La clase Zoologico debe tener métodos para añadir_animal al zoológico y mostrar_animales, que imprima la 
información de cada animal en el zoológico, incluido su hábitat, mediante un bucle for que recorra la lista animales y el método mostrar_info.
Ejecución:
Crea un objeto de la clase Zoologico con el nombre del Zoo.
Crea dos objetos de la clase Habitat con los argumentos: Sabana/Cálido y Bosque/Templado.
Crea un objeto de la clase Mamifero haciendo referencia a un león. Se proponen 
los siguientes parámetros: Nombre: Simba, Especie: León, Edad: 5, Habitat: Sabana/Calido, Pelaje: corto.
Crea un objeto de la clase Ave haciendo referencia a un canario. 
Se proponen los siguientes parámetros: Nombre: Piolín, Especie: Canario, Edad: 2, Habitat: Bosque/Templado, Plumaje: suave.
Llama al método añadir_animal con cada uno de los objetos de las clases Mamifero y Ave.
Llama al método mostrar_animales para observar por pantalla los datos del zoológico.
Resultado esperado
Animales en ZooFantástico:
--> Nombre: Simba
Especie: León
Edad: 5
Hábitat: Sabana, Cálido
Tipo de pelaje: Corto
--> Nombre: Piolín
Especie: Canario
Edad: 2
Hábitat: Bosque, Templado
Tipo de plumaje: Suave
Notas para el Estudiante
Para aprobar esta evaluación tu respuesta debe coincidir con los datos presentados en la sección "Resultado esperado".
Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no son correctos, 
se desbloqueará la pestaña "Explicación de la solución" en la parte superior del ejercicio. 
En esta pestaña puedes ver el código de solución de esta práctica.
"""
class Animal():
    """
    Esta clase representa un animal y sera la clase base que heredaran otros tipos de animales
    """
    def __init__(self, nombre, especie, edad, habitat):
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        self._habitat = habitat

    def mostrar_info(self):
        """Metodo para imprimir las especificaciones de los animales"""
        print("Nombre: ", self._nombre,
              "\nEspecie: ", self._especie,
              "\nEdad: ", self._edad,
              f"\nHábitat: {self._habitat._tipo_habitat}, {self._habitat._temperatura}")

class Habitat:
    """Esta clase representa el habitat de un animal"""
    def __init__(self, tipo_habitat, temperatura):
        self._tipo_habitat = tipo_habitat
        self._temperatura = temperatura
    
#tengo dudas en estos metodos y el como estan sobre escritos
class Mamifero(Animal):
    def __init__(self, nombre, especie, edad, habitat,tipo_pelaje):
        super().__init__(nombre, especie, edad, habitat) #hereda del padre
        self._tipo_pelaje = tipo_pelaje
    def mostrar_info(self):
           super().mostrar_info()#llama al padre y agrega al atributo nuevo
           print(f"Tipo de pelaje: {self._tipo_pelaje}")

class Ave(Animal):
    def __init__(self, nombre, especie, edad, habitat, tipo_plumaje):
        super().__init__(nombre, especie, edad, habitat)
        self._tipo_plumaje = tipo_plumaje   

    def mostrar_info(self):#llama al padre y agrega al atributo nuevo
       super().mostrar_info()
       print(f"Tipo de pelaje: {self._tipo_plumaje}")
            
class Zoologico():
    def __init__(self, nombre):
        self._nombre = nombre
        self._animales = [] #lista vacia que se llena con añadir animal

    def añadir_animal(self, animal):
        self._animales.append(animal) #agregar la lista

    def mostrar_animales(self):
        print(f"Animales en {self._nombre}:")
        for animal in self._animales:
            print("-->", end= "")
            animal.mostrar_info()

Zoo = Zoologico("ZooFantástico")
habitat_sabana = Habitat("Sabana", "Cálido")
habitat_bosque = Habitat("Bosque", "Templado")
leon = Mamifero("Simba","León", 5, habitat_sabana, "corto")
canario = Mamifero("Piolín", "Canario", 2, habitat_bosque, "suave")

Zoo.añadir_animal(leon)
Zoo.añadir_animal(canario)

Zoo.mostrar_animales()