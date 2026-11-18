class Book:
    """Represent a book with its title, author, and price."""

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price

    # Encapsulation: Provide controlled access to the private price
    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Error: Price must be greater than zero.")

    def display_info(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Price : ${self.__price:.2f}")

class EBook(Book):
    """Represent an electronic book that inherits from Book."""

    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    # Extend the parent's display method
    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size} MB")


book1 = Book("Python Programming", "John Smith", 25.00)
ebook1 = EBook("Data Science Fundamentals", "David Lee", 15.00, 5)

print("=== Printed Book ===")
book1.display_info()

print("\n=== Electronic Book ===")
ebook1.display_info()

ebook1.set_price(20.00)

print("\n=== Updated EBook Price ===")
print(f"New Price: ${ebook1.get_price():.2f}")
