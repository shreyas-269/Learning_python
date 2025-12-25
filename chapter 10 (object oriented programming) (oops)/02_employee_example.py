class employee:
    lang = "python"
    salary = "1rs"

    def greet(self):
        print("good morning")
    
izumi = employee() #This variable is the object.
izumi.name = "Izumi" #This literally means that the name of the object izumi is Izumi
print(izumi.name, izumi.lang, izumi.salary)
izumi.greet()


kyouko = employee()
kyouko.name = "Kyouko"
print(kyouko.name, kyouko.lang, kyouko.salary)
kyouko.greet()

#Lang and salary are the attributes of the class.
#Name is the attribute of the object.
#Object attributes are mostly called instance attributes.
#Instance attributes are given preference over class attributes during assignment and retrieval.










