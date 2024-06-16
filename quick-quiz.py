class animal ():
    def __init__(self,animal,sound):
        self.animal = animal
        self.sound = sound
    def animal_detail(self):
        print (f"this is an {self.animal} which makes sound of {self.sound}")


class cat (animal):
    def cat_details(self):
        print (f"this is an {self.animal} which makes sound of {self.sound}")
parent_cat = animal("cat","meaow")
parent_cat.animal_detail()
kid_cat = cat("kid cat","meaow")
kid_cat.cat_details()


