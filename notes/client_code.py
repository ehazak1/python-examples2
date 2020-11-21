from __future__ import division
from class_demo import Circle
from random import seed, random

c = Circle(10)
print 'Demo of Circuitious', Circle.version
print 'A circle with a radius of', c.radius
print 'has an area of', c.area()
print

### Academic friends #####################################

print 'Proposal to study the average area of random circles'
print 'using Circuitous(tm)', Circle.version
print "Seeded using Jenny's number: "
seed(8675309)
n = 1000000
circles = [Circle(random()) for i in range(n)]
print 'Make', n, 'random circles'
areas = [c.area() for c in circles]
average = sum(areas) / n
print 'The average area is: %.6f' % average
print

### Rubber Sheet ##########################################

cuts = [0.1, 0.2, 0.7]
circles = [Circle(r) for r in cuts]
for c in circles:
    print 'A circle of radius', c.radius
    print 'has a perimeter of', c.perimeter()
    print 'and a cold area of', c.area()
    c.radius *= 1.1
    print 'and a warm area of', c.area()
    print

### National Tire Company ##################################

class Tire(Circle):
    'Odometer corrected circle'
    def perimeter(self):
        'Correct the circumference for the rubber on the tire'
        return Circle.perimeter(self) * 1.25
    __perimeter = perimeter

t = Tire(22)
print 'A tire of radius', t.radius
print 'has an inner area of', t.area()
print 'and a corrected perimeter of', t.perimeter()
print

### National Trucking Company ##############################

print 'A inclinometer reading of 5 degrees'
print 'is a %.2f%% grade' % Circle.angle_to_grade(5)
print

### National Graphics Company ##############################

c = Circle.from_bbd(30)
print 'A circle with a BBD of 30'
print 'has a radius of', c.radius
print
