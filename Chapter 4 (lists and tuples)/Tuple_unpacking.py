t1 = (3,5)
x,y = t1
print(x,y) #This is unpacking.
#Through this x and y will be assigned the value of 3 and 5 respectively.

# t2 = (2,4,5)
# a,b = t2 
#This will give an error as there are too many values to unpack.
#Correct way :-
t2 = (2,4,5)
a,b,_ = t2
print(a,b)

#We use * to gather extra values in a list.
c,*d = t2
print(c,d)

# This works on both strings and lists as well.