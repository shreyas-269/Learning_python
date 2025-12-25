#Strings are immutable. Functions like replace don't change the original string, they create a new string with the desired change.

name = "izumi"

#Endswith()
print(name.endswith("mi")) #True
print(name.endswith("miya")) #False
print(name.endswith("Mi")) #False
#The output is returned in true or false.

#Startswith()
print(name.startswith("iz")) #True
print(name.startswith("ky")) #False
print(name.startswith("Iz")) #False

#Capitalize(), capitalizes first word of the sentence.
lyric = "what makes you think im not in love." 
print(lyric.capitalize()) 
#lower() converts all the words into lower case.
Red_haired_baddie = "Address denA"
print(Red_haired_baddie.lower())
#upper() converts all the words into upper case.
print(Red_haired_baddie.upper())
#title() converts the first letter of all the words into capital.
print(lyric.title())
#swapcase() converts all the capital into small and small into capital.
print(Red_haired_baddie.swapcase())

#Replace()
print(lyric.replace("makes you think im not in love", "you know about love, i got what you need"))

#Replace() replaces the old string with the new string, old string being at the left of comma and new string being at the right
#It replaces all occurences.
lust_for_life = '''Cause we're having too much fun
Too much fun tonight, yeah
And a lust for life, and a lust for life
And a lust for life, and a lust for life
Keeps us alive, keeps us alive
Keeps us alive, keeps us alive
And a lust for life, and a lust for life
And a lust for life, and a lust for life
Keeps us alive, keeps us alive
Keeps us alive, keeps us alive'''
print(lust_for_life.replace("lust", "tharak"))

#strip() cleans all the whitespaces
text = "   halo   "
clean_text = text.strip()
print(text)
print(clean_text)
#lstrip() cleans the leading whitespaces (left side of halo)
lstrip_text = text.lstrip()
print(lstrip_text)
#rstrip() cleans the trailing whitespaces (right side of halo)
rstrip_text = text.rstrip()
print(rstrip_text)

#Find()
print(name.find("i"))
#It returns the first occuring index of that character in the string.
print(name.find("mi"))
#The first occurence of this string (position of m) was at the index 3, so it gave 3 as the output.
#rfind() gives the index of the last occurence of the character.
print(name.rfind("i"))
#find() gives -1 as output if it isnt able to find the character.
print(name.find("a"))

#index() is like find(), but it gives a value error if it isnt able to find the character.
#It also has rindex()
print(name.index("a"))

#Count()
print(name.count("i"))
#It will count the number of times i is in that string.



