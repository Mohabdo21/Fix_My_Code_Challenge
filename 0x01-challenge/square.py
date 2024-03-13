#!/usr/bin/python3
"""
This module defines a Square class and calculates the area and perimeter.
"""


class Square():
    """
    A class to represent a square.

    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """init method for the class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Calculating PermiterOfMySquare"""
        return (self.width + self.height) * 2

    def __str__(self):
        """Repr the class"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Create a square"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
