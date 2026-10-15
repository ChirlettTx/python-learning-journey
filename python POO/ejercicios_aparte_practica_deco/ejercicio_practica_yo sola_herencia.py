"""
Ejercicio 1: herencia simple con super()
Crea una clase Vehiculo con estos atributos: marca, modelo, año. Y una clase hija Auto que herede de Vehiculo y agregue el atributo num_puertas.
Ambas clases deben tener un método mostrar_info que imprima sus datos. La clase Auto debe llamar al método del padre con super().
Resultado esperado:
Marca: Toyota
Modelo: Corolla
Año: 2020
Número de puertas: 4
"""
class Vehiculo():
    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    def mostrar_info(self):
        print(f"Marca: {self._marca}",
              f"\nModelo: {self._modelo}",
              f"\nAño: {self._año}")

class Auto(Vehiculo):
    def __init__(self,marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self._num_puertas = num_puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self._num_puertas}")

car = Auto("Toyota", "Corolla", 2020, 4)
car.mostrar_info()

print("-------------------------")

"""
Ejercicio 2: clase con objeto adentro
Crea una clase Direccion con atributos calle y ciudad. 
Luego crea una clase Persona que tenga atributos nombre, edad y direccion (que será un objeto de la clase Direccion).
Resultado esperado:
Nombre: Ana
Edad: 25
Calle: Av. Principal 123
Ciudad: Madrid
"""
class Direccion:
    def __init__(self, calle, ciudad):
        self._calle = calle
        self._ciudad = ciudad
    def mostrar_info(self):
        print(f"Calle: {self._calle}"
              f"\nCiudad: {self._ciudad}")

class Persona:
    def __init__(self, nombre, edad, direccion):
        self._nombre = nombre
        self._edad = edad
        self._direccion = direccion
    def mostrar_info(self):
        print(f"Nombre: {self._nombre}",
              f"\nEdad: {self._edad}")
        self._direccion.mostrar_info() #aqui se supone que llamo al objeto que es de la clase direccion

direccion = Direccion("Av. Principal 123", "Madrid")
persona = Persona("Ana", 25, direccion)#aqui se agrega el tercer argumento que es el objeto que creamos de direccion
persona.mostrar_info()
print("-----------------")
"""
Ejercicio 3: combinando todo
Crea una clase Dispositivo con atributos marca y precio. Luego dos clases hijas Telefono (agrega num_sim) y Laptop (agrega ram). 
Finalmente una clase Tienda con nombre y lista productos que tenga métodos agregar_producto y mostrar_productos.
Resultado esperado:
Productos en TechStore:
--> Marca: Samsung, Precio: 800, SIMs: 2
--> Marca: Dell, Precio: 1200, RAM: 16GB
"""
class Dispositivo:
    def __init__(self, marca, precio):
        self._marca = marca
        self._precio = precio
    
    

class Telefono(Dispositivo):
    def __init__(self,marca, precio, num_sim):
        super().__init__(marca, precio)
        self._num_sim = num_sim
    def mostrar_info(self):
        print(f"Marca: {self._marca}, Precio: {self._precio}, SIMs: {self._num_sim}")

class Laptop(Dispositivo):
    def __init__(self, marca, precio, ram):
        super().__init__(marca, precio)
        self._ram = ram
    def mostrar_info(self):
        print(f"Marca: {self._marca}, Precio: {self._precio}, RAM: {self._ram}")

class Tienda:
    def __init__(self, nombre):
        self._nombre = nombre
        self._lista_productos = []

    def agregar_producto(self, producto):
        self._lista_productos.append(producto)
        
    def mostrar_productos(self):
        print(f"Productos en {self._nombre}:")
        for producto in self._lista_productos:
            print("-->", end="")
            producto.mostrar_info()

telefono = Telefono("Samsung", 800, 2)
laptop = Laptop("Dell", 1200, "16GB")
tienda = Tienda("TechStore")
tienda.agregar_producto(telefono)
tienda.agregar_producto(laptop)
tienda.mostrar_productos()