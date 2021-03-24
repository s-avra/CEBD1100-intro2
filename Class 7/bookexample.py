class Book:

    def __init__(self, isbn, title,used):
        self.isbn = isbn
        self.title = title
        self.owner = "westmount library"
        self.used = used
#book has 3 attributes, only 2 are supplied
# self must be first parameter for constructor,
# indicates value belongs to class
    def is_book_used(self):
        return self.used


#instantiations of objects
#init tells us what to excpet when the book is being created

book1 = Book("123456789", "War of the Worlds", False)
book2 = Book("987654321", "Insomnia", True)


print(book2.title)
array_of_books = [book1,book2]
for book in array_of_books:
    print(book.title)
    print("Book used ?", end ="")
    if book.is_book_used():
        print("yes")
    else:
        print("no")

