#String f() used to return a new string with the desired change.
#List f() return the original string with the desired change.

#append()
#Adds an item at the end of the list.
l1 = ["abc", 19.3, 13, False]
l1.append("Izumi")
print(l1)

#sort()
#Sorts the numbers in the list. But the list should only have integers or float in it.
l2 = [1,4,3,500.3,769]
l2.sort()
print(l2)

# reverse()
#Reverses the order of the list given.
l3 = [1,8,7,2,21,15]
l3.reverse()
print(l3)

#insert()
#Used to add an item at a certain index.
l4 = [1,8,7,2,21,15]
l4.insert(3,8) #This will insert 8 at the 3rd index.
print(l4)

#pop()
#Used to remove an item on a certain index and return its value.
l5 = [1,8,7,2,21,15]
l5.pop(3) #Removes the element at the 3rd index.
print(l5)
#A function does the change and it sometimes has a return value. 
#In pop(), the change is that it creates a new list with the mentioned element removed and its return value is the element that was removed
l6 = [1,8,7,2,21,15]
print(l6.pop(3)) #This will return the return value which is 2.
print(l6) #This willr return the changed list.

#Return value of other functions:-
l7 = [1,8,7,2,21,15]
print(l7.sort()) #Output is none because no value is returned.
#Same with append(), reverse(), insert()

#remove()
#Removes the 1st occurence of the mentioned element from the list.
l8 = [1,8,7,2,21,15,7]
l8.remove(21)
print(l8)
print(l8.remove(7)) #Return value is none.

#len()
l9 = [1,8,7,2,21,15]
print(len(l9))

#in and not in
l10 = [1,8,7,2,21,15]
print(7 in l10) #Returns true.
print(44 in l10) #Returns false.
print(44 not in l10) #Returns true.

#Concatenation
l11 = l9 + l10 #Adds all the elements of both the lists in the same list.
print(l11) 

#Repetition
l12 = l11*2 #Repeats the list 2 times.
print(l12)

#del
#Deletes the item at a certain index.
l13 = [1,8,7,2,21,15]
del l13[2] #Deletes 7 which is at the 2nd index
print(l13)

#extend()
#Adds one list into another.
l14 = [2,4,5]
l15 = [1,3]
l14.extend(l15)
print(l14)

#clear()
#Erases all the items in the list.
l16 = [1,8,7,2,21,15]
l16.clear()
print(l16)
l16.append(1)
print(l16)

#count()
l17 = [1,8,7,2,21,15,7]
print(l17.count(7)) #Counts the number of occurences of 7. 

#copy()
#Copies a shallow copy of the list.
l18 = [1,8,7,2,21,15,7]
l19 = l18.copy()
print(l19)





