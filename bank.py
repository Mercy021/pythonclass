class Bank:
    
    # type="online"
     name="kcb"
    
    
     def __init__(self,name,phonenumber):
         self.phonenumber=phonenumber
         self.name=name
         self.balance=0

     def show_balance(self):
          return f"Hello{self.name}your balance is{self.balance}" 
     def deposit(self,amount):
         self.balance+=amount
         return self.show_balance()
     def withdraw(self,amount):
        self.balance-=amount
        return self.show_balance()
     def update(self,amount):
         if amount>0:
            self.balance+=amount
            return f"Hello your balance is{self.show_balance}"
         else:
          return f"you cannot deposit{amount}it is beyond minimum"
     def borrow(self,amount):
         self.balance+=amount
         return f"Dear customer{self.name} you have borrowed{self.loan}"
     def repay(self,amount):
         self.loan-=amount
         return f"Dear customer{self.name} you loan is{self.loan} shillings you have paid{amount}"
      
         
         
    
       