import math

def calcular_area_circulo(radio):
    # Fórmula del área de un círculo: A = π * r^2
    area = math.pi * radio ** 2
    return area

# Solicitar el radio al usuario
radio = float(input("Introduce el radio del círculo: "))

# Calcular y mostrar el área
area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area:.2f}")
