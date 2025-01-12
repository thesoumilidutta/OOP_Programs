from datetime import datetime

class Bankaccount():
    def __init__(self,accno,accholder,balance):
        self.__accountnumber=accno
        self.__accholder=accholder
        self.__balance=balance
        self.transaction=[]

    def display(self):
        print("The account number is: ",self.__accountnumber)
        print("The name of the account holder is: ",self.__accholder)
        print("The balance of the account is: ",self.__balance)
    
    def deposit(self):
        amount=int(input("Enter the amount to be deposited :"))
        print("The new balance is : ",self.__balance+amount)
        self.__balance=self.__balance+amount
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.addTransaction(["deposit",amount,self.__balance,time])
    
    def withdraw(self):
        amount=int(input("Enter the amount to be withdrawn :"))
        print("The new balance is : ",self.__balance-amount)
        self.__balance=self.__balance-amount
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.addTransaction(["withdraw",amount,self.__balance,time])

    def addTransaction(self,lis):
        self.transaction.append(lis)

    def displayTransaction(self):
        print(" THE TRANSACTION HISTORY: ")
        for i in self.transaction:
            print("Type:",i[0],", Transaction Amount:",i[1],", Balance:",i[2],", Time:",i[3])

print("WELCOME TO OUR MINI BANK SYSTEM -->")
accountNum=int(input("Please enter your account number:"))
accHolderName=input("PLease enter name of the account holder:")
accBalance=int(input("Enter the current account balance:"))
account=Bankaccount(accountNum,accHolderName,accBalance)
response=""
print("Answer 'y' for yes and 'n' for no ")
response=input("Do you want to view the current balance?")
if response.lower()=="y":
    account.display()
response=input("Do you want to deposit money?")
if response.lower()=="y":
    account.deposit()
response=input("Do you want to withdraw money?")
if response.lower()=="y":
    account.withdraw()
response=input("Do you wish to view your transaction history?")
if response.lower()=="y":
    account.displayTransaction()