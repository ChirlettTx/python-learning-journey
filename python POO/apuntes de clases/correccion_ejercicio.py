#Resolución del ejercicio A continuación se presenta el código en Python que resuelve el ejercicio propuesto. #
# Copia y pega el código en el editor para visualizarlo mejor.

 

def formato_notificacion(func):
    """
    Decorator que agrega formato de notificación a las funciones que envían notificaciones.
 
    Este decorador imprime un encabezado y pie de página alrededor de la salida de la función decorada,
    indicando el inicio y fin de un evento en una plataforma específica.
 
    Args:
        func (Callable): La función a decorar, que debe aceptar al menos un argumento 'plataforma'.
 
    Returns:
        Callable: La función envuelta con la funcionalidad de formato de notificación.
    """
    def wrapper(self, plataforma):
        print(f"***** NUEVO EVENTO en {plataforma} *****")
        func(self, plataforma)
        print(f"***** FIN DEL EVENTO en {plataforma} *****\n")
    return wrapper
 
class NotificadorRedSocial:
    """
    Clase para enviar notificaciones de eventos a diferentes plataformas de redes sociales.
    """
 
    def __init__(self):
        """
        Inicializa la clase NotificadorRedSocial con el evento a notificar.
        """
        self.evento = "Lanzamiento de un nuevo libro"
    
    @formato_notificacion
    def notificar_evento(self, plataforma):
        """
        Envía una notificación del evento a la plataforma especificada.
 
        Args:
            plataforma (str): La plataforma de redes sociales a la que se enviará la notificación.
                Las plataformas soportadas son Twitter, Instagram y Facebook.
        """
        if plataforma == "Twitter":
            print(f"Tweet: {self.evento}")
        elif plataforma == "Instagram":
            print(f"Instagram Story: {self.evento}")
        elif plataforma == "Facebook":
            print(f"Post en Facebook: {self.evento}")
        else:
            print("Plataforma no soportada")
 
 
# Simulación de envío de notificaciones
notificador = NotificadorRedSocial()
plataformas = ["Twitter", "Instagram", "Facebook", "LinkedIn"]
for plataforma in plataformas:
    notificador.notificar_evento(plataforma)
