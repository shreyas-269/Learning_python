#Example for theory line number 21.

# When you create a class in Python, "self" is how the object keeps track of itself.
# It’s like saying:
# “When this function runs, I’m talking about this particular object.”

#__init__" is a special function which runs first as soon as the object is created.
#Its called constructor because it constructs the object with the data you give it.
#It takes self argument and other arguments as well.

class dog:
    def __init__(self, name, age, owner):
        self.name = name #This will have to be given as an attribute.
        #self.name is oops syntax. You will have to give a name in the brackets while object instantiation. 
        self.age = age #This will have to be given as an attribute.
        self.owner = owner #This will have to be given as an attribute.
    def making_the_dog_bark(self):
        print(f"{self.name} says woof.")
dog_details = dog("Harris Rauf", 31, "Virat Kohli" )
dog_details_in_a_string = f'''Name of the dog is {dog_details.name}
Age of the dog is {dog_details.age}
Owner of the dog is {dog_details.owner}'''
print(dog_details_in_a_string)
dog_details.making_the_dog_bark()

dog_details.owner = "Tilak Verma"
dog_details_in_a_string2 = f'''Name of the dog is {dog_details.name}
Age of the dog is {dog_details.age}
Owner of the dog is {dog_details.owner}'''
print(dog_details_in_a_string2)
dog_details.making_the_dog_bark()