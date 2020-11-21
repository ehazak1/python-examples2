#######################################################################
# Basic list operations

s = [10, 20, 30]                # Construct a list from square brackets

s.append(40)                    # Add a single element
print s

s.extend([50, 60, 70])          # Add multiple elements from an iterable
print s

print s.pop()                   # Remove the last element
print s

print s[0]                      # First element
print s[-1]                     # Last element
print s[:2]                     # First two elements
print s[-2:]                    # Last two elements

print '-' * 20

#######################################################################
# Circular list

s = [10, 20, 30]
s.append(s)
print s
print s[-1][-1][-1][0]

print '-' * 20

#######################################################################
# Singly Linked list stored as pairs in the form: [value, link]

VALUE = 0
LINK = 1

s = [10, None]
t = [20, s]
u = [30, t]

def head(p):
    return p[VALUE]

def tail(p):
    return p[LINK]

print 'Chain of pairs:', u
print head(u)
print head(tail(u))
print head(tail(tail((u))))

def show_linked_list(p):
    while p is not None:
        print p[VALUE]
        p = p[LINK]

show_linked_list(u)

print '-' * 20

#######################################################################
# Doubly Linked List stored as triplets in the form: [value, prev, next]

VALUE = 0
PREV = 1
NEXT = 1

b = ['Brian', None, None]

s = ['Sam', None, None]
b[NEXT] = s
s[PREV] = b

c = ['Charlie', None, None]
s[NEXT] = c
c[PREV] = s

print b[VALUE]
print b[NEXT][VALUE]
print b[NEXT][NEXT][VALUE]

print s[VALUE]
print s[PREV][VALUE]
print s[PREV][PREV][VALUE]

print '-' * 20

##########################################
# Tree:  [value, mlink, plink]

dennis = ['Dennis', None, None]
sharon = ['Sharon', None, None]
rachel = ['Rachel', sharon, dennis]
ramon = ['Ramon', None, None]
gayle = ['Gayle', None, None]
raymond = ['Raymond', gayle, ramon]
matthew = ['Matthew', rachel, raymond]


NAME = 0
MOM = 1
POP = 2

def father(p):
    return p[POP][NAME]

def grandfathers(p):
    return p[POP][POP][NAME], p[MOM][POP][NAME]


print father(raymond)
print father(rachel)
print father(matthew)
print grandfathers(matthew)

# Three ways to flatten a tree: Preorder, Inorder, Postorder

def preorder(p):
	if p is None:
		return []
	return [p[NAME]] + preorder(p[MOM]) + preorder(p[POP])

def inorder(p):
	if p is None:
		return []
	return inorder(p[MOM]) + [p[NAME]] + inorder(p[POP])

def postorder(p):
	if p is None:
		return []
	return postorder(p[MOM]) + postorder(p[POP]) + [p[NAME]]

print preorder(matthew)
print inorder(matthew)
print postorder(matthew)

print '-' * 20

##########################################
# List Iteration

s = [10, 20, 30]
for x in s:
    print x

s = [10, 20, 30]
it = iter(s)
print next(it)
print next(it)
print next(it)

# list iterators remember position
# stops with the position is too far
# once stopped, it stays stopped

# It is possible to mutate a list while looping over it.
s = [50, 25, 80, 90, 30, 15, 100]
for x in s:
    print x
    if x > 20:
        s.append(x // 2)

# It behaves differently if you loop over a copy
s = [50, 25, 80, 90, 30, 15, 100]
for x in s[:]:
    print x
    if x > 20:
        s.append(x // 2)

##########################################
# 2-D Arrays are implemented as a list of lists
# or as a list of tuples

m = [[10, 20, 30],
     [40, 50, 60]]

# Extract rows with single lookups
print 'Row 0:', m[0]
print 'Row 1:', m[1]

# Extract values with separate row and column references
print m[0][0]
print m[1][2]

# Extract columns with list comprehensions
print 'Col 0:', [m[i][0] for i in range(2)]
print 'Col 1:', [m[i][1] for i in range(2)]
print 'Col 2:', [m[i][2] for i in range(2)]

# Transpose the rows with zip()
print zip([10, 20, 30], [40, 50, 60])
print zip(m[0], m[1])
print zip(*m)

###########################################
## LIFO Stacks are easy

s = []
s.append(10)
s.append(20)
s.append(30)

print 'Pop most recently added:', s.pop()
print 'Pop next most recently added:', s.pop()
print 'Pop oldest:', s.pop()

###########################################
## FIFO Queues are easy too

s = []
s.append('First')
s.append('Second')
s.append('Third')

print 'Oldest task:', s.pop(0)
s.append('Fourth')
print 'Next oldest task:', s.pop(0)
print 'Pending tasks:', s

