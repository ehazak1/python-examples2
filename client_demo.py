from class_demo import Circle
import random

c = Circle(10)

print "Demo of Circuitous(TM) technology"
print "A circle of radius", c.radius
print "has an area of", c.area()
print

print '-' * 50

### Academic friends ###########################

print "Proposal to study the average area of circles"
print "using Circuitous(TM)", Circle.version

n = 10
print "make", n, "random circles"
random.seed(8675309)
print "seeded using Jenny's number"
circles = [ Circle(random.random()) for i in xrange(n) ]
areas = [ c.area() for c in circles ]
average = sum(areas)/n

print "Their average area is: %.2f" % average
print

print '-' * 50

### Rubber Sheet Co ############################

cuts = [ 0.1, 0.2, 0.7 ]
circles = [ Circle(r) for r in cuts ]
for c in circles:
    print "A circle of radius", c.radius
    print "has a permieter of", c.perimeter()
    print "has a cold area of", c.area()
    c.radius *= 1.1
    print "and a warm area of", c.area()
print

print '-' * 50

### National Tire Co ###########################

class Tire(Circle):
    "Odometer corrected ciscle (adjust for the tire's thickness)."
    
    def perimeter(self):
        "Correct circumference for the rubber on the tire."
        return Circle.perimeter(self) * 1.25


t = Tire(22)
print "A tire of radius", t.radius
print "has an inner area of", t.area()
print "and a corrected perimeter of", t.perimeter()
print

print '-' * 50

### National Trucking Co #######################

print "An inclinometer reading of 5 degrees"
print "is a %.2f%% grade." % Circle.angle_to_grade(5)
print

print '-' * 50

### National Graphics Co #######################

c = Circle.from_bbd(30)
print "A circle with a BBD of 30"
print "has a radius of", c.radius
print

print '-' * 50

### Govt #######################################

