# Making Library of volume and Area of Figures
import math

# Cube's volume
class Cube:
    def __init__(self):
        self.length = float(input('Введите длину: '))

    def volume(self):
        v = math.pow(self.length, 3)
        print(f'Объём куба(V) = {self.length} * {self.length} * {self.length} = {v:<5}')

# Sphere's volume
class sphere:
    def __init__(self):
        self.radius = float(input('Введите радиус: '))

    def volume(self):
        v = 4 * math.pi * math.pow(self.radius, 3) / 3
        print(f'Объём сферы(V) = 4 * Pi * {self.radius} / 3 = {v:<5}')

# Parellelogram's area
class parallelogram:
    def __init__(self):
        self.base = float(input('Введите основание: '))
        self.height = float(input('Введите высоту: '))

    def Area(self):
        s = self.base * self.height
        print(f'Площадь параллелограмма(S) = {self.base} * {self.height} = {s:<5}')

# Triangle's area
class triangle:
    def __init__(self):
        self.base = float(input('Введите основание: '))
        self.height = float(input('Введите высоту: '))

    def Area(self):
        s = self.base * self.height * 0.5
        print(f'Площадь параллелограмма(S) = {self.base} * {self.height} * 0.5 = {s:<5}')

# Rhombus's area
class rhombus:
    def __init__(self):
        self.diagonal1 = float(input('Введите первую диагональ: '))
        self.diagonal2 = float(input('Введите вторую диагональ: '))

    def Area(self):
        s = 0.5 * self.diagonal1 * self.diagonal2
        print(f'Площадь ромба(S) = 0.5 * {self.diagonal1} * {self.diagonal2} = {s:<5}')

# Trapezoid's area
class trapezoid:
    def __init__(self):
        self.base1 = float(input('Введите первое основание: '))
        self.base2 = float(input('Введите второе основание: '))
        self.height = float(input('Введите высоту: '))

    def Area(self):
        s = (self.base1 + self.base2) / 2 * self.height
        print(f'Площадь трапеции(S) = ( {self.base1} + {self.height} ) / 2 * {self.height} = {s:<5}')

# Circle's area
class circle:
    def __init__(self):
        self.radius = float(input('Введите радиус: '))

    def Area(self):
        s = math.pi * math.pow(self.radius, 2)
        print(f'Площадь круга(S) = {math.pi} * {math.pow(self.radius, 2)} = {s:<5}')

# Square's area
class square:
    def __init__(self):
        self.side = float(input('Введите любую сторону у квадрата: '))

    def Area(self):
        s = math.pow(self.side, 2)
        print(f'Площадь трапеции(S) = {self.side} ** 2 = {s:<5}')

# Rectangle's area
class rectangle:
    def __init__(self):
        self.side1 = float(input('Введите первую сторону: '))
        self.side2 = float(input('Введите другую сторону: '))

    def Area(self):
        s = self.side1 * self.side2
        print(f'Площадь прямоугольника(S) = {self.side1} * {self.side2} = {s:<5}')

# Cylinder's volume
class cylinder:
    def __init__(self):
        self.radius = float(input('Введите радиус: '))
        self.height = float(input('Введите высоту: '))

    def volume(self):
        v = math.pi * math.pow(self.radius, 2) * self.height
        print(f'Объём цилиндра(V) = {math.pi} * {math.pow(self.radius, 2)} * {self.height} = {v:<5}')