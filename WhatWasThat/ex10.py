# put to use thai characters!!!
# -- coding: utf-8 --

#escape double - quotes and single quotes so Python knows what to include in the sting

# print "I am 5'8\" tall."
# print 'I am 5\'8" tall.'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

chicken = "ก"
print chicken

delicious = "duck"
nasty = 'goat'

print " I eat %r and %r " % (delicious, nasty)
print ' I eat %s and %r ' % (delicious, nasty)

# 1. Memorize all the escape sequences by putting them on flash cards.
# 2. Use ''' (triple-single-quote) instead. Can you see why you might
# use that instead of """?
# ''' are treated as regular strings that can span multiple lines.
# Combine escape sequences and format strings to create a more complex format.
# Remember the %r format? Combine %r with double-quote and single-quotes# escapes
# and prints them out. Compare %r with %s. Notice how %r prints it in the
# way you'd write it in your file, but %s prints it the way you'd like to
# see it?
