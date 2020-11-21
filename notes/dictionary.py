''' Goal:  Make a dictionary-like object
           that is shareable between programs
           in a simple text format
           and persistent.
'''

import collections
import os

class PersistentDict(collections.MutableMapping):

    def __init__(self, dirname, items=[], **kwds):
        self.dirname = dirname
        try:
            os.mkdir(dirname)
        except OSError:
            pass
        self.update(items, **kwds)

    def __setitem__(self, key, value):
        fullname = os.path.join(self.dirname, key)
        with open(fullname, 'w') as f:
            f.write(value)
            
    def __getitem__(self, key):
        fullname = os.path.join(self.dirname, key)
        try:
            with open(fullname) as f:
                return f.read()
        except IOError:
            raise KeyError(key)
    
    def __delitem__(self, key):
        fullname = os.path.join(self.dirname, key)
        try:
            os.remove(fullname)
        except OSError as e:
            if e[0] == 2:
                raise KeyError(key)
            raise

    def __len__(self):
        return len(os.listdir(self.dirname))

    def __iter__(self):
        return iter(os.listdir(self.dirname))

    def __repr__(self):
        return '%s(%r, %r)' % \
            (self.__class__.__name__,
             self.dirname,
             self.items())

if __name__ == '__main__':
    d = PersistentDict('hettingers')
    d['raymond'] = 'red'
    d['rachel'] = 'blue'
    d['matthew'] = 'yellow'
    print d['raymond']
    print d['rachel']
    print d['matthew']
    print len(d)
    del d['matthew']
    print len(d)
    for k in d:
        print k
