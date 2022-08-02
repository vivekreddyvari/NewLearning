import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        # super().__init__(x=0.0, y=0.0)
        self.vertice1 = Point()
        self.vertice2 = Point()
        self.vertice3 = Point()

    def perimeter(self):
        pass


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())