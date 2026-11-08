
from mipaquete import *

if __name__ == '__main__':
    mimodulo.funcion_mimodulo()
    mimodulo2.func_mimodulo2()

#lo paquetes deben agrupar los modulos que se relacionan
#no son al azar

#if __name__ == '__main__': 
#esta sentencia sirve para ejecutar codigo en python
#cuando ejecutas main.py directamente, Python 
# le pone a __name__ el valor "__main__", así que la condición 
# se cumple y se llama a planificar_proyecto(). 
# Si otro archivo hace import main, __name__ vale "main" y 
# la función no se ejecuta sola al importar. Es útil para 
# no disparar código por accidente.
