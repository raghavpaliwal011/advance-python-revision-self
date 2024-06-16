class minecraft_god():
    def __init__(self,name,rank):
        self.name = name 
        self.rank = rank

    def print_details(self):
        print (f"the name of this god player is {self.name} and his rank is {self.rank}")

class minecraft_pro(minecraft_god):

    def the_details(self):
        print (f"the name of this pro player is {self.name} and his rank is {self.rank}")

class minecraft_noob (minecraft_god):
    def teller(self):
        print(f"the name of this ultra noob player is {self.name} and his rank is {self.rank}")

class minecraft_beginner (minecraft_pro,minecraft_noob):
    def details (self):
        print (f"the name of this beginner player is {self.name} and his rank is {self.rank}")
raghav = minecraft_god("raghav","gladiator")
raghav.print_details()
lakshit = minecraft_pro("lakshit","hero")
lakshit.the_details()
harshit = minecraft_noob("harshit","noob")
harshit.teller()
krishna = minecraft_beginner("krishna","beginner")
krishna.details()
