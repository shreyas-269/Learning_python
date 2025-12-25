#Arithmetic operators are +,-,*,/ etc
#Assignment operators are =, +=, -=
#Comparison operators are ==, >, >=, <, != 
#Logical operators are and,or,not 

#In 7+4=11, 7 and 4 are operands, + is the operator, 11 is the result. 


#Arithmetic operators

a = 7
b = 4
c = a + b
print("c =", c)


#Assignment operators 

d = 4-2 #assign 4-2 in d
print("d =", d)

e = 3
e += 2 #increase the value of the original e by 2 and assign it to e.
print("e =", e)

f = 2
f -= 1 #decrease the value of the original f by 1 and assign it to f.
print("f =", f)

g = 6
g /= 3 
print("g =", g)

h = 2
h *= 3
print("h =", h)


#Comparison operators
#Always gives the return value as Boolean. 

i = 5<4 #< is the boolean operator. The answer will be false.
print("i is", i)

j = 5>4 
print("j is", j)

# >= is greater than or equal to sign 
k = 5>=5
print("k is", k)

#<= is less than or equal to sign.
l = 5<=5
print("l is", l)

#!= is not equal to
m = 5!=6
print("m is", m)
n = 6!=6
print("n is", n)

#== is to check if it is equal to or not
o = 1==4-3
print("o is", o)
p = 2==3
print("p is", p)


#Logical operators

#And returns true if both are correct. False if any one or both are incorrect.
q = (4-3==1) and (4*3==12)
print("q is", q)

#Or returns true if any one or both are correct. False if none is correct.
r = (3*2==6) or (5/1==5)
print("r is", r)
s = (4/2==3) or (6*3==18)
print("s is", s)
t = (5/2==3) or (7*2==15)
print("t is", t)

#Not is like the not gate in logic gates. It turns true into false and false into true
u = (5*2==10)
print("u is", not(u))
v = (6*3==19)
print("v is", not(v))





