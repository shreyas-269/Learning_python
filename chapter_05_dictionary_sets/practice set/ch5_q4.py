s = set()
s.add(20)
s.add(20.0) #This is same as 20 so it wont get added.
s.add('20')
print(s)
print(len(s))
