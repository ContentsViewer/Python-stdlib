import math


class Vector2:

    def __init__(self, x=0, y=0):
        self.values = [x, y]

    @property
    def x(self):
        return self.values[0]

    @x.setter
    def x(self, value):
        self.values[0] = value

    @property
    def y(self):
        return self.values[1]

    @y.setter
    def y(self, value):
        self.values[1] = value

    @property
    def magnitude(self):
        return math.sqrt(self.sqr_magnitude)

    @property
    def sqr_magnitude(self):
        return self.values[0]**2 + self.values[1]**2

    @staticmethod
    def zero():
        return Vector2(0, 0)

    @staticmethod
    def one():
        return Vector2(1, 1)

    def __add__(self, other):
        return self.__class__(self.values[0] + other.values[0], self.values[1] + other.values[1])

    def __sub__(self, other):
        return self.__class__(self.values[0] - other.values[0], self.values[1] - other.values[1])

    def __mul__(self, other):
        return self.__class__(self.values[0] * other, self.values[1] * other)

    def __truediv__(self, other):
        return self.__class__(self.values[0] / other, self.values[1] / other)

    def __neg__(self):
        return self.__class__(-self.values[0], -self.values[1])

    def __iadd__(self, other):
        self.values[0] += other.values[0]
        self.values[1] += other.values[1]
        return self

    def __imul__(self, other):
        self.values[0] *= other
        self.values[1] *= other
        return self

    def __isub__(self, other):
        self.values[0] -= other.values[0]
        self.values[1] -= other.values[1]
        return self

    def __itruediv__(self, other):
        self.values[0] /= other
        self.values[1] /= other
        return self

    def __str__(self):
        return '(%f, %f)' % (self.values[0], self.values[1])

    def __repr__(self):
        return '(%f, %f)' % (self.values[0], self.values[1])
