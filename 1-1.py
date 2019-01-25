#!/usr/bin/env python

sum = 0

with open('1-1_input.txt') as f:
    for line in f:
        sum += int(line)

print(sum)
