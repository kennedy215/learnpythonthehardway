from sys import argv

# script, user_name = argv
# prompt = '> '
#
# print "Hi %s, I'm the %s scipt." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)
#
# print "Where do you live %s" % user_name
# lives = raw_input(prompt)
#
# print "What kind of computer do you have?"
# computer = raw_input(prompt)
#
# print  """
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# """ % (likes, lives, computer)

# 1. Find out what Zork and Adventure were. Try to find a copy and play it.
# http://textadventures.co.uk/games/play/5zyoqrsugeopel3ffhz_vq
# 2. Change the prompt variable to something else entirely.

script, user_name = argv
computer = '> '

print "Hi %s, I'm the %s scipt." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(computer)

print "Where do you live %s" % user_name
lives = raw_input(computer)

print "How old are you %s?" % user_name
age = raw_input(computer)

print "What kind of computer do you have?"
computer = raw_input(computer)

print  """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer and your only %r years old! Nice.
""" % (likes, lives, computer, age)


# 3. Add another argument use it in your script
# 4. Make sure you understand how I combined a """ style multiline string with
# the % format activator as the last print.
