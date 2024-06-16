class employee ():
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    def print_details(self):
        print (f"the name of this employee is {self.name} and his salary is {self.salary}")
class programmer(employee):
    def details(self):
        print (f"the name of this programmer is {self.name} and salary is {self.salary}")
deepti = employee("deepti",200000)
deepti.print_details()
raghav = employee("raghav",100000)
raghav.print_details()
mohan = programmer("mohan",200000)
mohan.details()
