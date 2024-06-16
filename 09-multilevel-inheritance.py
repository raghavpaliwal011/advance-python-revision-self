class ceo ():
    def __init__(self,name,work,company):
        self.name = name 
        self.company = company
        self.work = work
        
    
    def print_details(self):
        print (f"the name of this person is {self.name} and his company is {self.company} and his work is {self.work}")

class manager(ceo):
    def __init__(self,name,work,company):
        self.name = name 
        self.company = company 
        self.work = work

    def details(self):
        print (f"the name of the employee is {self.name} and his company is {self.company} and he is {self.work}")
class emmployee (manager):
    def __init__(self, name, work, company):
        self.name = name 
        self.work = work
        self.company = company
    
    def tails(self):
        print (f"the name of this person is {self.name} and he is an {self.work} ,his company is {self.company}")

raghav = ceo("raghav","rockstar games","ceo of the company")
raghav.print_details()
ramesh = manager("ramesh","manager","rockstar games")
ramesh.details()
suresh = emmployee("suresh","employee","rockstar games")
suresh.tails()
