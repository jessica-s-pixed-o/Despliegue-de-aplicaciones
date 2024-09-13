# Función para calcular el área de un rectángulo
def area_rectangulo(longitud, ancho):
    return longitud * ancho

# Ejemplo de uso
longitud = float(input("Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))

area = area_rectangulo(longitud, ancho)
print(f"El área del rectángulo es: {area}")
