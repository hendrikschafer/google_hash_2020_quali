from parser import parse_file, files

class examples:
    a = {1: [5, 2, 3],
           0: [0, 1, 2, 3, 4]}

# FIXME
def validate(file, submission):
    book_scores = file['book_scores']
    libraries = file['libraries']
    total_score = 0
    sent_books = set()

if __name__ == '__main__':

    file = parse_file(files.a)

    print(validate(file, examples.a))