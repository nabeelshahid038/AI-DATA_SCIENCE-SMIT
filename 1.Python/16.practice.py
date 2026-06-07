# create a library management system
# create a book class and a derived class ebook with methods for borrowing and returning books
# use a decorator to log all activities and save them in a file named as logs.txt 
# implement magic methods like __str__(),__len__(),__add__() for display and manage book data
# store all borrowing and returning records in book_record.txt
import datetime as dt

def track_action(func):
    def wrapper(self):
        print("track action decorator started")
        with open("16.library_logs.txt","a") as file:
            file.write(f"{dt.datetime.now()} - {func.__name__} has called\n")
        func(self)
        print("track action decorator ended")
    return wrapper

class Book:

    def __init__(self,t,a_n,p,p_y,isbn):
        self.title = t
        self.author_name = a_n
        self.pages = p
        self.pub_year = p_y
        self.isbn = isbn
    
    @track_action
    def borrow_book(self):
        name = input("enter your name :")
        id = input("enter your id : ")
        with open("16.books_record.txt","a") as file:
            file.write(f"book borrowed by {name} ({id}) - {dt.datetime.now()}\n")
        print("you have successfully borrowed the book")

    @track_action
    def return_book(self):
        name = input("enter your name :")
        id = input("enter your id : ")
        with open("16.books_record.txt","a") as file:
            file.write(f"book returned by {name} ({id}) - {dt.datetime.now()}\n")
        print("you have successfully returned the book")


    def __str__(self):
        str = ""
        str += f"title : {self.title}\nauthor name : {self.author_name}\nno. of pages : {self.pages}\npublished_year : {self.pub_year}\nisbn : {self.isbn}"
        return str
    
    def __len__(self):
        return self.pages
    def __add__(self, other):
        return len(self) + len(other)

class EBook(Book):

    def __init__(self,t,a_n,p,p_y,isbn,format,size):
        super().__init__(t,a_n,p,p_y,isbn)
        self.format = format
        self.size = size


    def __str__(self):
        return super().__str__() + f"\nformat : {self.format}\nsize : {self.size}"
    
    




book1 = Book("Java Basics","JAMES",205,1999,"BOOK1001")
book2 = Book("Python Basics","ANDREW",290,2003,"BOOK1002")
ebook1 = EBook("Python Advance","LIAM",420,2001,"BOOK1003","pdf","20mb")
ebook2 = EBook("Java Advance","YOUNG",510,2000,"BOOK1004","docx","50mb")

book1.borrow_book()
book2.borrow_book()
ebook1.borrow_book()
book2.return_book()






