names = {}

for i in range(1,5):
    name = input("Enter your name: ")
    fav_lang = input("Enter your fav lang: ")
    names.update({name:fav_lang})

print(names)

#If any name is repeated, it will be included only once.
#Keys are unique.
#Values can be repeated though.
