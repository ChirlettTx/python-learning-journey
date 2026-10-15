class coche:
    def __init__(self, vel_maxima, consumo_medio):
        self.vel_maxima = vel_maxima
        self.con_medio = consumo_medio

    def velocidad_maxima(self):
        """Este metodo devuelve la velocidad maxima del coche"""
        print("La velocidad maxima del coche es de: ", self.vel_maxima,"km/h")

    def consumo_medio(self):
        print("El consumo medio del coche es de: ", self.con_medio,"km/litro")



bwn = coche(170, 10)
bwn.velocidad_maxima()
bwn.consumo_medio()

renaul = coche(250, 14)
renaul.velocidad_maxima()
renaul.consumo_medio()

#### para lo siguiente sera con el uso del metodo __init__() el cual se utiliza
#  para inicializar los atributos de la clase
#### en este caso se utiliza para inicializar la velocidad maxima del coche

