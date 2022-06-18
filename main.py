# GENERATE 3 X 3 MATRIX (RANDOM LETTERS)

# make this a dict when moving towards creating points per word
import random

matrix_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]

# WORD MUST BE >3 <9

m1 = random.choice(matrix_letters)
m2 = random.choice(matrix_letters)
m3 = random.choice(matrix_letters)
m4 = random.choice(matrix_letters)
m5 = random.choice(matrix_letters)
m6 = random.choice(matrix_letters)
m7 = random.choice(matrix_letters)
m8 = random.choice(matrix_letters)
m9 = random.choice(matrix_letters)

matrix = [
    [m1, m2, m3],
    [m4, m5, m6],
    [m7, m8, m9]
    ]

print(matrix)
