# -- coding: utf-8 --
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()


# Study Drill

# 1. Above each line, write out in English what that line does.
# 2. search for python open.
# 3. I used the name "commands" here, but they are also called
# "functions" and "methods." Search around online to see what other
# people do to define these. Do not worry if they confused you.
# It's normal for programmers to confuse you with vast extensive
# knowledge.
# 4. Get rid of the part from lines 10-15 where you use raw_input
# and try the script then.
# 5. Use only raw_input and try the script that way. Think
# of why one way of getting the filename would be better than another
# 6.Run pydoc file and scroll down until you see the read() command (method/function).
# See all the other ones you can use? Skp the ones that have__(two underscores)
# in front because those are junk. Try some of the other commands
# 7.Start python and and use open from the prompt. Notice how you can open
# files and run read on them right there?
# 8 Have you script also do a close() on the txt and txt_again variables.
# It's important to close files when you are done with them.
