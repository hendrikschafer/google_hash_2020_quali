class files:
    a = 'txts/a_example.txt'
    b = 'txts/b_read_on.txt'
    c = 'txts/c_incunabula.txt'
    d = 'txts/d_tough_choices.txt'
    e = 'txts/e_so_many_books.txt'
    f = 'txts/f_libraries_of_the_world.txt'

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
        total_book_count, library_count, days = [int(x) for x in lines[0].split()]
        book_scores = [int(x) for x in lines[1].split()]
        libraries = []
        for i in range(library_count):
            book_count, signup_days, books_per_day = [int(x) for x in lines[2*i+2].split()]
            books = [int(x) for x in lines[2*i+3].split()]
            library = Library(i, book_count, signup_days, books_per_day)
            library.add_books(books)
            libraries.append(library)

        file = {'total_book_count': total_book_count,
                'library_count': library_count,
                'days': days,
                'book_scores': book_scores,
                'libraries': libraries}

        print_file(file)

        return file


def print_file(file):
    print(f"""
total_book_count: {file['total_book_count']}
library_count: {file['library_count']}
days: {file['days']}
max_book_score: {max(file['book_scores'])}
min_book_score: {min(file['book_scores'])}""")

def print_libraries(file):
    for library in file['libraries']:
        print(f"""
library id: {library.get_id()}
book_count: {library.get_book_count()}
signup_days: {library.get_signup_days()}
books_per_day: {library.get_books_per_day()}""")


if __name__ == '__main__':
    file = parse_file(files.b)
    print_libraries(file)
    