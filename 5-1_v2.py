#!/usr/bin/env python

from string import ascii_uppercase
import re

input = []
with open('5_input.txt') as f:
    for line in f:
        input.append(line)

#input = [ 'dabAcCaCBAcCcaDA' ]

def makeReaction(input):
    alphabet = ascii_uppercase
    finished = False
    while not finished:
        for letter_upper in alphabet:
            letter_lower = letter_upper.lower()
            if letter_lower + letter_upper in input:
                input = re.sub(letter_lower + letter_upper, '', input)
                break
            elif letter_upper + letter_lower in input:
                input = re.sub(letter_upper + letter_lower, '', input)
                break
            elif letter_upper == 'Z':
                finished = True
    return input


def polyReact(a, b):
    if a.islower():
        if a.upper() == b:
            return True
    elif a.isupper():
        if a.lower() == b:
            return True
    return False

if __name__ == '__main__':
    input = input[0].splitlines()[0]
    result = makeReaction(input)
