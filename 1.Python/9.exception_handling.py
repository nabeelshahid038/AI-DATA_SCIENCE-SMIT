""" 
Exception handling:
    Exception means an error.
        types of error:
            1. Syntax error
            2. Logical error
            3. Runtime error
    -> we had three clauses in EH.
        1. try : we provide the code to try if there is an error.
        2. except : except cluase will only be executed
                    when there is an error in try cluase
        3. finally : this block of code will run always no matter the situation is 

        Common Exception Types

            Exception	                     Description

        ValueError	                      Wrong value type
        TypeError	                      Wrong data type
        ZeroDivisionError	              Division by zero
        FileNotFoundError	              File not found
        IndexError	                      Index out of range
        KeyError	                      Missing dictionary key
        ImportError	                      Module not found
"""

# try:
#     a = int(input())
# except Exception as e:
#     print("Invailid input!!!",e)
# finally:
#     print("this will always execute")


data = {
    "Name" : "Nabeel",
    "Balance" : 1000,
    "Pin" : 1234
}

print("=== Welcome to ATM ===")

# 1. PIN Verification Loop
while True:
    try:
        userpin = int(input("Please enter your PIN: "))
        if userpin == data['Pin']:
            print(f"\nHello {data['Name']}! Login Successful.")
            break
        else:
            print("Wrong PIN! Try again.\n")
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")

# 2. Main Menu Loop
while True:
    print("\n" + "="*20)
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    print("="*20)
    
    try:
        userselection = int(input("Enter your selection: "))
    except ValueError:
        print("Invalid Selection! Please enter a number.")
        continue

    if userselection == 1:
        print(f"Your current balance is: Rs. {data['Balance']}")
        
    elif userselection == 2:
        try:
            amount = int(input("Enter amount to withdraw (Multiples of 500): "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > data['Balance']:
                print("Insufficient Balance!!!")
            elif amount % 500 != 0:
                print("Amount must be a multiple of 500...")
            else:
                data['Balance'] -= amount
                print(f"Withdrawal successful! Remaining Balance: Rs. {data['Balance']}")
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
            
    elif userselection == 3:
        try:
            amount = int(input("Enter amount to deposit (Multiples of 500): "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount % 500 != 0:
                print("Amount must be a multiple of 500...")
            else:
                data['Balance'] += amount
                print(f"Deposit successful! New Balance: Rs. {data['Balance']}")
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
            
    elif userselection == 4:
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Please select a valid option (1-4).")