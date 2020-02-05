# consultant
class Consultant:
    name = ""
    skill = ""
    exp = 0
    sal = 0

    def __str__(self):
        return self.name+""+self.skill+""+str(self.exp)+""+str(self.sal)+"\n"


class Org(Consultant):
    name = ""
    skill = ""
    exp = 0
    sal = 0

    def __add__(self, set):
        if self.skill == "python" or self.skill == "AI" and self.exp > 3 or self.exp < 8:
            self.sal = 7000
        elif self.skill == "c" or self.skill == "java" or self.skill == "c++" or self.skill == "python" and self.exp >= 4 or self.exp <= 10:
            self.sal = 5000
        elif self.skill == "java" or self.skill == "python" and self.exp > 5 or self.exp <= 10:
            self.sal = 12000
        else:
            print("Sorry Sir ur not eligible for this position")

        def __str__(self):
            return self.name+""+self.skill+""+str(self.exp)+""+str(self.sal)+"\n"


com1 = org()
com1.name = 'Kat'
com1+"python"
com1+3
print(com1)

com2 = org()
com2.name = 'Katti'
com2+"c++"
com2+10
print(com2)

com3 = org()
com3.name = 'Kia'
com3+"java"
com3+6
print(com3)

com4 = org()
com4.name = 'Kaira'
com4+"c"
com4+9
print(com4)

