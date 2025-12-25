#get()
#get(key,default) is the syntax.
#Returns the value for a key and if it doesnt exist it returns the default value.
#Normal marks["harry"] method gives an error if the key DNE.
d1 = {                
    "Harry": 100,        
    "Shubham": 56,
    "Rohan": 23,
    "list" : [1,2,9]
}
print(d1.get("Harry", 0))
print(d1.get("izumi","atmkbfj"))
print(d1.get("abc"))

#update()
#dictionary.update({key:value}) is the syntax.
d1.update({"izumi" : 78})
d1.update({"Rohan" : 46})
print(d1)

#popitem()
#Removes and return the last inserted key value pair.
d1.popitem() #Izumi will be removed as it was last added.
print(d1) 

#pop()
# dict.pop(key,default value) is the syntax.
d2 = {                
    "Harry": 100,        
    "Shubham": 56,
    "Rohan": 23,
    "list" : [1,2,9]
}
print(d2.pop("Shubham", "no key found")) #This will return the value of Shubham and remove it from the dict
print(d2.pop("a", "none"))
print(d2)

#clear() removes all of the items in the list.
d2.clear()
print(d2) #This will print an empty dict.

#keys()
# dict.keys()
#Returns a view object of all the keys in the form of dict_keys[]
d3 = {                
    "Harry": 100,        
    "Shubham": 56,
    "Rohan": 23,
    "list" : [1,2,9]
}
keys = d3.keys()
print(keys)
#THis prints dict_keys which is a view object.
#View object is like a live window of whats inside a dict.
#Its diff from list.
#Its immutable as its in read-only view.
#If the dict changes, view updates change instantly.
#It doesnt have an indexing, we have to first convert it into a list for indexing.
a = list(keys) #Converting dict_keys into list.
print(a)
print(a[0]) #This is how you get indexing in dict_keys.

#values()
#Returns view only object for values.
values = d3.values()
print(values)
b = list(values)
print(b)

#items()
#Returns view only object for key,value pairs.
items = d3.items() #Returns it in the form of dict_items([('Harry', 100), ('Shubham', 56), ('Rohan', 23), ('list', [1, 2, 9])]).
print(items)
c = list(items)
print(c)

#copy()
#Returns a shallow copy of the dict.
d4 = d3.copy()
print(d4)

#fromkeys()
#Builds a new dict with the keys that you give it in a data type.
#If we assign a value, it will be allotted to all keys.
key_list = ["x", "y", "z"]
val = 60
d5 = dict.fromkeys(key_list, val)
print(d5)
#It will give none if no value is given.
key_list2 = ["x", "y", "z"]
d6 = dict.fromkeys(key_list2)
print(d6)
key_list3 = ("x", "y", "z") #keys can also be given in tuple form.
d7 = dict.fromkeys(key_list3) 
print(d7)

#setdefault()
#dict.setdefault(key, default value) is the syntax.
#It returns the value of key if it exists and add the key in the dict with its value as the default value if it doesnt exist.
d7.setdefault("w", 60)
print(d7)
print(d7.setdefault("x", 60)) #Will return none
