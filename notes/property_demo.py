''' Learn all about how to properties

It supports computed fields:
* data consistency (one field computed from others)
* space efficiency (no need to store the computed field)
* API consistency (everything looks like an attribute lookup)
* possible side-benefit:  create a read-only attribute

Is supports assignment checks:
* Validate data before it gets stored
* Simplfies debugging because the error happens
  at the moment the data is corrupted and not downstream

It is common to create a module full of validators:
* validate_string(size)
* validate_percentage
* validate_positive
* validate_among('win', 'lose', 'draw')
* validate_foreign_key(mapping)

'''

def validate_percentage(value):
    if not isinstance(value, (int, float)):
        raise TypeError('Expected an int or float')
    if value < 0.0 or value > 100.0:
        raise ValueError('Expected a value between 0 and 100')


##############################################################

class PriceRange(object):

    def __init__(self, low, high):
        self.low = low
        self.high = high

    @property                       # midpoint = property(midpoint)
    def midpoint(self):
        'Computed field half-way between low and high'
        return (self.low + self.high) / 2.0

    @property
    def low(self):
        'The small end of the price range'
        return self._low

    @low.setter
    def low(self, low):
        validate_percentage(low)
        self._low = low

    @property
    def high(self):
        'The high end of the price range'
        return self._high

    @high.setter
    def high(self, high):
        validate_percentage(high)
        self._high = high


p = PriceRange(10.0, 18.0)
