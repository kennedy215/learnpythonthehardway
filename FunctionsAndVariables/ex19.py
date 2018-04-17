# function that passes in the argument cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints the data of cheese_count
    print "You have %d cheeses!" % cheese_count
    # prints the data of boxes_of_crackers
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # prints the string
    print "Man that's enough for the party!"
    # prints the string then space
    print "Get a blanket. \n"
# print outside the function of cheese and crackers
print "We can just give the function numbes directly:"
# calling the function cheese_and_crackers and stating the variables that'll pass in the arg
cheese_and_crackers(20,30)
# creating 2 new variables and defining data for amount_of_cheese and amount_of_crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# passing in variable amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calling function cheese and crackers and doing the math/passing intergers
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# calling function cheese, crackers placing defined variables with intergers and adding intergers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def deathslog(heart_attacks, cancer, other):
    print " %d people died from heart attack!" % heart_attacks
    print " %d people died from cancer!" % cancer
    print " %d people died from other!" % other

# way 1 calling function and defining integers
print "Way 1"
deathslog(20, 18, 23)
print "\n"

# way 2 using variables from script
print "Way 2 defining variables"
heart_attacks = 20
cancer = 50
other = 93

deathslog(heart_attacks, cancer, other)
print "\n"


# way 3 adding to pre-defined variables
print "Way 3"
deathslog(heart_attacks, cancer, other)
heart_attacks = 20 + 40
cancer = 20 + 5
other = 32 + 43
print "\n"

print "Way 4"

natural_heart_attacks = 5
induced_heart_attacks = 10
natural_cancer = 20
viral_cancer = 2
high_bloodpressure = 3
suicide = 1

deathslog(natural_heart_attacks + induced_heart_attacks, natural_cancer + viral_cancer, high_bloodpressure + suicide)
print "\n"

print "Way 5"

natural_heart_attacks = 5 + 9
induced_heart_attacks = 10 + 0
natural_cancer = 20 + 39
viral_cancer = 2 + 80
high_bloodpressure = 3 + 2
suicide = 1 + 2

deathslog(natural_heart_attacks + induced_heart_attacks, natural_cancer + viral_cancer, high_bloodpressure + suicide)
print "\n"

print "Way 6"

one = natural_heart_attacks + induced_heart_attacks
two = natural_cancer + viral_cancer
three = high_bloodpressure + suicide

deathslog(one, two, three)
print "\n"

print "Way 7"


zoneone = one + two + 3
zonetwo = two + three + 4
zonethree = three + one + 5

deathslog(zoneone, zonetwo, zonethree)

print "\n"

print "Way 8"
deathslog(2 + 2 + 3, 4 * 27, 9 * 9)

print "\n"

print "Way 9"
x = 1
y = 2
z = 3

a = x + z
b = y + z
c = y + x

deathslog(a, b, c)

print "\n"

print "Way 10"
x = 1
y = 2
z = 3

a = x + z
b = y + z
c = y + x

deathslog(a * 10, b * 10, c * 10)











# 1. Go back through the script and type a comment above each line, explaining in English what it does.
# 2. Start at the bottom and read each line backward, saying all the important characters
# 3. Write at least one more function of your own design, and run it 10 different ways.
