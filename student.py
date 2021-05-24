class Student:
    school="Akirachix"
    
    def __init__(self,firstname,lastname,age):
         self.firstname=firstname
         self.lastname=lastname
         self.age=age
    def greet(self):
        return f"Welcome to school{self.firstname}"
    def year_of_birth(self):
        return f"Hello i was born in{2021-self.age}"
    def initials(self):
        return f"Hello{self.firstname}{self.lastname} your initals are"
             
  