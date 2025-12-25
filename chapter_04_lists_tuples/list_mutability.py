#Containers to a store all data types.
friends = ["abc", 19.3, 13, False] #String, float, integer, boolean all in the same container.
print(friends[0])

#Strings are immutable.
#If there is a string of a = "Izumi" and i want to replace the 0th index using a[0] = A, this will show an error.
#This is cause we cant actually change the original strings through such functions.

#But lists are mutable.
friends[1] = 19.5
print(friends)
#The original list has been changed.
