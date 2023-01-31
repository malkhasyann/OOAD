import tqdm
import time

class Student:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone
        self._books = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if len(value) != 9 or \
                value[0] != '0' or \
                (not value.isdigit()):
            raise ValueError('Invalid phone number')
        self._phone = value

    def show_books(self):
        print(f"------- {self.name}'s books -------")
        for book in self._books:
            print(book)
        print(f"-----------------------------------")

    def borrow_book(self, book):
        self._books.append(book)

    def return_book(self, book):
        self._books.remove(book)
        return book

    def read_book(self, book):
        print(f'{self.name} is reading {book.title}')
        for _ in tqdm.tqdm(range(book.pages)):
            time.sleep(0.02)

    def __str__(self):
        return f'Student: {self.name}, {self.phone}'
