import math


def circle_area(radius):
    """Вычисляет площадь круга по радиусу."""
    return math.pi * radius**2


def triangle_area(a, b, c):
    """Вычисляет площадь треугольника по трем сторонам, используя формулу Герона."""
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def is_right_triangle(a, b, c):
    """Проверяет является ли треугольник прямоугольным"""
    sides = [a, b, c]
    sides.sort()
    return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)
