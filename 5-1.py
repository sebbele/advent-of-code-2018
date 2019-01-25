#!/usr/bin/env python

input = []
with open('5_input.txt') as f:
    for line in f:
        input.append(line)

#input = [ 'dabAcCaCBAcCcaDA' ]

def makeReaction(input):
    finished = False
    while not finished:
        for pos in range(len(input) - 1):
            print('currently working on pos {0} / {1}. input: {2}'.format(pos, len(input), len(input)))
            curr_letter = input[pos]
            try:
                next_letter = input[pos + 1]
            except IndexError:
                finished = True
            if polyReact(curr_letter, next_letter):
                new_input = input[:pos] + input[pos + 2:]
                input = new_input
                break
            if pos + 2 == len(input):
                finished = True
                break
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
    input = input[0]
    result = makeReaction(input)
    print(len(result))
