class Account:
    def __init__(self,bal,acc):
        self.accno = acc
        self.balance = bal
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"has been credited into your account")
        print("Total balance = ", self.get_balance())
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"has been debited from your account")
        print("Total balance = ", self.get_balance())
        
    def get_balance(self):
        return self.balance
        
c1 = Account(10000, "022310137704")
c1.debit(1000)
c1.credit(500)
