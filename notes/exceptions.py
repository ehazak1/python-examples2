class MyException:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return '%s%r' % (self.__class__.__name__, self.args)

class MyKeyError(MyException):
    pass

'''
BaseException:
|-    Exception
      |- ValueError  (too generic -- domain error -- unusable value)
      |- TypeError   (used everywhere when the type is wrong)
      |- LookupError
         |- KeyError    (used with sets and dicts)
         |- IndexError  (used with lists, tuples, and strings)
      |- NameError   (like a keyerror, but on a namespace dictionary)
|- SystemExit
|- KeyboardInterrupt

'''
