L = []
for k in range(1,7):
    if k == 1:
        m1 = int(input(f"marks of the {k}st student is: " ))
        L.append(m1)
    elif k == 2:
        m2 = int(input(f"marks of the {k}nd student is: "))
        L.append(m2)
    elif k == 3:
        m3 = int(input(f"marks of the {k}rd student is: "))
        L.append(m3)
    else:
        m = int(input(f"marks of the {k}th student is: "))
        L.append(m)
L.sort()
a,b,c,d,e,f = L
print(a,b,c,d,e,f)

    
