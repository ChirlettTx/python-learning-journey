def cabecera():
    """Muestra la cabecera de la aplicacion"""
    titulo = r"""
   _____                        _______              
  / ____|                      |__   __|             
 | |  __  __ _ _ __ ___   ___ _ __| | __ _  __ _ ___ 
 | | |_ |/ _` | '_ ` _ \ / _ \ '__| |/ _` |/ _` / __|
 | |__| | (_| | | | | | |  __/ |  | | (_| | (_| \__ \
  \_____|\__,_|_| |_| |_|\___|_|  |_|\__,_|\__, |___/
                                            __/ |    
                                           |___/  
"""
    print(titulo)

def crear_tag_basico(nombre):
    """
    Cea un gamertag basico usando las primeras 4 letras.
    Párametro:
    nombre (str): nombre del usuario

    retorna:
    str: Gamertag básico
    """
    tag=nombre[:4]
    return tag

def crear_tag_invertido(nombre):
    """
    Crear un gamertag invirtiendo el nombre completo.

    parametro: 
    nombre(str): nombre del usuario

    return: 
    str:nombre invertido
    """
    tag=nombre[::-1]
    return tag

def crear_tag_intercalado(nombre, apellido):
    """
    crear un gamertag combinando letras del nombre y apellido 

    Parametros: 
    nombre(str): el nombre del usuario
    apellido(str): el apellido del usuario

    return:
    none(imprime directamente)
    """
    #primera letra del nombre
    inicial_nombre = nombre[0]
    #primera letra del apellido
    inicial_apellido=apellido[0]
    #resto del nombre
    resto_nombre= nombre[1:]
    #resto del apellido
    resto_apellido= apellido[1:]

    print("3. TAG INTERCALADO: ", inicial_nombre, inicial_apellido, resto_nombre, resto_apellido, sep="")


def crear_tag_elite(nombre):
    """
    crear un gamertag "elite" usando el inicio y final del nombre 
    ej: "santiago" -> "Sago"

    Parametro:
    nombre(srt): El nombre del usuario

    retorna:
    None(imprime directamente)
    """
    #Primeras 2 letras
    inicio = nombre[:2]
    #ultimas letras
    final= nombre[-2:]

    print("4, TAG ELITE: ", inicio, final, sep="")
    
def crear_tag_con_numero(nombre, numero_favorito):
    """
    Crear un gamertag añadiendo numero al final.

    Parametros:
    nombre(str): el nombre del usuario
    numero_favorito (int): el numero favorito del usuario

    retorna:
    None(imprime directamente)
    """
    print("5. TAG CON NUMERO: ",nombre[:5], numero_favorito, sep="")

def mostrar_estadisticas(nombre):
    """
    Muestra estadisticas del nombre proporcionado

    Parametro:
    nombre(str):el nombre ha analizar

    retorna:
    None(imprime directamenta)
    """
    print("\n estadisticas de tu nombre")
    print("nombre completo: ", nombre, sep="")
    longitud_nombre= len(nombre)
    print("Longitud del nombre: ", longitud_nombre, sep="")
    print("Primera letra: ", nombre[0], sep="")
    print("Ultima letra: ", nombre[-1], sep="")

def generar_todas_opciones(nombre, apellido, numero):
    """
    Genera y muestra todas las opciones de gamertags.

    Parametro:
    nombre(str): nombre del usuario
    apellido(str): Apellido del usuario
    numero(int): numero favorito

    retorna:
    None(imprime directamente)
    """
    print("\n===================================")
    print("🎯​ Tus opciones de Gamertag: ")
    print("=====================================")

    tag_basico = crear_tag_basico(nombre)
    print("\n1. TAG BASICO:", tag_basico)
    print("2. TAG INVERTIDO:", crear_tag_invertido(nombre))
    crear_tag_intercalado(nombre, apellido)
    crear_tag_elite(nombre)
    crear_tag_con_numero(nombre, numero)

    print("\n==================")


#==========================
#Aplicacion principal
#==========================

#Mostrar cabecera
cabecera()

#solicitar datos al usuario
nombre = input("\n 👤​ Introduce tu nombre: ")
apellido= input("🫆​  introduce tu apellido: ")
numero = input("📈​ Introduce tu numero favorito: ")

#mostrar estadisticas del nombre
mostrar_estadisticas(nombre)

#generar y mostrar todas las opciones de gamertag
generar_todas_opciones(nombre, apellido, numero)

print("\n 🌟​ Elige tu favorito y conquista el mundo gamer 🌟​")
