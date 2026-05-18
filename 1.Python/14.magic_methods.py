# Magic Methods : These methods are used without directly calling the method name.

""" 
class calculate:

    # most common magic method which is invoked by the classname with parenthesis or at the time of object initialization
    def __init__(self,numbers: list):
        self.numbers = numbers

    # different common magic methods
    def __len__(self):
        return len(self.numbers)
    def __str__(self):
        return ",".join([str(x) for x in self.numbers]) 
    def __repr__(self):
        return "this shows this mesaage when object is called directly without print"
    def __add__(self, other):
        new_list = self.numbers.copy()
        new_list.extend(other.numbers)
        return new_list
    def __sub__(self, other):
        list1, list2 = self.numbers, other.numbers
        new_set = set(list1).union(set(list2)) - set(list1).intersection(set(list2))
        return list(new_set)
        # newlist = []
        # for x,y in zip(self.numbers,other.numbers):
        #     if x not in other.numbers:
        #         newlist.append(x)
        #     if y not in self.numbers:
        #         newlist.append(y)
        # return newlist
    def __mul__(self, other):
        return None
    def __divmod__(self, other):
       pass 
    def __mod__(self, other):
        pass
    def __iadd__(self, other):
        self.numbers.extend(other.numbers)
        self.numbers = list(set(self.numbers))
        return self
    def __isub__(self, other):
        pass

            
# cal = calculate(3,6) 
# cal1 = calculate.__init__(3,7)
cal = calculate([3,6])
# print(calculate.__len__(cal))
cal2 = calculate([5,3])
print(cal + cal2)
print(cal)
print(cal - cal2) 

"""

# 1) Smart Shopping Cart (Operator Overloading)
# - A shopping cart should behave like a real object.
# - You must allow adding items with +, removing using -, and printing in a readable way.
#     - Requirements
#         - Class Cart holds items (name, price, qty)
#         - cart + item → adds item
#         - cart - item → removes item (if exists)
#         - str(cart) shows total items & bill

class cart:
    def __init__(self):
        self.items = []
        self.total_bill = 0
    
    def __iadd__(self, other):
        self.items.append(other)
        self.total_bill += other["price"] * other["qty"]
        return self
    
    def __isub__(self, other):
        # subtract by the whole dictionary
        """ 
        if other in self.items:
            self.items.pop(self.items.index(other))
            self.items.remove(other)
        self.total_bill -= other["price"]*other["qty"] 
        """
        # subtracting by the index no
        """ 
        if other-1 < len(self.items) and other-1 > -1:
            self.total_bill -= self.items[other-1]["price"]*self.items[other-1]["qty"]
            self.items.pop(other-1)
        return self 
        """
        # subtracting by the name and qty
        for dict in self.items:
            if dict["name"] == other[0]:
                if other[1] <= dict["qty"]:
                    dict["qty"] -= other[1]
                    self.total_bill -= dict["price"]*other[1]
                    if dict["qty"] == 0:
                        self.items.remove(dict)
                    break
                else:
                    print("given qty is more than available qty in the cart")
        return self


    def __str__(self):
        str = ""
        for index,dict in enumerate(self.items):
            print()
            str += f"item : {index+1}\n"
            for k,v in dict.items():
                str += f"{k} : {v}\n"
            str += f"\nsub total : {dict["price"]*dict["qty"]}"
            str += "\n" + ("*"*20 )+ "\n"
        str += f"total items : {len(self.items)}\n"
        str += f"total bill : {self.total_bill}"
        return str
        

mycart = cart()
mycart += {"name":"pen","price":100,"qty":2}
mycart += {"name":"remover","price":200,"qty":1}
# mycart -= {"name":"pen","price":100,"qty":2}
# print(mycart)
# mycart -= 2
print(mycart)
mycart -= ("pen",1)
print(mycart)
mycart -= ("pen",1)
# print(mycart)




