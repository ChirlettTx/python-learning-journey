from calculos_arquitectonicos import area_rectangulo, volumen_cilindro, area_circulo

def planificar_proyecto():
    print("---------- Informe proyecto ----------")
    print(f"Área de la sala principal: {area_rectangulo(20,15)} metros cuadrados.")
    print(f"Volumen de la piscina: {volumen_cilindro(5,2)} metros cúbicos.")
    print(f"Área del jardín circular: {area_circulo(10)} metros cuadrados.")
    print("--------------------------------------")

if __name__ == "__main__":
    planificar_proyecto()