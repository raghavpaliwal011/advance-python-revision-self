class parent ():
    def __init__(self,name):
        self.name = name 

    def print_details(self):
        print (f"the name of this employee is {self.name}")

class son():
    def __init__ (self,work):
        self.work = work
    def print_details(self):
        print (f"the work of raghav is {self.work}")

class son_of_parent(son,parent):
    def __init__(self,name,work):
        self.name = name 
        self.work = work

    def print_details(self):
        print (f"the name of this person is  {self.name} and his work is {self.work}")

raghav = son_of_parent("raghav","programmer")
raghav.print_details()