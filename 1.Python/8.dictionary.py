# Dictionary: A collection of key and value pairs.
#  syntax:
#          mydict = {"key1":"value","key2":"value"}
# functions:
#     1. keys()
#     2. values()
#     3. items()

mydict = {"name":"Yasir",
          "fname":"Nawaz",
          "phone":"03003000000",
          "pass":True,
          "marks":890}
mydict['add'] = "hvdjcgascydgvcjwvjwhdm"

# print(mydict)

# sortedkeys = list(mydict.items())
# print(sortedkeys)
# sortedkeys.sort()
# print(sortedkeys)

# for k,v in mydict.items():
#     print(f"{k} : {v}")

""" 
data = [{"name":"Yasir",
          "fname":"Nawaz",
          "phone":"03003000000",
          "pass":True,
         'email':"yasir123@gmail.com",
         'password':'abc123',
          "marks":890},
        {"name":"Ahmed",
          "fname":"Faraz",
          "phone":"03003000000",
          "pass":True,
         'email':"ahmed123@gmail.com",
         'password':'abc123',
          "marks":890},
        {"name":"Ali",
          "fname":"Parvez",
          "phone":"03003000000",
          "pass":True,
         'email':"ali123@gmail.com",
         'password':'abc123',
          "marks":890}]

useremail = input("Enter your email:")
userpass = input("Enter your pass:")

for user in data:
    if useremail == user['email'] and userpass == user['password']:
        print('*'*10)
        for k,v in user.items():
            print(f"{k} : {v}")
        break
else:
    print("user not found!!") 
    
"""

""" 
data = {"u1":{"name":"Yasir",
             "fname":"Nawaz",
             "phone":"03003000000",
             "pass":True,
             'email':"yasir123@gmail.com",
             'password':'abc123',
              "marks":890},
        "u2":{"name":"Ahmed",
            "fname":"Faraz",
            "phone":"03003000000",
            "pass":True,
            'email':"ahmed123@gmail.com",
            'password':'abc123',
            "marks":890},
        "u3":{"name":"Ali",
            "fname":"Parvez",
            "phone":"03003000000",
            "pass":True,
           'email':"ali123@gmail.com",
           'password':'abc123',
           "marks":890}}

#print(data['u2']['name'])

useremail = input("Enter your email:")
userpass = input("Enter your pass:")

for userid, uservalue in data.items():
    if useremail == uservalue['email'] and userpass == uservalue['password']:
        print('*'*10)
        for k,v in uservalue.items():
            print(f"{k} : {v}")
        break
else:
    print("user not found!!") 
    
"""

data = [{"name":"Yasir",
          "fname":"Nawaz",
          "phone":"03003000000",
          "pass":True,
         'email':"yasir123@gmail.com",
         'password':'abc123',
          "marks":890},
        {"name":"Ahmed",
          "fname":"Faraz",
          "phone":"03003000000",
          "pass":True,
         'email':"ahmed123@gmail.com",
         'password':'abc123',
          "marks":890},
        {"name":"Ali",
          "fname":"Parvez",
          "phone":"03003000000",
          "pass":True,
         'email':"ali123@gmail.com",
         'password':'abc123',
          "marks":890}]

listnames = [(std['name'],std['email']) for std in data]
print(listnames)

#mylist = [x for x in range(1,101)]
#print(mylist)