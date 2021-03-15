class bankaccount:
    def __init__(self,accno,name,acctype,balance):
        self.accno= accno
        self.name= name
        self.acctype= acctype
        self.balance= balance

    def deposit(self):
        amount = float(input("\nenter amount to be deposited : "))
        amount = amount + self.balance
        print("\namount deposited :", amount)
    def withdraw(self):
        amount = float(input("enter amount to be writhdrawn"))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou withdrew :", amount)
        else:
            print("\nInsufficient balance !!! ")
    def display(self):
        print("\n account number",self.accno)
        print("Holder Name : ", self.name)
        print("Account Type : ", self.acctype)
        print("Net available Balance : ", self.balance)
t=bankaccount(1232414,"ryan","savings",10000)
t.deposit()
t.withdraw()
t.display()
