class Library:
    def __init__(self, id, book_count, signup_days, books_per_day):
        self.id = id
        self.book_count = book_count
        self.signup_days = signup_days
        self.books_per_day = books_per_day
        self.books = []

    def add_books(self, books):
        self.books = books

    def get_books(self):
        return self.books

    def get_id(self):
        return self.id

    def get_book_count(self):
        return self.book_count

    def get_signup_days(self):
        return self.signup_days

    def get_books_per_day(self):
        return self.books_per_day

    def get_sorted_books(self, book_scores):
        return sorted(self.books, key=lambda x: book_scores[x], reverse=True)



def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        total_book_count, library_count, days = list(map(int, lines[0].split()))
        book_scores = [int(x) for x in lines[1].split()]
        libraries = []
        for i in range(library_count):
            book_count, signup_days, books_per_day = list(map(int, lines[2 + i * 2].split()))
            books = list(map(int, lines[3 + i * 2].split()))
            library = Library(i, book_count, signup_days, books_per_day)
            library.add_books(books)
            libraries.append(library)
        return {'total_book_count': total_book_count,
                'library_count': library_count,
                'days': days,
                'book_scores': book_scores,
                'libraries': libraries}

if __name__ == '__main__':
    file = parse_file('txts/a_example.txt')
    print(file)
    # print each library
    for library in file['libraries']:
        print(library.get_id(), library.get_book_count(), library.get_signup_days(), library.get_books_per_day())
        print(library.get_books())