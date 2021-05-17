class Bank:
    type="online"
    name="kcb"
    
    def __init__(self,type,name):
         self.type=type
         self.name=name
    def accountNumber(self):
        return f"Hello,my bank accountNumber is {self.name}"
    def withdraw(self):
        return f"Hello,my withdrawed money is{self.name}"    