# -------------------------------------------------------
#                      OS MODULE 
# -------------------------------------------------------

""" 
import os
print(os.environ["USERNAME"])
print(os.environ["HOME"])

cwd = os.getcwd()
os.chdir('data/')
with open('smit.txt','r') as file:
    pass
print(os.getcwd())

for file in os.listdir('.'):
    if file.endswith('.csv'):
        print(file)

os.system('mkdir test')

print(os.listdir('.'))

for path,dir,files in os.walk(cwd):
    print(f"path: {path}")
    print(f"Folders: {dir}")
    print(f"Files: {files}")
    print('*'*20) 
    
"""

# -------------------------------------------------------
#                      Math MODULE 
# -------------------------------------------------------

import math

# print(2**3)
# print(math.pow(2,5))
# print(math.sqrt(30))
# print(math.isqrt(30))
# print(math.cbrt(125))
# print(math.factorial(5))
# print(math.pi)
# print(math.nan)
# print(math.prod([2,10,5,-3,20]))
# print(math.sin(90))
# print(math.log10(2.34))
# print(math.floor(3.67))
# print(math.ceil(3.67))

# Create a function for area of a circle (A = πr2)
""" 
def area_of_circle(r):
    return math.pi * math.pow(r,2)

print(area_of_circle(4)) 

"""

#create a function for if the number is a perfect sqrt or not (True, False) 

""" 
def is_perfect_sqrt(num: int):
    return math.sqrt(num) == math.isqrt(num)

print(is_perfect_sqrt(30)) 

"""

# create a function to find distance between two points.

""" 
def distance(p1: tuple,p2: tuple):
    return math.sqrt(math.pow(p2[0]-p1[0],2)+math.pow(p2[1]-p1[1],2))

print(distance((3,4),(5,7)))

print(math.dist((3,4),(5,7))) 

"""
# -------------------------------------------------------
#                     Collection MODULE 
# -------------------------------------------------------

""" 
import collections as col
import queue


myqueue = col.deque([3,6])

myqueue.appendleft(0)
myqueue.appendleft(4)
myqueue.appendleft(8)
myqueue.appendleft(0)

print(myqueue)


mycounterlist = col.Counter(["hen","bread","chiken","hen"])

print(mycounterlist['hen'])

mycounterlist2 = col.Counter({"cat":2,"dogs":4})

print(mycounterlist2["eggs"])

mycounterlist3 = col.Counter("allopmnnyy")

print(mycounterlist3['y']) """

# mycounterlist4 = col.Counter([["a","c","f"],["c","g","f"],["e","t","y"]])




""" 
mystack = queue.LifoQueue(maxsize=5)
mystack.put(4)
mystack.put(7)
mystack.put(9)
mystack.put(0)
mystack.put(10)

print(mystack.full())
print(mystack.get())
print(mystack.full()) 

"""