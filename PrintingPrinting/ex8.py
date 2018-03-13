formatter = "%r %r %r %r"
# repeat 1,2,3,4
print formatter % (1,2,3,4)
# repeat "one","two","three","four"
print formatter % ("one","two","three","four")
# repeat True, False, False True
print formatter % (True, False, False, True)
# repeat '%r,%r,%r,%r','%r,%r,%r,%r','%r,%r,%r,%r','%r,%r,%r,%r'
print formatter % (formatter, formatter, formatter, formatter)
# prints all 4 strings
print formatter % (
    'I had this thing.',
    'That you could type up right.',
    "But it didn't sing",
    'So I said goodnight.'
    )

# Study Drills
# 1. Do your checks of your work, write down your mistakes, and try not to make
# them on the next exercise.
# 2. Notice that the last line of output uses both single-quotes and double-quotes
# for individual pieces. Why do you think that is?
# The reason why both single quotes and double quotes were used was because,
# to make sure that it stays a line of code and doesn't break or break
# into seperate lines. " ' "
