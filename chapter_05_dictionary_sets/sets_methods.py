#add()
#Adds a single element in a set.
s1 = set()
s1.add(1)
s1.add("Izumi")
print(s1)

#update()
#Used to add multiple elements.
s1.update(["abc", 19.3, 13, False])
print(s1)
#An iterable is updated inside those brackets, we cant update ints in a set.
#s1.update(2) will give an error.
s1.update("abc") #update() adds the separate elements of the iterable (string in this case).
print(s1) # 'a', 'b', 'c' will be added separately and the rest of the set will be printed along it.
#Use add() to add a whole string.

#Atp s1 = {False, 1, 'abc', 13, 'a', 19.3, 'Izumi', 'b', 'c'}

#remove()
#Removes an element and gives error if the element isnt there.
s1.remove("Izumi")
print(s1)

#discard()
#Removes an element but doesnt give an error if the element isnt there.
s1.discard('a')
print(s1)
# print(s1.discard("b")) will have no return value.
#There are no default values in discard(), it silently ignores if the element isnt there.

#pop()
#Removes an arbitrary (random) element from a set.
#It returns the value of the element removed.
print(s1.pop()) #Printing the return value.
print(s1)

#clear()
s2 = s1.copy() #Creating a copy of the set.
s2.clear() #Clearing it.
print(s2) #Gives an empty test.

#len()
#Gives the number of items in a set.
print(len(s1))

#max()
s3 = {4,6,9,20}
print(max(s3))







