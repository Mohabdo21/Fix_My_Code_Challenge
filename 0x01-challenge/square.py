#!/usr/bin/python3
"""
This module defines a Square class and calculates the area and perimeter.
"""


class Square:
    """
    A class to represent a square.

    ...

    Attributes
    ----------
    side : int
        side length of the square

    Methods
    -------
    area():
        Returns the area of the square.
    perimeter():
        Returns the perimeter of the square.
    """

    def __init__(self, side=0):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
            side : int
                side length of the square (default 0)
        """
        self.side = side

    def area(self):
        """Returns the area of the square."""
        return self.side ** 2

    def perimeter(self):
        """Returns the perimeter of the square."""
        return self.side * 4

    def __str__(self):
        return "Square with side length: {}".format(self.side)


if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
