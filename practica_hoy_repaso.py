#con titulo
class RegistroPuntos:
    def __init__(self):
        self.puntos = {}
    def sumar_puntos(self, jugador, cantidad):
        if jugador in self.puntos:
            self.puntos[jugador] = self.puntos.get(jugador) + cantidad
        else:
            self.puntos[jugador] = cantidad
    def consultar_puntos(self, jugador):
        return self.puntos.get(jugador, " jugador no registrado")

    def mostrar_ranking(self):
        print("=== Ranking ===")
        for key, valor in self.puntos.items():
            print(f"{key}: {valor}")
        print("===============")

    def eliminar_jugador(self,jugador):
        if jugador in self.puntos:
            self.puntos.pop(jugador)

    def total_jugadores(self):
        participantes = self.puntos
        return len(participantes)

        
r = RegistroPuntos()
r.sumar_puntos("Ana", 10)
r.sumar_puntos("Luis", 5)
r.sumar_puntos("Ana",7)
print(r.consultar_puntos("Ana"))
print(r.consultar_puntos("Pedro"))
r.mostrar_ranking()
r.eliminar_jugador("Luis")
r.mostrar_ranking()
print(f"el total de jugadores es: {r.total_jugadores()}")