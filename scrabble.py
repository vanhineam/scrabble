#!/bin/python

import argparse
import copy

# Get the input from the commandline
parser = argparse.ArgumentParser(description="Scrabble")
parser.add_argument('input')
args = parser.parse_args()
userIn = args.input.upper()

# Scrabble letter scores
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

# Get the valid words and store in list
f = open('sowpods.txt', 'r')
words = []
for line in f:
    words.append(line.strip())

valid_words = []

letters = []
for i in userIn:
    letters.append(i)

for current_word in words:
    valid = True
    copy_letters = copy.deepcopy(letters)
    for current_letter in current_word:
        if current_letter in copy_letters:
            copy_letters.remove(current_letter)
        else:
            valid = False
            break
    if valid:
        valid_words.append(current_word.lower())


for word in reversed(valid_words):
    score = 0
    for letter in word:
        score += scores[letter]
    print score, word
