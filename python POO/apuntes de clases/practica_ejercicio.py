"""
Práctica Clases, Objetos, Métodos y Atributos
Objetivo
En este caso práctico se propone al alumno "Crear un software para la gestión de una biblioteca".
Para ello el alumno debe hacer uso de clases, objetos, métodos y atributos en Python.
Instrucciones
Crea una clase llamada Libro que represente los detalles básicos de un libro en una biblioteca. 
La clase Libro debe incluir los siguientes atributos de instancia:
titulo (str): El título del libro.
autor (str): El nombre del autor del libro.
isbn (str): El número ISBN del libro.
disponible (bool): Un valor booleano que indica si el libro está disponible para préstamo.
Dentro de la clase Libro, define un método __init__ que inicialice 
los atributos de instancia con los valores proporcionados como argumentos. 
Asegúrate de que todos los libros se inicialicen como disponibles.
Define un método información que muestre por pantalla los detalles de libro.
Define un método prestar_libro que cambie el estado de disponible a False cuando un libro se preste. 
Debe mostrarse por pantalla que el libro ha sido prestado y su información invocando el método información. 
Si el libro ya está prestado, debe imprimir un mensaje que diga: Este libro ya está prestado.
Define otro método devolver_libro que cambie el estado de disponible a True cuando un libro sea devuelto. 
Debe mostrarse por pantalla que el libro ha sido devuelto y su información invocando el método informacion. 
Si el libro ya está disponible, debe imprimir un mensaje que diga: Este libro ya está en la biblioteca
Fuera de la clase, crea al menos dos instancias de Libro con diferentes detalles. 
Ejemplo: un libro de J.K. Rowling y otro de George Orwell.
Prueba los métodos prestar_libro y devolver_libro con tus instancias de libros para demostrar que 
el estado de disponibilidad cambia apropiadamente y que los mensajes se imprimen cuando es necesario.

Resultado esperado

El libro "Harry Potter y la piedra filosofal" ha sido prestado.
--> Informacion del libro: Harry Potter y la piedra filosofal
Titulo: Harry Potter y la piedra filosofal
Autor: J.K. Rowling
ISBN: 978-0747532743
El libro "Harry Potter y la piedra filosofal" ha sido devuelto a la biblioteca.
--> Informacion del libro: Harry Potter y la piedra filosofal
Titulo: Harry Potter y la piedra filosofal
Autor: J.K. Rowling
ISBN: 978-0747532743
El libro "1984" ha sido prestado.
--> Informacion del libro: 1984
Titulo: 1984
Autor: George Orwell
ISBN: 978-0451524935
Este libro ya está prestado.
Notas para el estudiante
Para aprobar esta evaluación tu respuesta debe coincidir con los
datos presentados en la sección "Resultado esperado".
Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no
son correctos, se desbloqueará la pestaña "Explicación de la solución" en la parte superior del ejercicio.
En esta pestaña puedes ver el código de solución de esta práctica.

"""


class Libro():
    def __init__(self, titulo, autor, isbn):
        """Inicializa los atributos de instancia
            argumentos posicionales:
            titulo: string nombre del Libro
            autor: string nombre del autor del Libro
            isbn: str numero del isbn del Libro
            disponible: indica si un libro esta diponible o no.
        """
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self.disponible = True
        
    def informacion(self):
        "debe mostrar la informacion del libro consultado"
        print("Titutlo: ", self._titulo,
        "\nAutor: ", self._autor,
        "\nISBN: ", self._isbn,
        "\nDisponibilidad: ", self.disponible)
        
    def prestar_libro(self):
        if self.disponible == False:
            print("Este libro ya está prestado")
        else:
            self.disponible = False
            print(f"El libro \'{self._titulo}\' ha sido prestado. ")
            print("--> informacion del libro: ", self._titulo)
            self.informacion()
    
    def devolver_libro(self):
        if self.disponible == True:
            print("Este libro ya está en la biblioteca")
        else:
            self.disponible = True
            print(f"El libro \'{self._titulo}\' ha sido devuelto a la biblioteca. ")
            print("--> informacion del libro: ", self._titulo)
            self.informacion()
            
            
libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "978-0747532743")
libro2 = Libro("1984", "George Orwell", "978-0451524935")

libro1.prestar_libro()
libro1.devolver_libro()
libro2.prestar_libro()
libro2.prestar_libro()