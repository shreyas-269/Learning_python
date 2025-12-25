class employee:
    def __init__(self, name, job_role, salary):
        self.name = name
        self.job_role = job_role
        self._salary = salary #Marking this attribute as internal as it will be changed inside the class.
        self._increment = 0
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        self._salary = value
    
    @property
    def increment(self):
        return self._increment
    
    @increment.setter
    def increment(self, value):
        self._increment = value
    
    @property
    def salary_after_increment(self):
        return self._salary + self._increment
    
    @salary_after_increment.setter
    def salary_after_increment(self, value):
        self._salary + self._increment = value
        print(f"Salary after increment is {value}")

izumi = employee("Izumi", "AiMl", "1")
izumi.increment()