#+ve and -ve indexing
Name = "Izumi"
# In this, i is on 0th position
# z is on 1st 
# u is on 2nd 
# Indexing from left start with 0
# Indexing from right starts from -1.
# Small i at the last is -1

#Len function
print("length of name is", len(Name))
#Len function measures the characters in a string.
#Output will be 5.

#Slicing
Sliced_name = Name[0:3]
#This is the syntax for slicing the string.
#0th index will be included and 3rd index will be excluded. 
print("The sliced name is", Sliced_name)

#Printing a character of any index.
print("The character at the 1st index of the Name string is", Name[1])
#Name[1] is the syntax for printing the 1st indexed character.

# Name = "Izumi"
#-ve slicing.
print(Name[-4:-1])
#-1 is the last i, its not included in the output.
#-4,-3,-2 are printed.

print(Name[:4])
#If there is nothing written on the left of the :, assume it as 0.
#So this is the same as Name[0:4]
print(Name[1:]) 
#If there is nothing written on the right side of the :, assume it as length-1.
#Length of Izumi is 5, so here it will print till the 4th index (length-1).
#Its same as Name[1:5]

#Preferably convert everything into +ve index and then work.

#Slicing with skip value
Word = "Consequences"
print(Word[1:7:2])
#1st index is of o
#7th index is of e.
#2 is the skip value that is at the right of indexes.
#It will print o, then jump 2 characters and print s, then q (7th won't be included).
#The output will be osq.

Word2 = "aanvay"
print(Word2[5:1:-2])

