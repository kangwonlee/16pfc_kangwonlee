my_name = 'Kangwon Lee'
my_age = 46  # It's a lie
my_height_cm = 180.5
my_weight_kg = 80
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'
# place holder
print "Let's talk about %s." % my_name
print "He's %g centimeters tall." % my_height_cm
print "He's %d centimeters tall." % my_height_cm
print "He's %d kilograms heavy." % my_weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height_cm, my_weight_kg, my_age + my_height_cm + my_weight_kg
)
