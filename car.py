class Car:
    model="Mazda"
    color="red"
    
    def __init__(self,model,color):
         self.model=model
         self.color=color
    def speed(self):
            return f"Hello,my model is{self.model}"
    def accelarate(self):
        return f"Hello my car accelarate is{self.color}"
                