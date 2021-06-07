from datetime import datetime
class Bank:
    
    
     name="kcb"
    
    
     def __init__(self,name,phonenumber):
         self.phonenumber=phonenumber
         self.name=name
         self.balance=0
         self.statement=[]
         self.loan=0
         
     def show_balance(self):
          return f"Hello {self.name} your balance is {self.balance}" 
      
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
         return f"Dear customer {self.name} you have borrowed {self.loan}"
     
     def repay(self,amount):
         self.loan-=amount
         return f"Dear customer {self.name} you loan is {self.loan} shillings you have paid {amount}"
     def show_statement(self):
        for transaction in self.statement:
             amount=transaction["amount"]
             narration=transaction["narration"]
             time=transaction["time"]
             date=time.strftime("%d/%m/%y")
             print (f"{date}:{narration} {amount}")
     def borrow(self,amount):
         if amount<0:
             return f"the user has no loan {self.name} you qualified for the loan {self.loan}"
         elif self.loan>0:
             return f"you cannot borrow {self.name} please repay your outstanding loan {self.loan}"
         elif amount<0.1*self.balance:
             return f"you not qualified {self.name} you cannot borrow {self.loan}"
         else:
             loan=amount*1.05
             self.loan=loan
             self.balance+=amount
             now=datetime.now()
             transaction={
               "amount":amount,
               "time":now,
               "narration":"you deposited"
               }
             self .statement.append(transaction)
             return f"Dear {self.name} you have borrowed {self.loan} your balance is {self.balance}"
     def repay(self,amount):
         if amount<0:
             return f"Dear {self.name} you cannot repay {self.loan} your loan limit is {self.balance*0.05}"
         elif amount<=self.loan:
             self.loan-=amount
             return f"Dear {self.name} you have repayed {self.loan} "
         else:
              diff=amount-self.loan
              self.loan=0
              self.deposit(diff) 
              now=datetime.now()
              transaction={
               "amount":amount,
               "time":now,
               "narration":"you deposited"
               }
              self .statement.append(transaction)            
              return f"Dear {self.name} you have repayed {self.loan} your loan balance{self.balance}"
             
     
             
             
       