# Encapsulation (Kapsülleme)
# Bir sınıfa ait değişkenlerin veya niteliklerin ancak o sınıfa ait metotlar tarafından değiştirilebilmesi ve okunabilmesi ilkesidir.
# Bu ilke sayesinde nesnelerde oluşacak anlamsızlıkların önüne geçilebilir.


class Book:
    
    # instance attributes
    def __init__(self, author, book_name, total_page):
        self.__author = author
        self.__book_name = book_name
        
        if(total_page < 0):
            self.__total_page = 10
        
        else:
            self.__total_page = total_page
        
    
        
    # instance method
    # Getter and Setter
    def getauthor(self):
        return self.__author
        
    def setauthor(self, author):
        self.__author == author
        
    def getbook_name(self):
        return self.__book_name
        
    def setbook_name(self, book_name):
        self.__book_name = book_name
    
    def gettotal_page(self):
        return self.__total_page
        
    def settotal_page(self, total_page):
        if(total_page < 0):
            self.__total_page = 10
        
        else:
            self.__total_page = total_page
        
        

book1 = Book("George Orwell", "1984", 302)
book2= Book("George Orwell", "Animal Farm", 102)


print(book1.__dict__)
print(book2.__dict__)

print(book1.getauthor())
print(book1.getbook_name())
print(book1.gettotal_page())

print(book2.getauthor())
print(book2.getbook_name())
print(book2.gettotal_page())
