class Dog:
    breed="Bulldog"
    color="grey"
    
    
    def __init__(self,breed,color):
         self.breed=breed
         self.color=color
    def bite(self):
        return f"Hello chew,my pet bites strangers {self.breed}"
    def bark(self):
        return f"Hello,my dog barks every morning {self.breed}"         