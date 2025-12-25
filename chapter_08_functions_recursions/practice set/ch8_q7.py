def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
            print (n)

l = ["Izumi", "Rohan", "an"]
rem(l, "an")