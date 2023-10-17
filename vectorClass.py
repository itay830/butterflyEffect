import pygame

from math import sqrt, pow
from typing import Union
from abc import ABC



class Vector(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector2(Vector):
    def __init__(self, x=0, y=0):
        if isinstance(x, tuple):
            super().__init__(x[0], x[1])
        else:
            super().__init__(x, y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __add__(self, other: Union[Vector, float]):
        if isinstance(other, self.__class__):
            return Vector2(self.x + other.x, self.y + other.y)
        return Vector2(self.x + other, self.y + other)

    def __sub__(self, other: Union[Vector, float]):
        if isinstance(other, self.__class__):
            return Vector2(self.x - other.x, self.y - other.y)
        return Vector2(self.x - other, self.y - other)

    def __mul__(self, other: Union[Vector, float]):
        if isinstance(other, self.__class__):
            return Vector2(self.x * other.x, self.y * other.y)
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other: Union[Vector, float]):
        if isinstance(other, self.__class__):
            return Vector2(self.x / other.x, self.y / other.y)
        return Vector2(self.x / other, self.y / other)

    def get_length(self):
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self):
        length = self.get_length()
        if length < 0.0001:
            return Vector2(0, 1)
        return self / length

    def return_tuple(self):
        return self.x, self.y

    def draw(self, display: pygame.Surface, origin: Union[Vector, tuple], color=(0, 0, 125), scale: int = 10):

        if isinstance(origin, self.__class__):
            origin = (origin.x, origin.y)
        pygame.draw.line(display, color, origin, (origin[0] + self.x*scale, origin[1] + self.y*scale), 5)


def rounding(vector: Vector2) -> Vector2:
    return Vector2(round(vector.x), round(vector.y))


def dot_product(v1: Vector2, v2: Vector2) -> Union[float, int]:
    return v1.x * v2.x + v1.y * v2.y


def dist(v1: Vector2, v2: Union[Vector2, tuple]) -> Union[float, int]:
    if isinstance(v2, tuple):
        v2 = Vector2(v2[0], v2[1])

    return (v1 - v2).get_length()


def reflection(v1: Vector2, normal: Vector2) -> Vector2:
    return v1 - normal * dot_product(v1, normal) * 2
