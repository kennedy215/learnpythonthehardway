from sys import argv

# Original Script

# script, first, second, third = argv

# script, first, second, third = argv
#
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third
#


# Script with 2 arguments

# lessscript, one, two = argv
#
# print "Script:", lessscript
# print "One:", one
# print "Two:", two

# Script with 4 arguments
#
# morescript, jam, love, heart, strings = argv
#
# print "Script is called:", jam
# print "I:", love
# print "Heart:", heart
# print "?", strings





# make sure to run the script like this
# python ex13.py first 2nd 3rd

# Study Drills
# Try giving fewer than three arguments to your script. See that error you get?
# See if you can explain it.

# Traceback (most recent call last):
#   File "ex13.py", line 5, in <module>
#     script, first, second = argv
# ValueError: too many values to unpack

# We're not giving it enough values to unpack.


# Write a script that has fewer argments and one that has more. Make sure you
# give the unpacked variables good names.
# Won't work if you have too many arguments it's too much

# Combine raw_input with argv to make a script that gets more input from a user.
# Remember that modules give you features. Modules. Modules.

# Combine argV with raw_input

argrawscript, name = argv
prompt = '> '

print "Hi %s, I am the %s script." % (name, argrawscript)
intro = raw_input(prompt)

print "Can we talk %s?" % name
talk = raw_input(prompt)

print "%s never mind I must go, write the first thing that comes to your mind..." % name
go = raw_input(prompt)

print "Your name is %s, you said %s and what came to your mind was %s" % (intro, talk, go)
