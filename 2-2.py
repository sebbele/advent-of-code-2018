#!/usr/bin/env python

from collections import Counter

input = []
with open('2-1_input.txt') as f:
    for line in f:
        input.append(line)

def findMatches(num, input):
    candidates = input
    diff_count = 0
    curr_word = input.pop(num)
    cand_diff = [ 0 ] * len(candidates)

    for letter_num in range(len(curr_word)):
        curr_letter = curr_word[letter_num]
        for cand_num in range(len(candidates)):
            if candidates[cand_num][letter_num] != curr_letter:
                cand_diff[cand_num] += 1
            if cand_diff[cand_num] >= 2:
                continue
    if 0 in cand_diff or 1 in cand_diff:
        for i in range(len(cand_diff)):
            if cand_diff[i] == 0 or cand_diff[i] == 1:
                cand_match = candidates[i]
        print("{0} is very similar to {1}".format(curr_word, cand_match))
        res = ''
        for x, y in zip(curr_word, cand_match):
            if x == y:
                res = res + x
        print("This should be the answer: {0}".format(res))
        exit()

    input.insert(num, curr_word)
        
#input = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

if __name__ == "__main__":
    for num in range(len(input)):
        findMatches(num, input)
