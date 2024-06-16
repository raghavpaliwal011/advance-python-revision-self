class minecraft_god():
    def __init__(self,name,rank):
        self.name = name 
        self.rank = rank

    def print_details(self):
        print(f"the name of this god gamer is {self.name} and his rank is {self.rank}")
 
class minecraft_pro(minecraft_god):
    def detailer(self):
        print (f"the name of this pro gamer is {self.name} and his rank is {self.rank}")

class minecraft_noob (minecraft_god):
    def detail(self):
        print(f"the name of this noobest gamer is {self.name} and his rank is {self.rank}")   

class minecraft_beginner(minecraft_pro):
    def teller(self):
        print (f"the name of this beginner gamer is {self.name} and his rank is {self.rank}")     
raghav = minecraft_god("raghav","god")
raghav.print_details()
lakshit = minecraft_pro("lakshit","pro")
lakshit.detailer()
processor = minecraft_noob("krishna urf processor","noob")
processor.detail()
manthan = minecraft_beginner("manthan","beginner")
manthan.teller()