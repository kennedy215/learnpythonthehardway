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
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing",
    "So I said goodnight."
    )
