#write a python program To implement multiple inheritance 
class Father:
    def skills_father(self):
        print("Father: Good at Business")
class Mother:
    def skills_mother(self):
        print("Mother: Good at Music")
# Child inherits from both Father and Mother
class Child(Father, Mother):
    def skills_child(self):
        print("Child: Good at Sports")
c = Child()
c.skills_father()   # from Father
c.skills_mother()   # from Mother
c.skills_child()    # own method