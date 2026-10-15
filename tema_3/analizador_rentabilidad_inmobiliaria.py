#==========================
#Analizador de rentabilidad inmobiliaria
#==========================

#ITP = impuesto de transmisiones patrimoniales
tasas_itp = {
    "Madrid": 6.0,
    "Cataluña": 10.0,
    "Andalucía": 8.0,
    "Valencia": 10.0,
    "País Vasco": 4.0,
    "Galicia": 10.0,
    "Castilla y león": 8.0,
    "Castilla-La Mancha": 9.0,
    "Murcia": 8.0,
    "Aragón": 8.0,
    "Canarias": 6.5,
    "Extremadura": 8.0,
    "Asturias": 8.0,
    "Baleares": 8.0,
    "Cantabria": 10.0,
    "La Rioja": 7.0,
    "Navarra": 6.0,
    "Ceuta": 6.0,
    "Melilla": 6.0
}
def crear_propiedad(direccion, precio, metros, habitaciones, comunidad_autonoma, tipo_inmueble):
    """
    Crea un diccionario con toda la informacion de una propiedad

    retorna:
    dict: Diccionario con informacion completa de la propiedad
    """
    propiedad = {
        "direccion": direccion,
        "precio_compra": precio,
        "metros_cuadrados": metros,
        "habitaciones": habitaciones,
        "comunidad_autonoma": comunidad_autonoma,
        "tipo_inmueble": tipo_inmueble,
        "precio_por_m2": precio/ metros
    }
    return propiedad

def crear_financiamiento(entrada_porcentaje, tasa_anual, plazo_años, precio_total):
    """
    Crea un diccionario con la informacion de financiemiento
    retorno:
    dict: diccionario con los datos de financiamiento
    """
    entrada_monto = precio_total * (entrada_porcentaje / 100)
    monto_finaciado = precio_total - entrada_monto

    #calcular la cuota mensual (formula de amortizacion)
    tasa_mensual = (tasa_anual /100) /12
    num_pagos = plazo_años * 12
    cuota_mensual = monto_finaciado * (tasa_mensual * ((1 + tasa_mensual) ** num_pagos)) / (((1 + tasa_mensual)** num_pagos) - 1)

    financiamiento = {
        "entrada_porcentaje": entrada_porcentaje,
        "entrada_monto": entrada_monto,
        "monto_financiado": monto_finaciado,
        "tasa_anual": tasa_anual,
        "plazo_años": plazo_años,
        "cuota_mensual": cuota_mensual,
        "total_a_pagar": cuota_mensual * num_pagos
    }
    return financiamiento
def calcular_ibi(precio_compra, tipo_inmueble):
    """
    Calcula de IBI (impuesto sobre bienes inmuebles) anual que debe pagarse por la propiedad

    Paramteros:
    precio_compra (float): Precio de compra de la vivienda
    tipo_inmueble (str): "Urbano" o "Rústico"

    Retorna: 
    (float): IBI anual a pagar

    Las tasas de IBI son:

    Inmuebles urbanos: 0.428% (0.00428 en decimal)

    Inmuebles rústicos: 0.567% (0.00567 en decimal)
    Calcula el IBI: valor_catastral * tasa_ibi
    """
    valor_catastral = precio_compra * 0.70
    tasa_ibi = 0.00428 * (tipo_inmueble == "Urbano") + 0.00567 *(tipo_inmueble == "Rústico")

    return valor_catastral * tasa_ibi

def calcular_total_lista(lista_gastos):
    """
    Suma todos los gastos de una lista que cotiene tuplas

    Parametros: 
    lista_gastos (list): Lista de tuplas donde cada tupla es (concepto, monto)

    retorna:
    (float): Total de todos los gastos sumados
    """

    total = 0 
    total += lista_gastos[0][1] #primer gasto mensual
    total += lista_gastos[1][1] #segundo gasto mensual
    total += lista_gastos[2][1] #tercer gasto mensual
    return total
