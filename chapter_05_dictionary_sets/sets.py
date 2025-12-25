#Collection of unordered non repetitive elements.
#The elements are unordered hence no indexing is there.
#Closed in curly brackets.
s1 = {1,2,5}
print(type(s1))

s2 = {} #This is an empty dict, not an empty set
s3 = set() #This is an empty set.
print(type(s3))

#Set only takes a value once, no repition allowed.
#So we use sets when no repetition is allowed in the desired code.
s4 = {1,7,43,3,7,43,3}
print(s4) #Order wont be maintained in the output, it would be something like {1,3,43,7} (it is not decided on the basis of ascending order)
#If you want a set sorted in ascending order, use sorted (). 
ascending_s4 = sorted(s4)
print(ascending_s4) #The output will be a list though.
#For descending order:-
descending_s4 = sorted(s4, reverse=True)
print(descending_s4)

#We cant change any item of a set.

#A set can only contain immutable objects.
#Lists are mutable, they cant be the elements of a set.
s5 = {8, 7, 12, "Harry", (1,2)}
print(s5)

