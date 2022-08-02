import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        square_root_xy = math.sqrt(x - y)
        return square_root_xy

    def distance_from_point(self, point):
        x_cor = (point.getx() - self.__x) ** 2
        y_cor = (point.gety() - self.__y) ** 2
        return math.sqrt(x_cor + y_cor)


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
