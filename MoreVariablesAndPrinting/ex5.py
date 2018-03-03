my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight, my_age + my_height + my_weight)

# Study drills
# 1. Change all the variables so there isn't the my_in front. Make sure you Change
# the name everywhere, not just where you used = to set them.

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)

# 2. Try more format characters. %r is a very useful one. It's like saying "print this no matter what."

first_name = 'Mya' # her first name
last_name = 'Henderson' # her last name
her_age = 38 # her age

print "%s, %s is a great R&B singer. She looks much younger than %d " % (first_name, last_name, her_age)

print "%r, %r is a great R&B singer. She looks much younger than %r " % (first_name, last_name, her_age)
# 3. Search online for all the Python format characters
# %i interger decimal
# %o unsigned octal
# %u unsigned decimal
# x unsigned hexidecimal lowercase
# X unsigned hexidecimal uppercase
# e floating point decimal
# E Floating point exponential format
# f Floating point decimal format
# F flating point decimal format
# c single character (accepts interger or single character string)

# 4. Try to write some variables that convert the inches and pounds to centimeters
# and kilos. Do not just type in the measurements

print "%s's is %d inches tall that makes him %d centimeters " % (name, height, height * 2.5)
print "%s's is %d pounds that makes him %d kilos!" % (name, weight, weight * 0.45359237)
