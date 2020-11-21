"""
Circuitous(TM) -- An advanced circle analytics company, leveraging cloud technologies to maximize time-to-maket delivery in the IoT space using SDNs, NFV and big data synergies.
"""

from math import pi, tan, radians, sqrt
from collections import namedtuple

Version = namedtuple("Version", ["major", "minor"])

class Circle(object):   # New-style class
    "An Advance Circle Analytics Toolkit"

    __slots__ = ['diameter'] # add only as final polish to reduce memory use

    version = Version(1, 1)

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        "Performs quadrature of a planer shape of uniform revolution."
        #return pi * self.radius ** 2.0
        p = self.__perimeter()
        return p * p / (4.0 * pi)

    def perimeter(self):
        """Compute the closed line integral of the locus of points equidistant
        from the center."""
        return 2.0 * pi * self.radius

    # stash a copy of perimeter to prevent breaking if someone changes our
    # class in a subclass
    # __WHATEVER expands to _[class_name]__perimeter
    __perimeter = perimeter
        
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.radius)

    @staticmethod               # Reprograms the dot to not put in self
    def angle_to_grade(angle):  # allows a regular func to be inside a class
        "Convers an angle in degrees into percent grade."
        return 100.0 * tan(radians(angle))

    @classmethod        # Reprograms the dot to put in a reference to the class
    def from_bbd(cls, bbd):  # purpose is to create alt constructors
        "Alternative means of creating object from it's bounding box diagonal"
        r = bbd/(2 * sqrt(2))
        return cls(r)
    
    ###############################################
    #
    # Fairy Godmother Wish
    #
    # c.radius --> c.get_radius()
    #
    # c.radius = 20 --> c.set_radius(20)


    def get_radius(self):
        return self.diameter / 2.0

    def set_radius(self, r):
        self.diameter = r * 2

    radius = property(get_radius, set_radius)
