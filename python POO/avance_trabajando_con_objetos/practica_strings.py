#Práctica Strings
#Objetivo
#Crear un generador de nombres de usuario con formato específico haciendo uso de objetos String y sus métodos en python.
#Instrucciones
#Crea una clase llamada GeneradorNombresUsuario que genere nombres de usuario únicos siguiendo un formato específico.
#La clase debe tener un método constructor que reciba el nombre, el apellido y el año de nacimiento del usuario.
#Implementa un método generar_nombre_usuario que:
#Utilice .lower() para convertir el nombre a minúsculas.
#Utilice .upper() para convertir el apellido a mayúsculas.
#Combine el nombre y apellido sin espacios entre ellos y añada el año de nacimiento al final.
#Añade un método validar_nombre_usuario que asegure que el nombre de usuario cumpla con los siguientes criterios:
#El nombre generado tenga al menos 8 caracteres de longitud (Pista: función len).
#El nombre generado tenga 4 números al final (Pista: función isdigit)
#Implementa un método mostrar_nombre_usuario que imprima el nombre de usuario generado si este pasa la validación. Si no es así, imprimirá por pantalla: El nombre de #usuario no cumple con los criterios de validación.
#Crea un objeto de la clase GeneradorNombresUsuario y llama a los métodos generar_nombre_usuario y mostrar_nombre_usuario
#Resultado esperado
#Nombre de usuario generado: santiagoHERNANDEZ1994
#Notas para el estudiante
#Para aprobar esta evaluación tu respuesta debe coincidir con los datos presentados en la sección "Resultado esperado".
#Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no son correctos, se desbloqueará la pestaña "Explicación de la solución" en la parte superior del #ejercicio. En esta pestaña puedes ver el código de solución de esta práctica.

nombre = "chirlett"
print(f"mi nombre es {nombre.upper()}")

class GeneradorNombresUsuario:
    def __init__(self, nombre, apellido, year):
        self.nombre = nombre
        self.apellido = apellido
        self.year = year
        
    def generar_nombre_usuario(self):
        nombre = self.nombre.lower()
        apellido = self.apellido.upper()
        return "".join([nombre, apellido, str(self.year)])
        
    def validar_nombre_usuario(self):
        nombre_usuario = self.generar_nombre_usuario()
        return len(nombre_usuario) >= 8 and nombre_usuario[-4:].isdigit()
    
    def mostrar_nombre_usuario(self):
        if self.validar_nombre_usuario():
            print(f"Nombre de usuario generado: {self.generar_nombre_usuario()}")
        else:
            print("El nombre de usuario no cumple con los criterios de validación.")
            
usuario = GeneradorNombresUsuario("santiago", "hernandez", 1994)
usuario.mostrar_nombre_usuario()