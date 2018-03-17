print("I am 6'2\" tall.") # escape double-quote inside string
print('I am 6\'2" tall.') # escape single-quote inside string

tabby_cat = "\tI'm tabbed in." # escape tabbed
persian_cat = "I'm split\non a line." # escape on a new line
backslash_cat = "I'm \\ a \\ cat." # escape single \

print(tabby_cat)
print(persian_cat)
print(backslash_cat)

#triple quotes: write as much code as needed
fat_cat = """ 
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
 """

print(fat_cat)

#testing the string formats
print("This is me: %s" % tabby_cat)
print("This is also me: %r " % tabby_cat)


