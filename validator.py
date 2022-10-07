from parser import parse_file

def validate(file, submission):
    days = file['days']
    book_scores = file['book_scores']
    libraries = file['libraries']
    total_score = 0
    sent_books = set()
    for library_id, books in submission.items():
        library = libraries[library_id]
        signup_days = library.get_signup_days()
        books_per_day = library.get_books_per_day()
        days -= signup_days
        if days < 0:
            return 0
        total_books = days * books_per_day
        # append to sent_books
        sent_books.update(books[:total_books])

    for book in sent_books:
        total_score += book_scores[book]
    return total_score

if __name__ == '__main__':

    example = {1: [5, 2, 3],
           0: [0, 1, 2, 3, 4]}

    file = parse_file('txts/a_example.txt')

    print(validate(file, example))