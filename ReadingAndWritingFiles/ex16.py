from sys import argv

script, filename = argv

print "We're going to erase %r. " % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Trucating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

# Study Drills

# 1. IF you feel you do not understand this, go back through and use the
# comment trick to get it squared away in your mind. One simple English
# comment above each line will help you understand or at least let you
# know what you need ot research more.

# 2. Write a script similar to the last exercise that uses read
# and argv to read the file you just created.

# 3. There's too much repetition in this file. Use
# strings, formats, and escapes to print
# out line1, line2, and line3 with just one target.write()
# command instead of 6
