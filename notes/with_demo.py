import threading

# The RightWay(tm) to open and close files.

f = open('notes/hamlet.txt')
try:
    play = f.read()
    print len(play)
finally:
    f.close()

# The NewWay(tm) to open and close files.

with open('notes/hamlet.txt') as f:
    play = f.read()
    print len(play)

# Threading tends to create race conditions
# which are managed using mutexes (mutual exclusion)

print_lock = threading.Lock()

# How to use a lock TheOldWay(tm) ##################

print_lock.acquire()
try:
    print 'Hello'
    print 'I love you'
    print "Won't you tell me your name"
finally:
    print_lock.release()

# How to use a lock TheNewWay(tm) ##################

with print_lock:
    print 'Hello'
    print 'I love you'
    print "Won't you tell me your name"

####################################################

''' Notes:

        The "as f" stores whatever __enter__ returns
        If __exit__ returns True, exceptions are handled
            which means control flow continues downward
        If __exit__ returns False, exceptions are not handled
            which mean control flow goes up to high level handlers
            including the default handler which stops the program
            and prints a traceback
        
'''
    

class CM:

    def __init__(self, x):
        print 'Initializing'
        self.x = x

    def __enter__(self):
        print 'Entering'
        return 42

    def __exit__(self, exc_type, exc_inst, exc_tb):
        # The bool of the return value
        # determines whether the exception is handled
        print 'Exiting'
        print 'The exctype is:', exc_type
        if isinstance(exc_inst, KeyError):
            print 'Caught a KeyError'
            print 'The arguments are', exc_inst.args
            print 'Marking as handled'
            return True
        print 'Not handling exceptions'


# The normal path through a context manager

print 'Starting up the example'
with CM(10) as y:
    print 'In the body with', y
    print 'In the middle'
    print 'At the end'
print 'Wrapping-up the example'
        
# The handled exception path through a context manager

print '-----------------------'
print 'Starting up the example'
with CM(10) as y:
    print 'In the body with', y
    print 'In the middle'
    raise KeyError('raymond')
    print 'Never get here'
print 'Wrapping-up the example'

# The unhandled exception path through a context manager
##
##print '-----------------------'
##print 'Starting up the example'
##with CM(10) as y:
##    print 'In the body with', y
##    print 'In the middle'
##    raise IndexError(5)
##    print 'Never get here'
##print 'Never get here either'

# How files are implemented

class File:

    def __init__(self, filename, mode='r', flags=0466):
        self.fd = os.makefile(filename, mode, flags)

    def read(self, n=None):
        if n is None:
            return os.read_the_whole_file()
        else:
            return os.read_fixed_number_of_bytes(n)

    def write(self, s):
        pass

    def close(self):
        return os.free_fd(self.fd)

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        self.close()

class Lock:
    def __init__(self):
        self.lock = os.getlock()

    def acquire(self):
        os.acquire_lock(self.lock)

    def release(self):
        os.release_lock(self.lock)

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exctype, excinst, exctb):
        self.release()

###############################################################
# How to add a context manager to existing classes
# by wrapping them

class Closing:
    'Context manager for autoclosing a file-like object'

    def __init__(self, filelikeobj):
        self.fileobj = filelikeobj

    def __enter__(self):
        return self.fileobj

    def __exit__(self, exctype, excinst, exctb):
        self.fileobj.close()

from StringIO import StringIO
from contextlib import closing

with closing(StringIO()) as f:
    print >> f, 'Tear down the wall'
    print >> f, 'Mother, do you think they will drop the bomb'
    s = f.getvalue()

print repr(s)
        




