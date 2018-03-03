# Put the formated string inside the varible x
x = "There are %d types of people." % 10

# Put the string "binary" inside a varible named binary
binary = "binary"
# Put the string "don't" inside the variable do_not
do_not = "don't"

# Assigned formated string two arguments and put inside of the varible y
# 1 string is put in a string
y = "Those who know %s and those who %s." % (binary, do_not)

# print the results of x
print x
# print the results of y
print y
# print the assigned formated string with the results of x
# 2 string is put inside a string
print "I said: %r." % x
# print the assigned formated string with the results of y
# 3 string is put inside a string
print "I also said: '%s'." % y

# assigned false to the variable hilarious and assigneed the formated string
hilarious = False
#4 string is put inside a string
joke_evaluation = "Isn't that joke so funny?! %r"

# printed the formated string in the variable joke and got the assigned boolean
# from hilarious
print joke_evaluation % hilarious

# assigned a string to the variable w
w = "This is the left side of..."
# assigned a string to the variable e
e = "a string with a right side."

# concatenated and printed content the variable w and e
print w + e

#Study Drill

# 1. Go through this program and write a comment above each line explaining it.

# 2. Find all the places where a string is put inside a string. There are four places.

# 3. Are you sure there are only four places? How do you know? Maybe I like lying.

# 4. Explain why adding the two strings w and e with + makes a longer string.
# because your concatenating it. 
