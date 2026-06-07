"""
decorator : 

"""

def greeting_decorator(func):
    def wrapper(*args,**kwargs):
        print("Hello! Welcome to SMIT")
        func(*args,**kwargs)
        print("GoodBye!! Thankyou for Visiting SMIT")
    return wrapper

def confirmation_decorator(func):
    def wrapper(*args,**kwargs):
        user_input = input("Enter y to confirm : ")
        if user_input.lower() == "y":
            func(*args,**kwargs)
    return wrapper


def logs_decorator(func):
    def wrapper(*args,**kwargs):
        with open("15.logs.txt","a") as file:
            file.write("functions has been called")
        func(*args,**kwargs)
    return wrapper

@greeting_decorator
@confirmation_decorator
@logs_decorator
def printer(*args,**kwargs):
    print(args[0],kwargs["message2"])

printer("hello",message2="this is me")


class ATM:
    def __init__(self, acc_title:str, balance:int):
        self.acc_title = acc_title
        self.balance = balance

    def check_balance(self):
        return f"your balance is {self.balance}"
    
    def view_acc_title(self):
        return f"Account title : {self.acc_title}"

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw in multiple of (500) : "))
        if amount <= self.balance:
            self.balance -= amount
        print("money withdrawn successfull")

    def deposit(self):
        amount = int(input("Enter the amount to deposit  : "))
        if amount > 0:
            self.balance += amount
        print("money deposited successfull")

    def 

        