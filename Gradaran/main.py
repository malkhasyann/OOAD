from student import Student
from book import Book
from library import Library
import copy


good_book = Book('Extreme C', 'Kamran Amini', 823)
another_good_book = Book('Aybenaran', 'Mesrop Mashtots', 50)

student = Student('Leo', '077666999')

lib = Library()
lib.add_book(good_book)
lib.add_book(another_good_book)
lib.add_book(copy.copy(another_good_book))

print(lib)

student.borrow_book(lib.give_book(another_good_book))
student.read_book(another_good_book)

print(student)
student.show_books()

print(lib)

lib.add_book(student.return_book(another_good_book))

print(lib)
