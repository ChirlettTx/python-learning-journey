#==========================================
# Calculadora de fitness y salud personal
#==========================================

def calcular_imc(peso_kg, altura_m):
    """
    calclula el indice de masa corporal (IMC)

    formula: IMC = peso / (altura^2)

    parametros: 
    peso_kg(float): peso en kilogramos
    altura_m(float): Altura en metros

    Retorna: 
    float: el IMC calculado
    """
    imc = peso_kg / (altura_m**2)
    return imc

def es_peso_saludable(imc):
    """
    determina si el IMC esta en rango saludable (18.5 y 24.9)

    parametro:
    imc (float): indice de masa corporal

    retorna:
    bool: True si esta en rango saludable, False si no
    """
    # Operadores de comparacion y logicos
    return imc >= 18.5 and imc <= 24.9

def tiene_sobrepeso(imc):
    """
    Descripción: Determina si una persona tiene sobrepeso según su IMC.

    Criterio médico: Se considera sobrepeso cuando el IMC es mayor o igual a 25.

    Paramentro: 
    imc(float): el indice de masa corporal calculado

    return:
    true: si hay sobrepeso (IMC >= 25)
    False: si no hay sobre peso (IMC<25)
    """
    return imc >= 25

def tiene_bajo_peso(imc):
    """
    Descripción: Determina si una persona tiene bajo peso según su IMC.

    Criterio médico: Se considera bajo peso cuando el IMC es menor a 18.5.

    Parámetro:

    imc (float): El Índice de Masa Corporal calculado

    Debe retornar:

    True si hay bajo peso (IMC < 18.5)

    False si no hay bajo peso (IMC ≥ 18.5)
    """
    return imc < 18.5

def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    """
    Descripción: Calcula las calorías diarias recomendadas usando la Fórmula de Harris-Benedict.

    Fórmulas médicas:

    Para hombres: 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)

    Para mujeres: 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)

    Parámetros:

    peso_kg (float): Peso en kilogramos

    altura_cm (float): Altura en centímetros

    edad (int): Edad en años

    es_hombre (bool): True si es hombre, False si es mujer
    """

    calorias_hombre  = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
    calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)
    
    # usa el hecho de que True = 1 y false = 0
    return es_hombre * calorias_hombre + (1 - es_hombre) * calorias_mujer

def calcular_agua_diaria(peso_kg):
    """
    Descripción: Calcula los litros de agua recomendados al día.
    Recomendación médica: Se recomienda beber 35 mililitros de agua por cada kilogramo de peso corporal.

    Parámetro:
    peso_kg (float): Peso en kilogramos

    Debe retornar:
    (float): Litros de agua recomendados
    """
    return (peso_kg * 35)/1000

def calcular_ritmo_cardiaco_maximo(edad):
    """
    Descripción: Calcula el ritmo cardíaco máximo recomendado durante ejercicio.

    Fórmula médica: 220 - edad

    Parámetro:

    edad (int): Edad en años

    Debe retornar:

    (int): Pulsaciones por minuto máximas recomendadas
    """
    return 220 - edad

def generar_reporte_completo(nombre, peso, altura, edad, es_hombre):
    """
    Genera un reporte completo de salud y fitnes
    """
    print("="*60)
    print(f"REPORTE DE FITNESS Y SALUD - {nombre}")
    print("="*60)

    #calculos
    imc =calcular_imc(peso, altura)
    calorias = calcular_calorias_diarias(peso, altura, edad, es_hombre)
    agua = calcular_agua_diaria(peso)
    fc_max = calcular_ritmo_cardiaco_maximo(edad)

    #mostrar infomacion básica
    print("\n 👤​ DATOS PERSONALES: ")
    print(f"    Peso: {peso} kg" )
    print(f"    Altura: {altura} m")
    print(f"    Edad: {edad} años")
    print(f"    ¿Hombre?: {es_hombre}")

    #IMC y evaluacion
    print("\n 💪​ indice de masa corporal (IMC):")
    print(f"    tu IMC: {round(imc,2)}")
    print(f"    ¿Peso saludable? {es_peso_saludable(imc)}")
    print(f"    ¿sobrepeso? {tiene_sobrepeso(imc)}")
    print(f"    ¿Bajo peso?: {tiene_bajo_peso(imc)}")

    #calorias
    print("\n Nutrición:")
    print(f"    calorias diarias recomendadas: {round(calorias, 0)} kcal")
    print(f"    agua diaria recomendada: {round(agua,2)} litros")

    #cardio
    print("\n Zona cardiaca:")
    print(f"    Frecuencia cardiaca maxina: {fc_max} bpm")
    print(f"    Zona de cardio optima: {round(fc_max*0.6, 0)} - {round(fc_max*0.8,0)} bpm")

    print("\n" + "="*60)

#=======================
# Programa principal
#=======================

cabecera = """
    Calculadora de Fitness y Salud personal 
    Descubre tus metricas de salud optimas!
"""
print(cabecera)

#solicitar los datos al usuario
nombre = input("¿Cual es tu nombre? ")
peso = float(input(" ¿cuanto pesas?(kg): "))
altura = float(input("¿Cuanto mides? (metros, ej: 1.75): "))
edad = int(input("¿Cuantos años tienes? "))
sexo = input("¿Eres hombre o mujer? (H/M): ")

#convertir sexo en booleano

es_hombre = sexo == "H" or sexo == "h" or sexo == "hombre"

#generar reporte
generar_reporte_completo(nombre, peso, altura, edad, es_hombre)

print("\n ¡Cuida tu salud!")