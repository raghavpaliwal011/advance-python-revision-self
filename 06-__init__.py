class employee():
    def __init__(self,name,salary,country):
        self.name = name
        self.salary = salary
        self.country = country
    def print_details(self):
        return f"the name of the employee is {self.name} and salary is {self.salary}, country {self.country}"
raghav = employee("raghav",4000000000000,"india")
print (raghav.print_details())