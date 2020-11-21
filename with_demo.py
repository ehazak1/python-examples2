# The OldRightWay(TM) to open and close files
    
fh = open("notes/hamlet.txt")
try:
    data = fh.read()
    print len(data)
finally:
    fh.close()

# The NewRightWay(TM) to open and close files

with open("notes/hamlet.txt") as fh:
    data = fh.read()
    print len(data)

##################################

import threading

print_lock = threading.Lock()

# How to use a Lock the OldWay(TM)
print_lock.acquire()
#[Out]# True
try:
    print "Hello"
    print "I love you"
    print "Won't you tell me your name"
finally:
    print_lock.release()
    
# How to use a Lock the NewRightWay(TM)
with print_lock:
    print "Hello"
    print "Can you hear me?"

##################################


class CM:
     def __enter__(self):
         print "Inside __enter__"
         return 42

     def __exit__(self, exc_type, exc_inst, exc_tb):
         print "Inside __exit__"
         print "exc_type:", exc_type
         print "exc_inst:", exc_inst
         print "exc_tb:", exc_tb
         if isinstance(exc_inst, ValueError):
             print "Caught a value error"
             print "It's arguments are:", exc_inst.args
             print "Marking as handled"
             return True
         if exc_type is None:
             "No exception was encountered"
         else:
             print "Marking as UN-handled"
         return False


print '-' * 50
print "Normal path through a context manager"
with CM() as z:
    print "Inside the body, z=", z
    print "Done with the body"

print '-' * 50
print "Handled exception path through a context manager"
with CM() as z:
    print "Inside the body, z=", z
    raise ValueError("Oops, I did it again!")
    print "Done with the body"

print '-' * 50
print "Un-handled exception path through a context manager"
#with CM() as z:
#    print "Inside the body, z=", z
#    raise KeyError("Another one bites the dust")
#    print "Done with the body"

##################################

class Closing:
    "Context manager for auto-closing of file like object."

    def __init__(self, file_like_obj):
        self.fileobj = file_like_obj

    def __enter__(self):
        return self.fileobj

    def __exit__(self, exc_type, exc_inst, exc_tb):
        self.fileobj.close()
