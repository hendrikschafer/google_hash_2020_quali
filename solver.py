from parser import parse_file, files
from validator import validate

import random
from tqdm import trange

def random_solution(file):
    libraries = file['libraries']
    solution = {}
    # shuffle libraries
    random.shuffle(libraries)
    for library in libraries:
        solution[library.get_id()] = library.get_sorted_books(file['book_scores'])
    return solution

def best_of_n_random_solutions(file, n):
    max_score = 0
    best_solution = None
    for i in trange(n):
        solution = random_solution(file)
        score = validate(file, solution)
        if score > max_score:
            max_score = score
            best_solution = solution
    print(f'max_score: {max_score}')

if __name__ == '__main__':
    file = parse_file(files.c)

    best_of_n_random_solutions(file, 1000)