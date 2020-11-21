"""Learn more about how-to with property.

It supportes computed fields:
    * data consistency (one field is computed from others)
    * space efficiency (no need to store teh computed field)
    * API consistency (everything looks like an attribute)
    * possible side-benefit: create a read-only attribute

It supports assignments checks:
    * validate data beore it gets stored
    * simplify debugging because the error is noticed at the momemnt the data
      is entered and not down the line

It's commong to create a module full of validatores:
    * validate_positive
    * validate_percentage
    * validate_string(size)
    * validate_among('win', 'lose', 'draw')
    * validate_foreign_key(mapping)

"""

def validate_positive(value):
    if value < 0.0:
            raise ValueError("Did not expect a negative value!")


class PriceRange(object):

    def __init__(self, low, high):
        self.low = low
        self.high = high

    # a property definition for the midpoint value, it is compupted on
    # the fly (dynamically), and is read-only, and is called as PriceRange.midpoint
    # as an attribute, and not as a function
    @property
    def midpoint(self):
        return (self.low + self.high) / 2.0

    #### definition of property (getter & setter) using the property func ####
    def get_low(self):
        validate_positive(value)
        return self._low

    def set_low(self, value):
               self._low = value

    low = property(get_low, set_low)
    
    #### definition of property (getter & setter) usind decorators ####
    @property
    def high(self):
        return self._high
    
    @high.setter
    def high(self, value):
        validate_positive(value)
        self._high = value
