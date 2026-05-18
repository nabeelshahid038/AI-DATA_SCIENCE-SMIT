"""
Conditional Statements:
	if statements:
		syntax: if condition:
			---- body of if
	else statement:
		syntax:	else:
			---- body of else.
"""

""" x = 6
y = 3

if x>y and x>5:
    #body of if
    print(f"x={x} is greater than y={y}")
else:
    print(f"x={x} is less than y={y}") """

# create a variable named as number and get a number from user using input()
# print if the number is even or odd (hint: number % 2 == 0)

""" number = int(input("Enter your number to check: "))
if number % 2 == 0:
    print(f"The number = {number} is even")
else:
    print(f"The number = {number} is odd") """


# if the users age is above 18 so he/she can vote
'''
age = int(input("Enter your age to check: "))

if age >= 18:
    print("You are eleigible to vote...")
else:
    print("You are underage for voting!!!")
'''
# 1. find the number is positive or negative
# 2. store the marks for a student in a variable if marks are above 50 the student is pass else fail.
# 3. if the number is completely divisible by 5 show a message ("Divisible by 5")or("not divisible by 5")

'''
num = int(input("Enter a number: "))
if num >= 0:
    print("The number is positive...")
else:
    print("The number is negative...")


marks = int(input("Enter a marks: "))
if marks >= 50:
    print("Pass...")
else:
    print("Fail...")


num1 = int(input("Enter a number: "))
if num1%5 == 0:
    print("Divisible by 5...")
else:
    print("Not Divisible by 5...")
'''

""" x = 8
y = 7

if x>y :
    print(f"x = {x} is greater than y = {y}")
elif x<y:
    print(f"x = {x} is less than y = {y}")
elif x == y:
    print(f"x = {x} is equals to y = {y}") """

# grade check system where
#(marks > 50 - 59 is D)
#(marks > 60 - 69 is C)
#(marks > 70 - 79 is B)
#(marks > 80 - 100 is A)

# Task :
# Step 1: Create some variables (Name,Fname,Phone,Email,Pass) and store 
#         your information.
# Step 2: Create two more variables (useremail and userpass) get user inputs for
#         useremail and userpass
# Step 3: Compare useremail with email and userpass with pass if both are equal
#         print user name, fname, phone else print 'incorrect pass or email'
'''
Name = 'Yasir'
Fname = 'Nawaz'
Phone = '030065347632'
Email = 'abc@gmail.com'
Pass = 'abc123'

useremail = input('Enter your email: ')


if useremail == Email and userpass == Pass:
    print(f"Name: {Name}")
    print(f"FName: {Fname}")
    print(f"Phone: {Phone}")
else:
    print("Incorrect email or pass...!!")
'''
# --------------------------------------
"""
Nasted if:
    syntax:
            if condition:   #(outer if)
                #body of outer if
                if condition:   #(inner if)
                    #body of inner if
 if useremail == Email:
    userpass = input('Enter your pass: ')
    if userpass == Pass:
        print(f"Name: {Name}")
        print(f"FName: {Fname}")
        print(f"Phone: {Phone}")
    else:
        print("Incorrect Password..!!!")
else:
    print("User not found..!!!") """


# grade check system where
#(marks > 50 - 59 is D)
#(marks > 60 - 69 is C)
#(marks > 70 - 79 is B)
#(marks > 80 - 100 is A)

""" marks = int(input("Enter your marks : "))

if marks >= 80 and marks <= 100:
    print("Your Grade is A")
elif marks >= 70:
    print("Your Grade is B")
elif marks >= 60:
    print("Your Grade is C")
elif marks >= 50:
    print("Your Grade is D")
else:
    print("Unfortunately You are fail") """