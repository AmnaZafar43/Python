name = ''' Aymee
is      12
   years     old '''
#print(name)  # This is the way that how we print the same thing on output.

n = "aymee"
#print(n[2:5]) # to divide name into portions it print from 3rd letter to 4th  letter.

name = "\tAymee"
#print(name)
#print(name.strip()) # to ignore the spaces whether it is given space or an escape sequence.

name = "aymee"
#print(len(name)) # to find length.

name = "Amna"
#print(name.lower()) # to print all letters in lowercase.
#print(name.upper()) # to print all letters in uppercase.

name = " amna"
#print(name.replace("a","r")) # to replace letter with a given letter.

name1 = "Aymee is a good girl"
name2 = " and she loves cat"
#print(name1+name2) # to combine two strings

name1 = "amna"
name2 = "amad"
#temp = "{} is a cute girl and {} loves her ".format(name1,name2) # this fromat will place the name ta the given bracket and this is old syntax.
temp = f" {name1} is is a cute girl and {name2} loves her" # this is new syntax that we use.
#print(temp)

a=2
b=3
print(a**b)
print(a//b)