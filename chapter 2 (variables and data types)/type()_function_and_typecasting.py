# type f() is used to identify the data type of a given variable.
a = 31
print("a is", type(a))
# output is <class 'int'>.

b = "abc"
print("b is", type(b))
#output is <class 'str'>.

c = "31.3"
print("c is", type(c)) #<class 'str'> will be the output.
d = float(c) #covert c into float.
print("d is", type(d)) #
# e=int(c)
# print(type(e)) this wont work because thats a float number.

f = 34
g = float(f)
print("float version of f is", g)

