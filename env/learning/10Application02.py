import numbers
import collections
from collections import abc

# Polygon - Vertices - 2D.
class Int:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner_class, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.name} must be an int')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be at least {self.max_value}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, None)


class Point2D:
    x = Int(min_value=0, max_value=800)
    y = Int(min_value=0, max_value=600)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'

    def __str__(self):
        return f"{self.x}, {self.y}"


point_2_d = Point2D(0, 10)

print(f"Testing STRING_TYPE: {str(point_2_d)}")

print(f" Testing REPRESENTATION: {repr(point_2_d)}")

try:
    point_2_d = Point2D(0, 800)
except ValueError as ex:
    print(ex)

# using collection.abc.sequence
print(f"is '1,2,3' a sequence = {isinstance((1,2,3), abc.Sequence)}")
print(f"is '1,2,3' a sequence = {isinstance((1,2,3), abc.MutableSequence)}")

class Point2DSequence:
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, abc.Sequence):
            raise ValueError(f"{self.name} must be a sequence type")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"{self.name} must contain at least {self.min_length} elements")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f"{self.name} must contain at least {self.max_length} elements")

        for index, item in enumerate(value):
            if not isinstance(item, Point2D):
                raise ValueError(f"Item at index {index} is not a Point2D instance ")

        instance.__dict__[self.name] = list(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            if self.name not in instance.__dict__:
                instance.__dict__[self.name] = []
            return instance.__dict__.get(self.name)


class Polygon:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices


try:
    polygon = Polygon()
except ValueError as ex:
    print(ex)

try:
    polygon = Polygon(Point2D(-100, 0), Point2D(0, 1), Point2D(1, 0))
except ValueError as ex:
    print(ex)

poly = Polygon(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))
print(f" Vertices of Poly = {poly.vertices}")


class PolygonAppend:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            raise ValueError(f"Vertices length is at max ({max_length})")
        self.vertices.append(pt)


polyTwo = PolygonAppend(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))

print(polyTwo.vertices)
polyTwo.append(Point2D(10, 10))
print(polyTwo.vertices)


# inherit Polygon Method
class Triangle(PolygonAppend):
    # vertices with min and max lengths
    vertices = Point2DSequence(min_length=3, max_length=3)

class Rectangle(PolygonAppend):
    # vertices with min and max lengths
    vertices = Point2DSequence(min_length=4, max_length=4)

# checking error if any other vertices is added to the polygon
# t = Triangle(Point2D(0, 0), Point2D(1, 1), Point2D(3, 3), Point2D(10, 10))


class PolygonFinal:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            raise ValueError(f"Vertices length is at max ({max_length})")
        self.vertices.append(pt)

    # For finding how many vertices are there
    def __len__(self):
        return len(self.vertices)

    # for slicing vertices
    def __getitem__(self, idx):
        return self.vertices[idx]

polyThree = PolygonFinal(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))

print(f"Length of Polygon={len(polyThree)}")
print(polyThree.vertices)
print(f"Which is 2nd Vertice={polyThree[1]}")
print(f"slicing {polyThree[1:3]}")


class PolygonFinalVersion:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            raise ValueError(f"Vertices length is at max ({max_length})")
        self.vertices.append(pt)

    # For finding how many vertices are there
    def __len__(self):
        return len(self.vertices)

    # for slicing vertices
    def __getitem__(self, idx):
        return self.vertices[idx]

    # inplace addition
    def __iadd__(self, pt):
        self.append(pt)
        return self

    def __contains__(self, pt):
        return pt in self.vertices


polyFour = PolygonFinalVersion(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))

print(list(polyFour))

polyFour += Point2D(10, 11)

print(polyFour.vertices)
print(Point2D(0, 0) in polyFour.vertices, end='\n\n')


class Point2D:
    x = Int(min_value=0, max_value=800)
    y = Int(min_value=0, max_value=600)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __eq__(self, other):
        return isinstance(other, Point2D) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x, self.y)


class Polygon:
    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D instances')
        max_length = type(self).vertices.max_length
        if max_length is not None and len(self.vertices) >= max_length:
            raise ValueError(f"Vertices length is at max ({max_length})")
        self.vertices.append(pt)

    # For finding how many vertices are there
    def __len__(self):
        return len(self.vertices)

    # for slicing vertices
    def __getitem__(self, idx):
        return self.vertices[idx]

    # inplace addition
    def __iadd__(self, pt):
        self.append(pt)
        return self

    def __contains__(self, pt):
        return pt in self.vertices


polyFive = Polygon(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))
print(Point2D(0, 0) in polyFive.vertices)