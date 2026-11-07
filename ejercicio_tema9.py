class SistemaCalificaciones:
    "administrar calificaciones de estudiantes en el sistema"
    def __init__(self):
       self.calificaciones = []

    def añadir_calificacion(self, calificacion):
        self.calificacion = calificacion
        self.calificaciones.append(calificacion)

    def mostrar_calificaciones(self):
        for nota in self.calificaciones:
            print(nota)

    def calificacion_promedio(self):
        if len(self.calificaciones)==0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def ordenar_calificaciones(self):
        self.calificaciones.sort()

sistema = SistemaCalificaciones()

for nota in [8, 9.5, 7, 10]:
    sistema.añadir_calificacion(nota)

print("Calificaciones originales:")
sistema.mostrar_calificaciones()

print(f"Promedio: {sistema.calificacion_promedio()}")

sistema.ordenar_calificaciones()
print("Calificaciones ordenadas:")
sistema.mostrar_calificaciones()
       