# define variables, 4 strings
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who %s and those who %s." % (binary, do_not)

# print x and y
print x
print y

# print strings adding x and y to them
print "I said: %r." % x
print "I also said: '%s'." % y

# define a boolean variable
hilarious = False
# define a string with a substitution at the end
joke_evaluation = "Isn't that joke so funny?! %r"

# print the string
print joke_evaluation % hilarious

# define two strings
w = "This is the left side of..."
e = "a string with a right side."

# print and concatenate them
print w + e
