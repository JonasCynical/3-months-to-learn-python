name = 'Jonas'
age = 21 # that's true
height_inches = 70 # inches
weight_lbs = 145 # lbs
eyes = 'Black'
teeth = 'Yellow'
hair = 'Black'
k1 = 2.54
k2 = 0.4536
height_centimeters = height_inches * k1
weight_kilograms = weight_lbs * k2

print "Let's talk about %s." % name
print "He is %r inches tall.Which means %d centimeters." % (height_inches, height_centimeters)
print "He is %r pounds heavy.Which means %d kilograms." % (weight_lbs, weight_kilograms)

print "That's a perfect figure."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teech are usually %s depending on the coffee." % teeth

print "If i get %r, %r, and %r i get %r." % (age, height_inches, weight_lbs, age + height_inches + weight_lbs)
