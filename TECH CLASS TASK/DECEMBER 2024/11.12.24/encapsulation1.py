#public:accessible anywhere from outside class
#private:accessible within the class
#protector:accessible wihtin the class and its subclass
'''class Student:
    id=input()
    print(id)
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("NAME:",self.__name)
s=Student("HARSHU")
s.display()'''
class library:
    _librarybooks=["IGNITED MINDS","WINGS OF FIRE","INDIA 2020","5 SECRETS OF LIFE","BHAGAVATGEETA","RAMAYANAM","PONNIYINSELVAN"]
    _count=0
    for i in _librarybooks:
        _count+=1
class customer(library):
    __num=int(input("enter the number of books to be borrowed:"))
    books=[]
    print("the books in the library:",library._librarybooks)
    for i in range(__num):
        books.append(input("enter the name of the book to be borrowed:"))
        if i in library._librarybooks:
            library._librarybooks.remove[i]
    library._count-=__num
    print("the books borrowed:",books)
    print("the books left in  library:",library._librarybooks)
    print("the number of remaining books in library: ",library._count)
obj=customer()

