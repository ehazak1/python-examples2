''' Abstract Base Classes

Mixins:  provide reusable capability
         in the form a second story of the house
         on the plus side:
             - it provides easy code reuse
             - makes it really to build complex classes
         on the minus side:
             - they aren't self-documenting
             - they don't identify themselves as mixins
             - they don't describe their requirement

ABCS:   Mixins plus enforcement
        - Identify themselves as ABCs
        - They have a todo list:  C.__abstractmethods__
        - They verify the todos have gotten done
        - The self-document

'''

from abc import abstractmethod, ABCMeta

class Capper(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __len__(self):
        return 0

    @abstractmethod
    def __getitem__(self, index):
        raise IndexError

    def capitalize(self):
        return ''.join([c.upper() for c in self])


    def index(self, value):
        for i, v in enumerate(self):
            if v == value:
                return i
        raise ValueError(value)

class Uncapper:

    def uncapitalize(self):
        return ''.join([c.lower() for c in self])

#####################################################

from collections import Sequence

class DoubleSeq(Capper, Uncapper, Sequence):

    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return (len(self.seq) + 1) // 2

    def __getitem__(self, i):
        if i >= len(self):
            raise IndexError('Oops, I did it again')
        return self.seq[i * 2]


class TripleSeq(Capper, Sequence):

    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return (len(self.seq) + 2) // 3

    def __getitem__(self, i):
        if i >= len(self):
            raise IndexError('Oops, I did it again')
        return self.seq[i * 3]


if __name__ == '__main__':   

    d = DoubleSeq('Hettinger')
    print len(d)
    print d.capitalize()

    t = TripleSeq('Raymond')
    print len(t)
    print t.capitalize()





