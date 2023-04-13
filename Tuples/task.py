a=("Aymee","Amad","Mojo")
#a[0] = amna # it gives you error because tuples cannot be directly changed
#a = list(a) doing type casting is possible now we change a[0] = amna,but mostly we use tuples when we don't want to change items.
#print(a)

#   Sets
s = {1,34,65,7,8,4,2,2,1,3,4,5,6,7,7}
#s.add(100)
#s.remove(34)
#s.remove(10) # it gives us error because 10 does not exist in the set so here we use discard function.
s.discard(10) 
print(s) # it doesn't show you the repeated numbers it show number only one time