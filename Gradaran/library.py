class Library:
    def __init__(self):
        self._books = {}  # book:count

    def add_book(self, book):
        if book not in self._books:
            self._books[book] = 1
        else:
            self._books[book] += 1

    def give_book(self, book):
        if book not in self._books:
            raise ValueError('This book doesnt belong to the Library')
        self._books[book] -= 1
        return book

    def __str__(self):
        message = '------ LIBRARY -------\n'
        message += '\n'.join([str(book) + f' || Count: {count}\n' for book, count in self._books.items()])
        message += '----------------------'
        return message
