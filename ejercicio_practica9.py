#trabajando con Sets
#Práctica Sets
#Objetivo
#Crear un sistema de gestión de asistencia de estudiantes a clases universitarias mediante objetos Sets y sus métodos.
#Instrucciones
#Crea una clase llamada GestionAsistencia que administre la asistencia de estudiantes a diferentes 
# actividades universitarias.
#La clase debe tener un método constructor que inicialize dos atributos de instancia tipo set: asistentes_actividad_A y 
# asistentes_actividad_B, inicializados como sets vacíos. Estos atributos almacenarán los nombres de los estudiantes que 
# asistieron a las actividades A y B, respectivamente.
#Implementa un método añadir_asistente(self, actividad, estudiante) que utilice el método .add() para añadir el nombre 
# de un estudiante al set correspondiente de la actividad A o B. El método tendrá que comprobar a qué actividad pertenece de las dos.
#Añade un método asistencia_total(self) que utilice el método .union() para combinar los sets de asistentes de ambas 
# actividades y retorne el conjunto resultante, representando todos los estudiantes que asistieron a al menos una actividad.
#Implementa un método asistencia_comun(self) que utilice el método .intersection() para encontrar y retornar un set
#  de estudiantes que asistieron a ambas actividades.
#Implementa dos métodos diferencia_actividad_A(self) y diferencia_actividad_B(self) que utilicen el método .difference()
#  para encontrar y retornar estudiantes que asistieron exclusivamente a la actividad A o B, respectivamente.
#Ejecución del programa:
#Crea un objeto de la clase GestionAsistencia.
#Llama al método añadir_asistente con diferentes nombres de estudiantes y actividades a las que asisten (A o B).
#Llama al método asistencia_total e imprime por pantalla su resultado.
#Llama al método asistencia_comun e imprime por pantalla su resultado.
#Llama al método diferencia_actividad_A e imprime por pantalla su resultado.
#Llama al método diferencia_actividad_B e imprime por pantalla su resultado.
#Resultado esperado
#Asistentes actividad A: {'Ana', 'Juan'}
#Asistentes actividad B: {'Luis', 'Ana'}
#Asistencia total: {'Luis', 'Ana', 'Juan'}
#Asistencia común: {'Ana'}
#Diferencia actividad A: {'Juan'}
#Diferencia actividad B: {'Luis'}
#Notas para el estudiante
#Para aprobar esta evaluación tu respuesta debe coincidir con los datos presentados en la sección "Resultado esperado".
#Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no son correctos, se desbloqueará la pestaña "Explicación de la solución" en la parte superior del ejercicio. En esta pestaña puedes ver el código de solución de esta práctica.


class GestionAsistencia:
    "administar la asistencia de estudiantes a diferentes actividades universitarias"
    def __init__(self):
        self.asistentes_actividad_A = set()
        self.asistentes_actividad_B = set()

    def añadir_asistente(self, actividad, estudiante):
        if actividad == "A":
            self.asistentes_actividad_A.add(estudiante)
        elif actividad == "B":
            self.asistentes_actividad_B.add(estudiante)

    def asistencia_total(self):
        return self.asistentes_actividad_A.union(self.asistentes_actividad_B)

    def asistencia_comun(self):
        return self.asistentes_actividad_A.intersection(self.asistentes_actividad_B)

    def diferencia_actividad_A(self):
        return self.asistentes_actividad_A.difference(self.asistentes_actividad_B)

    def diferencia_actividad_B(self):
        return self.asistentes_actividad_B.difference(self.asistentes_actividad_A)

gestion = GestionAsistencia()
gestion.añadir_asistente("A", "Ana")
gestion.añadir_asistente("A", "Juan")
gestion.añadir_asistente("B", "Luis")
gestion.añadir_asistente("B", "Ana")
print(f"Asistentes actividad A: {gestion.asistentes_actividad_A}") 
print(f"Asistentes actividad B: {gestion.asistentes_actividad_B}") 
print(f"Asistencia total: {gestion.asistencia_total()}") 
print(f"Asistencia común: {gestion.asistencia_comun()}") 
print(f"Diferencia actividad A:{gestion.diferencia_actividad_A()}") 
print(f"Diferencia actividad B:{gestion.diferencia_actividad_B()}") 