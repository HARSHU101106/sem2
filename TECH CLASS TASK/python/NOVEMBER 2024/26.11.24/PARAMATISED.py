#paramatised.
class Book:
   def __init__(self,bookname,author):
       self.bookname=bookname
       self.author=author

   def show(self):
       print('Book name :',self.bookname,"Author name:",self.author)
b=Book('IGNITED MINDS','Dr.APJ.ABDUL KALAM')
b.show()






