# Write a Python program to select a random element from a list, set, dictionary (value) and
# a file from a directory. Use random.choice()
import random

list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

n = 5

for i in range(n):

    print(random.choice(list), end='')
