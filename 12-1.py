#!/usr/bin/env python

# part 2: every iteration adds 80 to the total. 80*50000000000 = 4000000000000

import re
import timeit

input = '''initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #'''

def parseInput(input):
    initial_state =  re.findall(r'initial state: (.*)', input)[0]
    state = {  }
    for index in range(len(initial_state)):
        state[index] = initial_state[index]

    rules_list = re.findall(r'^[.#]+.*$', input, re.MULTILINE)
    rule_re = re.compile(r'([.#]{5}) => ([.#])')
    rules = { '#' : [], '.' : [] }
    for rule in rules_list:
          match = rule_re.match(rule)
          res = match[2]
          patt = match[1]
          rules[res].append(patt)
    return state, rules

def progressGeneration(state, rules):
    new_state = {}
    state[min(state.keys()) - 1] = '.'
    state[min(state.keys()) - 1] = '.'
    state[max(state.keys()) + 1] = '.'
    state[max(state.keys()) + 1] = '.'
    for key in state.keys():
        plant_conf = ''
        try:
            plant_conf += state[key - 2]
        except KeyError:
            plant_conf += '.'
        try:
            plant_conf += state[key - 1]
        except KeyError:
            plant_conf += '.'
        plant_conf += state[key]
        try:
            plant_conf += state[key + 1]
        except KeyError:
            plant_conf += '.'
        try:
            plant_conf += state[key + 2]
        except KeyError:
            plant_conf += '.'
        if plant_conf in rules['#']:
            new_state[key] = '#'
        elif plant_conf in rules['.']:
            new_state[key] = '.'
        else:
#            new_state[key] = state[key]
            new_state[key] = '.'
    new_state = stripExtras(new_state)
    return new_state

def stripExtras(state):
    sorted_order = [ i for i in sorted(state) ]
    start_finished = False
    end_finished = False
    while not start_finished and not end_finished:
        if state[sorted_order[0]] == '.' and state[sorted_order[1]] == '.':
            state.pop(sorted_order[0])
            state.pop(sorted_order[1])
            sorted_order.pop(0)
            sorted_order.pop(0)
        else:
            start_finished = True
        if state[sorted_order[-1]] == '.' and state[sorted_order[-2]] == '.':
            state.pop(sorted_order[-1])
            state.pop(sorted_order[-2])
            sorted_order.pop(-1)
            sorted_order.pop(-1)
        else:
            end_finished = True
    return state

def printState(state):
    row_1 = [state[i] for i in sorted(state)]
    row_2 = [i for i in sorted(state)]
    print(' '.join(str(i) for i in row_1))
    print(' '.join(str(i) for i in row_2))

def calcRes(state):
    sum = 0
    for i in state.keys():
        if state[i] == '#':
            sum += i
    return sum

def main():
    with open('12_input.txt', 'r') as f:
        input = f.read()
    #initial_state, rules = parseInput(input)
    state, rules = parseInput(input)
#    gen = 0
    global gen
    for i in range(20):
        gen += 1
        state = progressGeneration(state, rules)
    res = calcRes(state)
    print(res)

if __name__ == '__main__':
    gen = 0
    try:
        main()
    except KeyboardInterrupt:
        print("gen:",gen)
