class ATM:
    def __init__(self,deposite_amount,withdraw_amount):
        self.deposite_amount = deposite_amount
        self.withdraw_amount = withdraw_amount
        self.balance = 5000
        pass
    balance = 5000
    def deposite(self):
        if self.deposite_amount > 0:
            self.balance += self.deposite_amount
            print("Money deposited Successfully")
        else:
            print("Invalid Amount")
    def withdraw(self):
        if 0 < self.withdraw_amount < self.balance:
            print("Money withdraw Successfully")
            self.balance -= self.withdraw_amount
        else:
            print("Insuffient balance or Invalid amount")
    def balance_info(self):
        print(f"Total balance : {self.balance}")
while True:
    try :
        deposite = int(input("Enter amount to be deposite : "))
        withdraw = int(input("Enter amount to be withdrawal : "))
        s1 = ATM(deposite,withdraw)
        s1.deposite()
        s1.withdraw()
        s1.balance_info()
    except(ValueError):
        print("Enter amount in Digits only")
    except(Exception):
        print("Something went wrong")
    quit_choice = input("Want to make more deposites\n Press 'q' to quit or Press Enter to continue :")
    if quit_choice.lower() == 'q':
        break