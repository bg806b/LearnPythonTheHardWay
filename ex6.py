#define x 
x = "There are %d types of people." % 10

#define binary
binary = "binary"

#define do_not
do_not = "don't"

#define y
y = "Those who know %s and those who %s." % (binary, do_not)

#print x + y
print(x)
print(y)

#print the previous x + y with "I said"  & "I also said"
print("I said: %r." % x)
print("I also said: '%s'." % y)

#define hilarious
hilarious = False

#define joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

#print joke eval
print(joke_evaluation % hilarious)

#def w+e
w = "This is the left side of..."
e = "a string with a right side."

#print the cat of w + e
print (w + e)
