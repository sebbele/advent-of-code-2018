#!/usr/bin/env python

with open('7_input.txt', 'r') as f:
    input=f.read().split('\n')[:-1]

#input = ['Step C must be finished before step A can begin.', 'Step C must be finished before step F can begin.', 'Step A must be finished before step B can begin.', 'Step A must be finished before step D can begin.', 'Step B must be finished before step E can begin.', 'Step D must be finished before step E can begin.', 'Step F must be finished before step E can begin.'] 

def mapOrder(input):
    comp_map = {}
    for line in input:
        required_step = line.split(' ')[1]
        step = line.split(' ')[7]
        if step in comp_map:
            comp_map[step].append(required_step)
        else:
            comp_map[step] = [required_step]
        comp_map[step].sort()
    return comp_map

def findAllLetters(comp_map):
    letters = []
    for key in comp_map:
        if key not in letters:
            letters.append(key)
        for letter in comp_map[key]:
            if letter not in letters:
                letters.append(letter)
    return letters

def canBegin(letter, comp_map, ins_order):
    try:
        for val in comp_map[letter]:
            if not val in ins_order:
                return False
        return True
    except KeyError:
        return True

def assembleInstructions(comp_map, letters):
    instruction_order = []
    letters.sort()
    # find letters that can be started after already completed letters are finished
    while len(letters) != 0:
        for letter in letters:
            if canBegin(letter, comp_map, instruction_order):
                instruction_order.append(letter)
                letters.remove(letter)
                break
    return instruction_order


def findOrder(input):
    completion_map = mapOrder(input)
    all_letters = findAllLetters(completion_map)
    step_order = assembleInstructions(completion_map, all_letters)
    return step_order


if __name__ == '__main__':
    result = findOrder(input)
    print(''.join(result))
