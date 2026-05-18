# read

""" 
try:
    useremail = input("Enter your Email: ")
    userpass = input("Enter your Password: ")
    file = open("10.data.csv",'r')
    # print(file.read())
    # print(file.readline().strip().split(','))
    for line in file.readlines():
        user = line.strip().split(',')
        if user[3] == useremail and user[4] == userpass:
            print(user)
    file.close()
except FileNotFoundError as e:
    print("Wrong File name!",e) 
    
"""

# append

""" 
name = input("Enter your Name: ")
fname = input("Enter your FName: ")
phone = input("Enter your Phone: ")
email = input("Enter your Email: ")
password = input("Enter your Password: ")
file = open('10.data.csv','a')
data = f"{name},{fname},{phone},{email},{password}\n"
file.write(data)
file.close() 

"""

# write

""" 
file = open("10.data2.txt","w")
listdata = ["ali,ahmed,892374209213,ahmed@gmail.com,ali123\n",
            "zeeshan,ali,09797892789,zeeshan@gmail.com,zeeshan123\n"]
file.writelines(listdata)
file.close() 

"""

# opening the file by using ( with ) keyword 

""" 
data = [['Yasir','Nawaz','abc@gmail.com','abc123'],
        ['Yasir1','Nawaz','abc1@gmail.com','abc123'],
        ['Yasir2','Nawaz','abc2@gmail.com','abc123'],
        ['Yasir3','Nawaz','abc3@gmail.com','abc123']]

with open('10.data3.csv','a') as file:
    for user in data:
        file.write(','.join(user)+'\n') 

"""

# mylist = ['Yasir','nawaz','76783478348673','abc@gmail.com']
# print(','.join(mylist))
# print(mylist)

# Task:
# Create a data.txt file for storing details for atleast 5 users.
# (uid, name, email, phone, cnic)
# create a program for updating user details by user id

""" 
uid = input("Please enter user id to update: ")
data = []
with open("10.data4.csv","r") as file:
    data = [ line.strip().split(',') for line in file.readlines()]

for i in range(0,len(data)):
    if data[i][0] == uid:
        name = input("Enter your Name: ")
        fname = input("Enter your FName: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        data[i][1] = name
        data[i][2] = fname
        data[i][3] = email
        data[i][4] = password

with open("10.data4.csv",'w') as file:
    # print([",".join(user) for user in data])
    strdata = []
    for user in data:
        strdata.append(",".join(user)+"\n")
    file.writelines(strdata) 
    
"""

# r+,w+ and a+ modes

# with open("data.csv","a+") as file:
#     # end = len(file.read())
#     # file.seek(end+1)
#     # file.write("THE END")\
#     file.seek(0)
#     print(file.read())