gastos = [("Comunidad", 80), ("Seguro", 30), ("Mantenimiento", 50)]
print(calcular_total_lista(gastos))

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
    Ingreso anual = renta mensual x meses ocupados
    Tasa de ocupación = (meses ocupados / 12) x 100
    """
    ingresos = {
        "renta_mensual": renta_mensual,
        "meses_ocupados": meses_ocupados,
        "ingreso_anual": renta_mensual * meses_ocupados,
        "tasa_ocupacion": (meses_ocupados/12)*100
    }
    return ingresos

def calcular_gastos_compra_iniciales(precio, comunidad_autonoma):
    """
    calcula gastos iniciales que debe pagar el comprador al adquirir la propiedad

    parametros:
    precio (float): Precio de compra de la propiedad
    comunidad_autonoma (str): Nombre de la comunidad autónoma (ej: "Madrid", "Cataluña")

    retorna:
    (tuple): Tupla con tres elementos: (impuesto_itp, notaria_registro, total)
    """
    
    impuesto_itp = precio * (tasas_itp[comunidad_autonoma] / 100)
    notaria_registro = precio * 0.015
    total = impuesto_itp + notaria_registro

    return (impuesto_itp, notaria_registro, total)

def calcular_metricas_rentabilidad(ingresos_anuales, gastos_anuales_operativos, gastos_anuales_totales, precio_propiedad, inversion_inicial):
    """
    calcula las metricas  mas importantes  para evaluar la rentabilidad de una inversion inmobiliaria

    Parametros: 
    ingresos_anuales (float): Ingresos totales por año
    gastos_anuales_operativos (float): Gastos operativos anuales (comunidad, seguro, mantenimiento, IBI)
    gastos_anuales_totales (float): Todos los gastos anuales (incluye hipoteca)
    precio_propiedad (float): Precio de compra de la propiedad
    inversion_inicial (float): Dinero invertido al inicio (entrada + gastos de compra)

    retorna: 
    (tuple): Tupla con cuatro métricas: (rentabilidad_bruta, rentabilidad_neta, cap_rate, roi_años)
    """
    beneficio_neto = ingresos_anuales - gastos_anuales_totales
    rentabilidad_bruta = (ingresos_anuales / precio_propiedad) * 100
    rentabilidad_neta = (beneficio_neto / inversion_inicial) * 100
    NOI = ingresos_anuales - gastos_anuales_operativos
    cap_rate = (NOI/ precio_propiedad)*100
    roi_años = inversion_inicial / beneficio_neto

    return (rentabilidad_bruta, rentabilidad_neta, cap_rate, roi_años)

def calcular_flujo_caja(ingresos_dict, gastos_mensuales_lista, cuota_hipoteca):
    """
    calcula el flujo de caja mensual 

    retorna: 
    tuple: (flujo mensual, flujo anual)
    """
    renta = ingresos_dict["renta_mensual"]
    gastos_mes = calcular_total_lista(gastos_mensuales_lista)

    flujo_mensual = renta - cuota_hipoteca -gastos_mes
    flujo_anual = flujo_mensual *12

    return (flujo_mensual, flujo_anual)

def evaluar_inversion(rentabilidad_neta, cap_rate, flujo_mensual):
    """
    Evalua la inversion y retorna tupla con puntiacion y recomendacion.

    Retorna:
    Tuple: (puntiacion, recomendacion, semaforo)
    """
    puntuacion = 0
    puntuacion += 40*(rentabilidad_neta >= 6)
    puntuacion += 30 *(cap_rate >=5)
    puntuacion += 30 * (flujo_mensual >0)

    #Recomendacion basada en puntuacion
    recomendacion = "EXCELENTE INVERSION" * (puntuacion >= 80) +\
    "Buena inversion" * (60 <= puntuacion <80) +\
    "Inversion moderada" *(40 <=puntuacion <60)+\
    "inversion arriesgada" *(puntuacion <40)

    semaforo = "🟢" * (puntuacion >= 70)+ "🟡" *(puntuacion<70)+ "🔴" *(puntuacion < 40)
    return (puntuacion, recomendacion, semaforo)

def solicitar_datos_propiedad():
    """
    Solicita al usuario los datos de la propiedad y retorna diccionario.
    
    Retorna:
    dict: Diccionario con información completa
    """
    print("\n" + "="*60)
    print("🏠 DATOS DE LA PROPIEDAD")
    print("="*60)
    
    direccion = input("\n📍 Dirección: ")
    precio = float(input("💰 Precio de compra (€): "))
    metros = float(input("📏 Metros cuadrados: "))
    habitaciones = int(input("🛏️  Número de habitaciones: "))
    tipo_inmueble = input("🏘️  Tipo de inmueble (Urbano/Rústico): ")
    
    # Mostrar comunidades autónomas disponibles
    print("\n🗺️  COMUNIDADES AUTÓNOMAS:")
    comunidades_list = list(tasas_itp)
    
    print(f"   {comunidades_list[0]}, {comunidades_list[1]}, {comunidades_list[2]}")
    print(f"   {comunidades_list[3]}, {comunidades_list[4]}, {comunidades_list[5]}")
    print(f"   {comunidades_list[6]}, {comunidades_list[7]}, {comunidades_list[8]}")
    print(f"   (y más...)")
    
    comunidad = input("\n🏛️  Comunidad Autónoma: ")
    
    propiedad = crear_propiedad(direccion, precio, metros, habitaciones, comunidad, tipo_inmueble)
    
    print("\n" + "="*60)
    print("💳 FINANCIAMIENTO")
    print("="*60)
    
    entrada_pct = float(input("\n💵 Porcentaje de entrada (%): "))
    tasa = float(input("📈 Tasa de interés anual (%): "))
    plazo = int(input("📅 Plazo en años: "))
    
    financiamiento = crear_financiamiento(entrada_pct, tasa, plazo, precio)
    
    print("\n" + "="*60)
    print("🏦 INGRESOS ESPERADOS")
    print("="*60)
    
    renta = float(input("\n💸 Renta mensual estimada (€): "))
    meses_ocup = int(input("📆 Meses ocupados al año (10-12): "))
    
    ingresos = crear_ingresos_alquiler(renta, meses_ocup)
    
    print("\n" + "="*60)
    print("💸 GASTOS MENSUALES")
    print("="*60)
    
    comunidad_gasto = float(input("\n🏢 Gastos de comunidad (€): "))
    seguro = float(input("🛡️  Seguro (mensual) (€): "))
    mantenimiento = float(input("🔧 Mantenimiento (mensual) (€): "))
    
    gastos_mes = [
        ("Gastos de comunidad", comunidad_gasto),
        ("Seguro", seguro),
        ("Mantenimiento", mantenimiento)
    ]
    
    print("\n" + "="*60)
    print("💸 GASTOS ANUALES EXTRAS")
    print("="*60)
    
    # Calcular IBI automáticamente
    ibi = calcular_ibi(precio, tipo_inmueble)
    print(f"\n🏛️  IBI calculado automáticamente: {ibi:,.2f}€")
    
    mant_extra = float(input("🔨 Mantenimiento extraordinario (anual) (€): "))
    
    gastos_anuales = [
        ("IBI (Impuesto Municipal)", ibi),
        ("Mantenimiento extraordinario", mant_extra)
    ]

    # Crear diccionario completo con todos los datos
    analisis_completo = {
        "propiedad": propiedad,
        "financiamiento": financiamiento,
        "ingresos": ingresos,
        "gastos_mensuales": gastos_mes,
        "gastos_anuales": gastos_anuales,
        "categorias_gasto": {"Hipoteca", "Mantenimiento", "Impuestos", "Seguros", "Comunidad"}, # Set de categorías de gasto
        "comunidades_disponibles": tasas_itp
    }
    
    return analisis_completo


def mostrar_reporte_completo(datos):
    """
    Genera el reporte completo usando el diccionario de datos.
    
    Parámetros:
    datos (dict): Diccionario con toda la información del análisis
    """
    # Extraer datos de los diccionarios anidados
    propiedad = datos["propiedad"]
    financ = datos["financiamiento"]
    ingresos = datos["ingresos"]
    gastos_mes = datos["gastos_mensuales"]
    gastos_anuales = datos["gastos_anuales"]
    
    print("\n\n" + "="*70)
    print("📊 ANÁLISIS DE RENTABILIDAD INMOBILIARIA")
    print("="*70)
    
    # INFORMACIÓN BÁSICA
    print(f"\n🏠 PROPIEDAD")
    print(f"   📍 Dirección: {propiedad['direccion']}")
    print(f"   💰 Precio: {propiedad['precio_compra']:,.0f}€")
    print(f"   📏 Superficie: {propiedad['metros_cuadrados']}m²")
    print(f"   🛏️  Habitaciones: {propiedad['habitaciones']}")
    print(f"   🏘️  Tipo: {propiedad['tipo_inmueble']}")
    print(f"   🏛️  Comunidad: {propiedad['comunidad_autonoma']}")
    print(f"   📐 Precio/m²: {propiedad['precio_por_m2']:,.2f}€")
    
    # FINANCIAMIENTO
    print(f"\n💳 FINANCIAMIENTO")
    print(f"   Entrada ({financ['entrada_porcentaje']}%): {financ['entrada_monto']:,.0f}€")
    print(f"   Monto financiado: {financ['monto_financiado']:,.0f}€")
    print(f"   Tasa: {financ['tasa_anual']}% anual")
    print(f"   Plazo: {financ['plazo_años']} años")
    print(f"   Cuota mensual: {financ['cuota_mensual']:,.2f}€")
    print(f"   Total a pagar: {financ['total_a_pagar']:,.0f}€")
    
    # GASTOS DE COMPRA
    imp, not_reg, total_compra = calcular_gastos_compra_iniciales(
        propiedad['precio_compra'],
        propiedad['comunidad_autonoma']
    )
    tasa_itp = datos["comunidades_disponibles"][propiedad['comunidad_autonoma']]
    print(f"\n📋 GASTOS INICIALES")
    print(f"   ITP ({tasa_itp}%): {imp:,.0f}€")
    print(f"   Notaría y registro: {not_reg:,.0f}€")
    print(f"   Total gastos compra: {total_compra:,.0f}€")
    
    inversion_inicial = financ['entrada_monto'] + total_compra
    print(f"\n💵 INVERSIÓN INICIAL TOTAL: {inversion_inicial:,.0f}€")
    
    # INGRESOS
    print(f"\n📈 INGRESOS PROYECTADOS")
    print(f"   Renta mensual: {ingresos['renta_mensual']:,.0f}€")
    print(f"   Meses ocupados: {ingresos['meses_ocupados']}/12")
    print(f"   Tasa ocupación: {ingresos['tasa_ocupacion']:.1f}%")
    print(f"   Ingreso anual: {ingresos['ingreso_anual']:,.0f}€")
    
    # GASTOS MENSUALES
    print(f"\n💸 GASTOS MENSUALES")
    print(f"   {gastos_mes[0][0]}: {gastos_mes[0][1]:,.0f}€")
    print(f"   {gastos_mes[1][0]}: {gastos_mes[1][1]:,.0f}€")
    print(f"   {gastos_mes[2][0]}: {gastos_mes[2][1]:,.0f}€")
    total_gastos_mes = calcular_total_lista(gastos_mes)
    print(f"   Subtotal mensual: {total_gastos_mes:,.0f}€")
    
    # GASTOS ANUALES
    print(f"\n💸 GASTOS ANUALES EXTRAS")
    print(f"   {gastos_anuales[0][0]}: {gastos_anuales[0][1]:,.0f}€")
    print(f"   {gastos_anuales[1][0]}: {gastos_anuales[1][1]:,.0f}€")
    gastos_anuales_extra = gastos_anuales[0][1] + gastos_anuales[1][1]
    
    total_gastos_anuales = (total_gastos_mes * 12) + gastos_anuales_extra + (financ['cuota_mensual'] * 12)
    total_gastos_anuales_operativos = (total_gastos_mes * 12) + gastos_anuales_extra # sin hipoteca
    print(f"   Total gastos anuales (con hipoteca): {total_gastos_anuales:,.0f}€")
    
    # CATEGORÍAS
    print(f"\n🏷️  CATEGORÍAS DE GASTOS")
    categorias_lista = sorted(datos["categorias_gasto"])
    print(f"   {', '.join(categorias_lista)}")
    
    # FLUJO DE CAJA
    flujo_mes, flujo_año = calcular_flujo_caja(
        ingresos,
        gastos_mes,
        financ['cuota_mensual']
    )
    print(f"\n💰 FLUJO DE CAJA")
    print(f"   Mensual: {flujo_mes:,.2f}€")
    print(f"   Anual: {flujo_año:,.2f}€")
    
    # RENTABILIDAD
    rent_bruta, rent_neta, cap, roi = calcular_metricas_rentabilidad(
        ingresos['ingreso_anual'],
        total_gastos_anuales_operativos,
        total_gastos_anuales,
        propiedad['precio_compra'],
        inversion_inicial
    )
    
    print(f"\n📊 INDICADORES DE RENTABILIDAD")
    print(f"   Rentabilidad bruta: {rent_bruta:.2f}%")
    print(f"   Rentabilidad neta: {rent_neta:.2f}%")
    print(f"   CAP Rate: {cap:.2f}%")
    print(f"   Recuperación inversión: {abs(roi):.1f} años")
    
    # EVALUACIÓN
    puntos, recomendacion, semaforo = evaluar_inversion(rent_neta, cap, flujo_mes)
    
    print(f"\n🎯 EVALUACIÓN FINAL")
    print(f"   Puntuación: {puntos}/100")
    print(f"   {semaforo} {recomendacion}")
    
    print("\n" + "="*70)



# ============================================
# PROGRAMA PRINCIPAL
# ============================================

cabecera = """
╔══════════════════════════════════════════════════════════════════╗
║          🏢 ANALIZADOR DE INVERSIÓN INMOBILIARIA 🏢              ║
║                                                                  ║
║              Análisis de rentabilidad para alquiler              ║
║                          España                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
print(cabecera)
    
print("\n💡 Bienvenido al analizador de inversión inmobiliaria")
print("    Este sistema te ayudará a evaluar si comprar una vivienda")
print("    para alquilarla es una buena inversión.\n")
    
# Solicitar datos al usuario
datos_completos = solicitar_datos_propiedad()
    
# Generar reporte
mostrar_reporte_completo(datos_completos)
    
# Notas finales
print("\n💡 NOTAS IMPORTANTES:")
print("   • Este análisis usa estimaciones generales")
print("   • Rentabilidad neta >6% = Excelente | 4-6% = Buena | <4% = Baja")
print("   • CAP Rate >5% = Recomendado para mercados estables")
print("\n✨ ¡Gracias por usar el Analizador! ✨\n")