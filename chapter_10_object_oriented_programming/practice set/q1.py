class programmer():
    company = "microsoft" #Class attribute 
    def __init__(self, name, age, job_role, salary): #Constructor 
        self.name = name
        self.age = age
        self.job_role = job_role
        self.salary = salary
    
    def printing_details(self):
        details_in_a_string = f'''Name of the employee is {self.name}
Age of the employee is {self.age}
Job role of the employee is {self.job_role}
Salary of the employee is {self.salary}'''
        print(details_in_a_string)

izumi = programmer("Izumi", "19", "intern", "1rs")
izumi.printing_details()
