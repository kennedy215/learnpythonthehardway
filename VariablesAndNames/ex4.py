cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

#prints the string then displays the assigned var and prints string
print "There are", cars, "cars available."
#prints string displays the assigned variable which is a float and a string.
print "There are only", drivers, "drivers available."
#prints a string calculates cars not driven which gets the results of cars
#subtracted from drivers
print "There will be", cars_not_driven, "empty cars today."
#returns a string and shows the product of carpool_capacity
print "We can transport", carpool_capacity, "people today."
#returns the strings and displays the content of the variable passengers
print "We have", passengers, "to carpool today."
#returns the strings and prints the result of average passengers in the car.
print "We need to put about", average_passenger_per_car, "in each car."

# Study drills

# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens
# if it's just 4? It's not neccesary to use a floating point in this
# case if you use 4, 4 will print.

# 2. Remember that 4.0 is a "floating point" number. Find out what that means.
# also know as real numbers and are written with decimal points.

# 3.Write comments above each of the variable assignments.

# 4.Make sure you know what = is called (equals) and that it's making names for things.

# 5. Remember that_is an underscore character

# 6. Try running Python as a calculator like you did before and use variable names to do your
# calculations. Popular variable names are also i, x, and j.


i = 100
o = 4.0
x = 30
p = 90
n = i - x
l = x
z = l * o
a = p / l

#prints the string then displays the assigned var and prints string
print "There are", i, "cars available."
#prints string displays the assigned variable which is a float and a string.
print "There are only", x, "drivers available."
#prints a string calculates cars not driven which gets the results of cars
#subtracted from drivers
print "There will be", n, "empty cars today."
#returns a string and shows the product of carpool_capacity
print "We can transport", z, "people today."
#returns the strings and displays the content of the variable passengers
print "We have", p, "to carpool today."
#returns the strings and prints the result of average passengers in the car.
print "We need to put about", a, "in each car."
