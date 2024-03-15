import math


class Figure:
    def calculate_area(self):
        raise NotImplementedError("Метод должен быть реализован")


class Circle(Figure):
    def __init__(self, radius):
        self.__set_radius(radius)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__set_radius(radius)

    def __set_radius(self, radius):
        if radius < 0:
            raise Exception("некорректное значение: радиус должен быть больше нуля")
        else:
            self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.__sides = [side1, side2, side3]
        self.__side1 = self.__set_side(side1, self.__sides)
        self.__side2 = self.__set_side(side2, self.__sides)
        self.__side3 = self.__set_side(side3, self.__sides)

    def __set_side(self, side, sides):
        sides.sort()
        if side <= 0 or sides[0] + sides[1] <= sides[2]:
            raise Exception("некорректное значение")
        self.__sides = sides
        return side

    @property
    def side1(self):
        return self.__side1

    @side1.setter
    def side1(self, side):
        sides = [side, self.__side2, self.__side3]
        self.__side1 = self.__set_side(side, sides)

    @property
    def side2(self):
        return self.__side2

    @side2.setter
    def side2(self, side):
        sides = [side, self.__side1, self.__side3]
        self.__side2 = self.__set_side(side, sides)

    @property
    def side3(self):
        return self.__side3

    @side3.setter
    def side3(self, side):
        sides = [side, self.__side2, self.__side1]
        self.__side3 = self.__set_side(side, sides)

    def calculate_area(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def is_right_triangle(self):
        return math.isclose(self.__sides[0] ** 2 + self.__sides[1] ** 2, self.__sides[2] ** 2)


class FigureManager:
    @staticmethod
    def calculate_area(figure):
        return figure.calculate_area()


if __name__ == '__main__':
    a = Triangle(3, 4, 5)
    print(a.calculate_area())
    a.radius = - 1
