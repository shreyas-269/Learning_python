#Dictionary is a collection of keys-value pairs.
marks = {                #Curly brackets are used for dict.
    "Harry": 100,        #A key-value pair is formed.
    "Shubham": 56,
    "Rohan": 23,
    "list" : [1,2,9]
}
print(marks, type(marks)) 

#Indexing doesnt exist in dict.
#Values are accessed by their respective keys.
# print(marks[0]) will give an error.
print(marks["Harry"]) #This is how you access the value of a key.

print(marks["list"]) #This will return the list.

#Dictionaries are unordered, mutable, indexed.
#They cant contain duplicate keys.

