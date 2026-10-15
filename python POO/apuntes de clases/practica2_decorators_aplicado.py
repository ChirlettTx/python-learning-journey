"""
Práctica Decorators
Objetivo

Implementa un "Sistema de notificaciones para eventos en redes sociales". 
Desarrolla un programa que simule el envío de notificaciones de nuevos eventos
 en redes sociales utilizando decorators en Python.



Instrucciones

Implementa una clase NotificadorRedSocial con un atributo de instancia evento que
 almacene la descripción del evento a notificar, por ejemplo "Lanzamiento de un nuevo libro".

Añade el método notificar_evento a la clase, que acepte un argumento plataforma 
(Twitter, Instagram o Facebook) y utilice declaraciones if/elif para imprimir mensajes de 
notificación adecuados para cada plataforma soportada. En caso de que la plataforma no
 esté soportada, debe imprimir "Plataforma no soportada". Mensajes de notificación:

En el caso de Twitter: Tweet: [evento]
En el caso de Instagram: Instagram Story: [evento]
En el caso de Facebook: Post en Facebook: [evento]
Fuera de la clase, define un decorator llamado formato_notificacion que imprima mensajes de ***** NUEVO EVENTO 
en {plataforma} ***** y ***** FIN DEL EVENTO en {plataforma} *****,
alrededor del mensaje de notificación específico de cada plataforma, proporcionado por la función notificar_evento.
Aplica Syntactic Sugar sobre la función notificar_evento para incluir el decorator formato_notificacion.
Fuera de la clase, crea una instancia de NotificadorRedSocial y simula el envío de notificaciones a varias plataformas 
(Twitter, Instagram, LinkedIn, Facebook).



Resultado esperado
***** NUEVO EVENTO en Twitter *****
Tweet: Lanzamiento de un nuevo libro
***** FIN DEL EVENTO en Twitter *****
***** NUEVO EVENTO en Instagram *****
Instagram Story: Lanzamiento de un nuevo libro
***** FIN DEL EVENTO en Instagram *****
***** NUEVO EVENTO en Facebook *****
Post en Facebook: Lanzamiento de un nuevo libro
***** FIN DEL EVENTO en Facebook *****
***** NUEVO EVENTO en LinkedIn *****
Plataforma no soportada
***** FIN DEL EVENTO en LinkedIn *****
Notas para el estudiante
Para aprobar esta evaluación tu respuesta debe coincidir con los datos presentados en la sección "Resultado esperado".
Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no son correctos, se desbloqueará la pestaña "Explicación 
de la solución" en la parte superior del ejercicio. En esta pestaña puedes ver el código de solución de esta práctica.
"""
#Este desarrollo esta mal, se debe revisar el otro archivo de correccion
def formato_notificacion(func):
   def wrapper(self, plataforma):
       print(f"***** NUEVO EVENTO en {plataforma} *****")
       func(self, plataforma)
       print(f"***** FIN DEL EVENTO en {plataforma} *****")
   return wrapper

class NotificadorRedSocial():
    def __init__(self, evento):
        self.evento = evento

    @formato_notificacion    
    def notificar_evento(self, plataforma): 
        if plataforma == "Twitter":
            print(f"Tweet: {self.evento}")
        elif plataforma == "Instagram":
            print(f"Story: {self.evento}")
        elif plataforma == "Facebook": 
            print(f"Post en Facebook: {self.evento}")
        else:
            print("Plataforma no soportada")
            
notificador = NotificadorRedSocial("Lanzamiento de un nuevo libro")
notificador.notificar_evento("Twitter")
notificador.notificar_evento("Instagram")
notificador.notificar_evento("Facebook")
notificador.notificar_evento("LinkedIn")

