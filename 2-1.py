#!/usr/bin/env python

from collections import Counter

input = []
with open('2-1_input.txt') as f:
    for line in f:
        input.append(line)

two_count = 0
three_count = 0

def countLetters(word, two_count, three_count):
    two = False
    three = False
    letter_dict = Counter(word)
    for letter, count in letter_dict.items():
        if count == 2:
            two = True
        if count == 3:
            three = True
    if two:
        two_count += 1
    if three:
        three_count += 1
    return two_count, three_count

for word in input:
    two_count, three_count = countLetters(word, two_count, three_count)

checksum = two_count * three_count
print(checksum)
