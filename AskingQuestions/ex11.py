print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Study Drills

# Go online and find out what Python's raw_input does.
# raw_input([prompt])
# If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised.
# Can you find other ways to use it? Try some of the samples you find.
# Write another "form" like this to ask some other questions
# Related to escape sequences, try to find out why the last line has '6\'2"'
# with that \' sequence. See how the single-quote needs to be escaped
# because otherwise it would end the string.
name = raw_input('What\'s your name? : ')
## prints Jimbo after answer is given.
hobby = raw_input('What\'s your hobby? : ')
print "So, your name is %r and your hobby is %r? %r I think that is awesome!" % (name,hobby,name)
