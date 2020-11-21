''' Becoming a black belt with dictionaries '''

from pprint import pprint

# How to make a dictionary #########################

d = {}                             # dictionary literal
d = dict()                         # dict contructor


# Five ways to prepopulate a dictionary #############

d = {                              # dictionary literal
     'raymond': 'red',
     'rachel': 'blue',
     'matthew': 'yellow',
}

d = dict(raymond='red', rachel='blue', matthew='yellow')

lot = [('raymond', 'red'), ('rachel', 'blue')]
d = dict(lot)

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow'.split()
d = dict(zip(names, colors))

d = dict.fromkeys(names, 0)

# How to override the just the behavior for missing keys ###

# d[k]  --> d.__getitem__(k)
#             return v if k is found
#             if not found, it calls d.__missing__(k)
#                 |--> __missing__(k) raises KeyError

class AngryDict(dict):
    def __missing__(self, key):
        print 'I am so mad!'
        print '%r is missing!' % key
        raise KeyError(key)

class ZeroDict(dict):
    def __missing__(self, key):
        return 0

colors = 'red green red blue red green'.split()

d = ZeroDict()
for color in colors:
    d[color] += 1

# How to group data in python ##########################
# mapping   group_key to a list of things in the group

class ListDict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]

names = 'davin raymond rachel matthew randal darron mary ' \
        'susan billy sherry beatrice bill marty betty sheldon'.split()

# Group these names by their first letter
d = ListDict()
for name in names:
    key = name[0]
    d[key].append(name)
    
pprint(d); print '-' * 20 + '\n' * 2

# Group these names by their last letter
d = ListDict()
for name in names:
    key = name[-1]
    d[key].append(name)
    
pprint(d); print '-' * 20 + '\n' * 2

# Group these names by the length of their name
d = ListDict()
for name in names:
    key = len(name)
    d[key].append(name)
    
pprint(d); print '-' * 20 + '\n' * 2

# Group these names by the number of vowels in the name
#    a e i o u y
d = ListDict()
for name in names:
    key = sum(name.count(v) for v in 'aeiouy')
    d[key].append(name)
    
pprint(d); print '-' * 20 + '\n' * 2

##################################################
# Show how to do partial substitution in templates

class FormatDict(dict):
    def __missing__(self, key):
        return '%%(%s)s' % key

d = FormatDict(old=10)
s = 'The answer is %(new)s today but was %(old)s yesterday' % d
print s
print s % dict(new=20)

##################################################
# Show how to chain dictionaries together

class ChainDict(dict):
    def __init__(self, fallback, **kwds):
        self.fallback = fallback
        self.update(kwds)
    def __missing__(self, key):
        return self.fallback[key]

window_defaults = dict(foreground='cyan',
                       background='white',
                       border=2,
                       width=200)

text_window = ChainDict(window_defaults,
                        foreground='blue',
                        border=4)

warning_window = ChainDict(window_defaults,
                        background = 'red',
                        border = 10,
                        width = 100)

    
pprint(d); print '-' * 20 + '\n' * 2

#####################################################
# How you could have created the __missing__ yourself


class MissingDict(dict):
    '''What if you had an old version of Python
       without __missing__?

       Answer:  Build any behavior you want
       and inherit from it

    '''
    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)
    def __missing__(self, key):
        raise KeyError(key)

    
class ZeroDict(MissingDict):
    def __missing__(self, key):
        return 0

d = ZeroDict()
print d['roger']
