#!/usr/bin/env python

freq = 0
results = [ 0 ]

change = []
with open('1-1_input.txt') as f:
    for line in f:
        change.append(int(line))

change_length = len(change) - 1
change_current = 0

def incr(freq, results, diff):
    freq += int(diff)
    if freq in results:
        results.append(freq)
        print(results)
        print(freq)
        exit()
    results.append(freq)
    return freq

while True:
    freq = incr(freq, results, change[change_current])
    if change_current == change_length:
        change_current = 0
    else:
        change_current += 1
