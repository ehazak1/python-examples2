"Becoming a black belt with dictionaries."

# How to make a dictionary; exercise at least 5 ways to make a dict

d = {}

d = dict()

dict([('alpha', 1), ('beta', 2), ('gamma', 3)])

fruits = ["apple", 'banana', 'chocolate pudding plant', "durian"]
tastes = ['delicious', 'sweet', "awesome", "creamy"]
dict(zip(fruits, tastes))

dict(enumerate(fruits))

dict.fromkeys(fruits)


#################################################################
#
#  d[k]  --->  d.__getitem__(k)
#                  returns v if k is found
#                  or raises KeyError(k) if not found
#              but REALLY what happens is this
#                  if k is not found, it calls d.__missing__(k)
#                  |----->  __missing__(k) raises KeyError
#


class AngryDict(dict):
    def __missing__(self, key):
        print("I am so ANGRY!")
        print("%r is missing!" % key)
        raise KeyError(key)

############################

# How to count things in Python
class ZeroDict(dict):
    def __missing__(self, key):
        return 0

crayons = [ 'blue', 'red', 'red', 'green', 'red', 'blue', 'yellow', 'green', 'blue', 'red' ]

zd = ZeroDict()
for color in crayons:
    zd[color] += 1

############################

# How to group things in Python
class ListDict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]


names = "Davin Gabriel Kanai Mara Raymond Rachel Matthew Brandon Justin Taylor Kanye Kim Khloe Richard Gerald Jimmy Ronald George Bill George Barack Pedro Mark Matthew Tricia Luke John Ringo Paul Adele Tommy James Jim".split()



# Group by first letter of name
ld = ListDict()
for name in names:
    key = name[0]
    ld[key].append(name)

# Group by last letter of name
ld = ListDict()
for name in names:
    key = name[-1]
    ld[key].append(name)

# Group by length of name
ld = ListDict()
for name in names:
    key = len(name)
    ld[key].append(name)

# Group names by their number of vowels (a e i o u y)
ld = ListDict()
for name in names:
    key = sum(( name.count(vowel) for vowel in "aeiouy" ))
    ld[key].append(name)

############################

# Partial String Interpolation

madlib = 'The %(adjective)s brown fox %(verb)s over the lazy %(noun)s.'

class FormatDict(dict):
    def __missing__(self, key):
        return "%%(%s)s" % key
    

fd = FormatDict({ 'adjective': "shiny", 'verb': "grinds" })

template = madlib % fd

print template % { 'noun': 'rocksalt', 'adverb': 'disturbingly' }

############################

# How could you have created the __missing__ for yourself ?
# Overwrite the __getitem__ method as below, by creating a window for __missing__

class MissingDict(dict):

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        raise KeyError(key)

############################

# Show how to chain dictionaries together (data-inheritance)

class ChainDict(dict):

    def __init__(self, fallback, **kwargs):
        self.fallback = fallback

    def __missing__(self, key):
        return self.fallback[key]

window_defaults = dict(forground='black',
                        background='white',
                        border=2,
                        diagonal=700,
                        flashing=False)

info_defaults = ChainDict(window_defaults,
                          forground='cyan',
                          border=10)

error_defaults = ChainDict(info_defaults, 
                           flashing=True,
                           forground='red',
                           diagonal=200)
