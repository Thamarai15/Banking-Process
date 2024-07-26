class Bank:
    Bankname="Indian Bank"
    Branch="Velachery"

def __init__(self,username,phone_number,pan_number,address):
    self.username=username
    self.phone_number=phone_number
    self.pan=pan
    self.address=address
    self.balance=0.0
    print(f'hello {self.username} your account is created successfully')
 
def deposit(self,amount):
    self.balance=self.balance+amount
    print(f"{amount}) deposited successfully")

def withdraw(self,amount):
    if amount<self.balance+amount:
       self.balance=self.balance+amount
       print(f"{amount} withdraw successfully")
    else:
        print(f"insufficient fund...")

def ministatement(self):
    print(f"your account balance is {self.balance}") 
    

print(f"welcome to {Bank.Bankname},{Bank.Branch}")
username=input("enter your name:")
phone_number=int(input("enter your phone_number:"))
pan_number=input("enter your pan_number:")
address=input("enter your address:") 

customer=Bank(username,phone_number,pan_number,address)
while true:
    print("please select any option")
    print("1.Deposit\n2.withdraw\n3.Ministatement\n4.Close")
    option=int(input(' '))

    if option==1:
        amount=int(input("enter the deposited amount:"))
        customer.deposit(amount)

    elif option==2:
        amount=int(input("enter the withdraw amount:"))
        customer.withdraw(amount)

    elif option==3:
        customer.ministatement()

    elif option==4:
        print(f"Thanks for using {Bank.Bankname}...Visit Again")
        break
    else:
        print("invalid option")
