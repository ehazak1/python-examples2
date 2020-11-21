''' Circuitous(tm) -- An advanced circle analytic company using SDN'''

from math import pi, radians, tan, sqrt       # Factored-out constants, code reuse, and variable precision
from collections import namedtuple

Version = namedtuple('Version', ['major', 'minor'])     # Self-documenting tuple

class Circle(object):     # New-style classes
    'An Advanced Circle Analytic Toolkit'  

    __slots__ = ['diameter']               # implement the flyweight design pattern by suppressing the instance dictionary

    version = Version(0, 8)                # class variable -- data shared by all instances

    def __init__(self, radius):
        self.radius = radius               # instance variable -- data unique to each instance
    
    def area(self):             # Regular method has "self" as an argument
        'Perform quadrature of planar shape of uniform revolution'
        p = self.__perimeter()  # class local reference using name mangling
        r = p / 2.0 / pi
        return pi * r ** 2.0

    def perimeter(self):
        'Compute the closed line integeral for the locus of points equidistant from a given point'
        return 2.0 * pi * self.radius

    __perimeter = perimeter     # class local copy for internal references

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.radius)

    @staticmethod               # Reprograms the dot to not put in self
    def angle_to_grade(angle):  # To allow a function to be put in a class
        'Convert an angle in degrees to a percent grade'
        return tan(radians(angle)) * 100.0

    @classmethod                 # Reprograms the dot to put in the class
    def from_bbd(cls, bbd):      # To create alternative constructors
        'Alternate constructor using a bounding box diagonal'
        r = bbd / 2 / sqrt(2)
        return cls(r)

    @property            # property() magicly changes attribute access into method access
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    



    
    


