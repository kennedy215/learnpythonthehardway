from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# Study Drills

# 1.Go read up on Python's import statmeent, and start python to try it out
# 2. This scrit is really annoying. There's no need to ask you before
# doing the copy, and it prints too much to the screen. Try to make it
# More friendly to use by removing features.
# 3. See how show you can make the script I could make this one line long
# 4. Notice at the end of the WYSS I used something called cat?
# It's an old command that "concatenates" files together, but mostly it's
# just an easy way to print a file to the screen. type man cat to read about it
# 5. Windows, people find the alternative to cat that Linux/OSX people have
# Do not worry about man since there is nothing like that.
# Find out why you had to do output.close() in the code
