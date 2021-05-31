from datetime import datetime
class Bank:
    
    
     name="kcb"
    
    
     def __init__(self,name,phonenumber):
         self.phonenumber=phonenumber
         self.name=name
         self.balance=0
         self.statement=[]
         
     def show_balance(self):
          return f"Hello{self.name}your balance is{self.balance}" 
      
     def deposit(self,amount):
        if amount<0:
            return "refused" 
        else:
            self.balance+=amount 
            now=datetime.now()
            transaction={
               "amount":amount,
               "time":now,
               "narration":"you deposited"
               }
            self .statement.append(transaction)
            
        return self.show_balance()
    
     def withdraw(self,amount):
         if amount>0:
          self.balance-=amount
          now=datetime.now()
          transaction={
               "amount":amount,
               "time":now,
               "narration":"you deposited"
               }
         self .statement.append(transaction)
         return self.show_balance()
    
     def borrow(self,amount):
         self.balance+=amount
         return f"Dear customer{self.name} you have borrowed{self.loan}"
     
     def repay(self,amount):
         self.loan-=amount
         return f"Dear customer{self.name} you loan is{self.loan} shillings you have paid{amount}"
     def show_statement(self):
        for transaction in self.statement:
             amount=transaction["amount"]
             narration=transaction["narration"]
             time=transaction["time"]
             date=time.strftime("%d/%m/%y")
             print (f"{date}:{narration} {amount}")
        
        
             
         
      
         
         
    
       