
#Práctica Tuplas
#Objetivo

#Implementa un analizador de datos de ventas haciendo uso 
#de objetos de tipo Tupla y sus métodos en Python.

#Instrucciones

#Crea una clase llamada AnalisisVentas que se enfoque en el a
# nálisis de una serie de datos de ventas almacenados en una tupla.
#El constructor de la clase debe recibir una tupla datos_ventas que 
# contenga las cifras de ventas (como números enteros o flotantes) de diferentes productos ordenadas históricamente. Ej: (100, 150, 150, 50, 250, 300, 100, 350, 200, 200, 150)
#Implementa un método venta_maxima que utilice el método .index() y 
# la función max() para encontrar el índice de la cifra de venta más alta en la tupla (es decir, que número de venta fue) y 
# retorne tanto el índice como el valor de esa venta máxima.
#Implementa un método venta_minima que encuentre el índice y el valor de la cifra de venta más baja en la tupla y los retorne.
#Implementa un método frecuencia_venta, que reciba como argumento una cifra de venta (venta) y 
# ue utilice el método .count() para contar cuántas veces aparece en la tupla y retorne ese conteo.
#Ejecución del programa:
#Crea una tupla con diversas ventas.
#Crea un objeto de la clase AnalisisVentas con la tupla creada.
#Llama a las funciones venta_maxima y venta_minima imprimiendo su resultado por pantalla.
#Llama a la función frecuencia_venta con una venta en concreto e imprime su resultado por pantalla.

#Resultado esperado
#Ventas totales: (100, 150, 150, 50, 250, 300, 100, 350, 200, 200, 150)
#La venta máxima tiene el índice 7 y es 350.
#La venta mínima tiene el índice 3 y es 50.
#Frecuencia de la venta por un valor de 200 es 2.
#Notas para el estudiante
#Para aprobar esta evaluación tu respuesta debe coincidir con los datos presentados en la sección "Resultado esperado".
#Si pulsas tres veces sobre "Ejecutar Pruebas" y los resultados no son correctos, 
# se desbloqueará la pestaña "Explicación de la solución" en la parte superior del ejercicio. 
# En esta pestaña puedes ver el código de solución de esta práctica.



class AnalisisVentas:
    def __init__(self, datos_ventas):
        self.datos_ventas = datos_ventas
        
    def venta_maxima(self):
        maxima = max(self.datos_ventas)
        return self.datos_ventas.index(maxima), maxima

    def venta_minima(self):
        minima = min(self.datos_ventas)
        return self.datos_ventas.index(minima), minima

    def frecuencia_venta(self,venta):
        return self.datos_ventas.count(venta)



analisis = AnalisisVentas((100, 150, 150, 50, 250, 300, 100, 350, 200, 200, 150))
indice_max, valor_max = analisis.venta_maxima()
indice_min, valor_min = analisis.venta_minima()
print(f" La venta máxima tiene el  índice {indice_max} y es {valor_max}")
print(f" La venta mínima tiene el  índice {indice_min} y es {valor_min}")
print(f" Frecuencia de la venta por un valor de 200 es {analisis.frecuencia_venta(200)}")
