#len()
t1 = (1, 7, 2)
print(len(t1))

#max()
print(max(t1))
# friends = ("abc", 19.3, 13, False)
# print(max(friends)) will give an error.
t2 = ("izumi", "kyouko", "ishikawa")
print(max(t2))
#Kyouko will be the output.
#Python compares these based on a lexicographical (basically dictionary) order

#min()
print(min(t1))
print(min(t2))

#sum()
print(sum(t1))
# print(sum(t2)) will give an error.

#tuple() converts an iterable (list, string etc) and converts it into tuple
l18 = [1,8,7,2,21,15,7]
t3 = tuple(l18)
print(t3)

#count() returns the number of occurences of an item in a tuple.
print(t3.count(7))

#index() returns the index of the first occurence of an item.
print(t3.index(7))

#Slicing
t4 = t3[1:5]
print(t4)

#Concatenation
t5 = t2+t3
print(t5)

#Repitition
t6 = t5*2
print(t6)

#Membership
print('izumi' in t6)
print('izumi' not in t6)
