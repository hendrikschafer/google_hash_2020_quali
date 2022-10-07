from parser import parse_file
from validator import validate

import random

file = parse_file('a_example.txt')


def random_solution(file):
    libraries = file['libraries']
    solution = {}
    # shuffle libraries
    random.shuffle(libraries)
    for library in libraries:
        solution[library.get_id()] = library.get_sorted_books(file['book_scores'])
    return solution



solution = random_solution(file)

print(file['book_scores'])
print(solution)
print(validate(file, solution))