#union()
#Its basically same as the union of maths.
s1 = {2,3,4}
s2 = {4,5,6}
print(s1.union(s2))
print(s2.union(s1))
#Both will be the same.

#intersection()
#Same as intersection of sets in maths.
print(s1.intersection(s2))
print(s2.intersection(s1))
#Both will be the same.

#difference()
#s2-s1 can be read as s2 without the elements that are common in s1 and s2 (intersection)
print(s2.difference(s1)) #Prints s2 without the common element (4).
print(s1.difference(s2)) #Prints s1 without the common element (4).
print(s2-s1) #Same as s2.diff(s1)

#intersection_update()
#The syntax is s1.intersection_update(s2).
#It changes the s1 completely to the intersection of s1 and s2.
s3 = {5,6,7}
s3.intersection_update(s2) #Updates it to s3 = {5,6}
print(s3)

#issubset()
#s2.issubset(s1)
#Checks if s2 is the subset of s1.
s4 = {6}
print(s4.issubset(s3)) #Prints True.

#issuperset()
#s2.issuperset(s1)
#Checks if s1 is the subset of s2.
print (s3.issuperset(s4)) #Prints True

#isdisjoint()
#Checks if there is any intersection bw the 2 sets.
print(s1.isdisjoint(s4))


