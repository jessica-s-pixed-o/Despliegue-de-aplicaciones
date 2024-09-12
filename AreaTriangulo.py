def calcular_area_triangulo(b, h):
    return b * h / 2

b = float(input("Ingresa la base del triángulo: "))
h = float(input("Ingresa la altura del triángulo: "))
area = calcular_area_triangulo(b, h)

print(f"El área del triángulo de {b} cm x {h} cm es de: {area:.2f} cm^2")