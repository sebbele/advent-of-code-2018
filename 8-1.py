#!/usr/bin/env python

# copied from https://www.reddit.com/r/adventofcode/comments/a47ubw/2018_day_8_solutions/ebc7ol0/

def parse(data):
    children, metas = data[:2]
    data = data[2:]
    totals = 0
    for i in range(children):
        total, data = parse(data)
        print(total, data)
        totals += total
    totals += sum(data[:metas])
    return (totals, data[metas:])

input = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

parse(input)
