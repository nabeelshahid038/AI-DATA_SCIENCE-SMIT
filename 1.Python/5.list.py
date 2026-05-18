'''
List: A collection of hetrogenius data type elements.
    Syntax:
            MyList = [10,30,'h',True,7.8]

mylist = [10,30,'h',True,7.8]

mylist[2] = 't'

print(mylist[2])
'''

#Task: Create a a list of user details include (Name,FNAme,CNIC,Phone,Add,
# Email and Pass)
#step 2: Email and Pass match using list

""" 
data = ["Yasir","abc@gmail.com",'abc123']
label = ['Name','Email','Pass']
useremail = input("Enter your email: ")
userpass = input("Enter your Pass: ")
if useremail == data[1] and userpass == data[2]:
    # using len function we can count all the elements of a list
    # for i in range(0,len(data)):
    #    print(label[i]+":",data[i])

    # for j, i in zip(label,data):
    #     print(j,i) 
 """
#std1 = ['yasir','D',58,True]
#std1[3] = 'abc'
#print(std1[3])

'''
List Functions:
	append( Element to add)	Adds an element at the end of the list
	clear()			Removes all the elements from the list
	copy()			Returns a copy of the list
	count(Element)		Returns the number of elements with the specified value
	extend()		Add the elements of a list (or any iterable), to the end of the current list
	index(Element)		Returns the index of the first element with the specified value
	insert(Index, Element)	Adds an element at the specified position
	pop()			Removes the element at the last element
	remove(Element)		Removes the item with the specified value
	reverse()		Reverses the order of the list
	sort()			Sorts the list


syntax:
    object.func()
'''



# mylist = [1,22,34,55,67,93,55]
# mylist.append(56)
# mylist.insert(7,2)
# mylist.extend([22,66,78,28,32])
# mylist.pop(0)
# mylist.remove(55)
# # mylist.clear()
# print(mylist.count(55))
# print(len(mylist))
# print(mylist.index(55))
# print(mylist)
# copy = mylist.copy()
# print(copy)
# print("adding new element in nested list of mylist : ",mylist[-1].append(1001))
# print(mylist)
# print(copy)

'''
elements = []
element_to_find = 100
for i in range(len(mylist)):
    if mylist[i] == element_to_find:
        elements.append(i)
print(elements)
'''
# mylist.reverse()
# mylist.sort(reverse = True)
# print(mylist)



