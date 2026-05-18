""" 
Funtion: It is a block of code seperated from atmosphare to perform individual task.

types of functions:
1. pre defined (print,len,input,...)
2. user defined 

To create a user defined function:

syntax:
  def name_of_the_function(     ):
      body of function.

call a function:

syntax:
  name_of_the_function() 
  
  """

# def add():
#     a = 3
#     b = 5
#     print(a+b)

# add()

""" 
Parameters:
    1. required parameters
    2. key parameters (optional) 
    
"""

# return value:
# `    

# def sub(x,y):
#     return x-y


# value = sub(5,6)

# print(value*2)



""" 
def add_students():
    name = input("Enter your name: ") 
    fname = input("Enter your Fname: ") 
    cnic = input("Enter your cnic: ") 
    email = input("Enter your email: ") 
    std_data = view_all_students()
    id = f"SMIT-{len(std_data)+1}"
    with open('11.student.csv','a') as file:
        student = f"{id},{name},{fname},{cnic},{email}\n"
        file.write(student)

def view_all_students():
    try:
        with open('11.student.csv','r') as file:
            std_data = [line.strip().split(',') for line in file.readlines()]
        return std_data
    except FileNotFoundError:
        print("No student is regitered!!!")
        return []
    except Exception as e:
        print(e)
        return []

def search_id(id):
    std_data = view_all_students()
    for std in std_data:
        if std[0] == id:
            return std
    else:
        return []

while True:
    print("1.add student\n2.view all students\n3.search by id\n4.exit")

    choice = int(input("Enter your selection: "))
    if choice == 1:
        add_students()
    elif choice == 2:
        std_data = view_all_students()
        print(std_data)
    elif choice == 3:
        std = search_id(input("Enter your id: "))
        if len(std) == 0:
            print("Wrong Id!!")
        else:
            print(std)
    elif choice == 4:
        break 
    
"""