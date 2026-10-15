def crear_ingresos_alquiler(renta_mensual, meses_ocupados):
    """
    crea un diccionario con informacion completa sobre los ingresos por alquiler

    Parametro:
    renta_mensual (float): Renta que se cobra al mes
    meses_ocupados (int): Meses al año que la propiedad está alquilada (normalmente entre 1 y 12)

    retorna:
    (dict): Diccionario con las claves:
    "renta_mensual": La renta mensual
    "meses_ocupados": Los meses ocupados
    "ingreso_anual": Ingreso total al año (renta x meses)
    "tasa_ocupacion": Porcentaje de ocupación anual
    
    Cálculos necesarios:
    Ingreso anual = renta mensual × meses ocupados
    Tasa de ocupación = (meses ocupados / 12) × 100
    """

    ingreso_anual = renta_mensual * meses_ocupados
    tasa_ocupacion = (meses_ocupados/12)*100

    ingresos = {
        "renta_mensual": renta_mensual,
        "meses_ocupados": meses_ocupados,
        "ingreso_anual": ingreso_anual,
        "tasa_ocupacion": tasa_ocupacion
    }
    return ingresos
print(crear_ingresos_alquiler(1000, 10))