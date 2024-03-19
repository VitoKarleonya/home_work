def calculate_triangle_area(a, b, c):
    # Полупериметр
    p = (a + b + c) / 2
    # Формула Герона для вычисления площади треугольника
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area

a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))

triangle_area = calculate_triangle_area(a, b, c)
print("Площадь треугольника:", triangle_area)
