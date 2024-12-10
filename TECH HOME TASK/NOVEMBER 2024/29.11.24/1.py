'''1. Scenario: Library Management System
Creating a simple library management system where:
• Library handles book details.
• Member handles member details.
• LibraryManagement combines the features of both Library and Member
and allows borrowing books.'''
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, copies):
        if title not in self.books:
            self.books[title] = {'author': author, 'copies': copies}
        else:
            self.books[title]['copies'] += copies

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for title, details in self.books.items():
                print(f"Title: {title}, Author: {details['author']}, Copies Available: {details['copies']}")
        else:
            print("No books available in the library.")

    def check_availability(self, title):
        return self.books.get(title, {}).get('copies', 0)


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"- {book}")
        else:
            print(f"{self.name} has no borrowed books.")


class LibraryManagement:
    def __init__(self, library):
        self.library = library
        self.members = {}

    def add_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, member_id, book_title):
        if member_id not in self.members:
            print(f"No member found with ID: {member_id}")
            return

        member = self.members[member_id]
        if self.library.check_availability(book_title) > 0:
            member.borrow_book(book_title)
            self.library.books[book_title]['copies'] -= 1
            print(f"{member.name} has borrowed '{book_title}'.")
        else:
            print(f"Sorry, '{book_title}' is not available in the library.")

    def return_book(self, member_id, book_title):
        if member_id not in self.members:
            print(f"No member found with ID: {member_id}")
            return

        member = self.members[member_id]
        if book_title in member.borrowed_books:
            member.return_book(book_title)
            self.library.books[book_title]['copies'] += 1
            print(f"{member.name} has returned '{book_title}'.")
        else:
            print(f"{member.name} has not borrowed '{book_title}'.")

    def display_all_books(self):
        self.library.display_books()

    def display_member_books(self, member_id):
        if member_id not in self.members:
            print(f"No member found with ID: {member_id}")
            return
        self.members[member_id].display_borrowed_books()

library = Library()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 5)
library.add_book("1984", "George Orwell", 3)

member1 = Member(1, "Krish")
member2 = Member(2, "Harshu")

library_management = LibraryManagement(library)
library_management.add_member(member1)
library_management.add_member(member2)

library_management.display_all_books()
library_management.borrow_book(1, "The Great Gatsby")
library_management.display_member_books(1)
library_management.display_all_books()

library_management.return_book(1, "The Great Gatsby")
library_management.display_member_books(1)
library_management.display_all_books()
