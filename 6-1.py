#!/usr/bin/env python

from pprint import pprint

input = []
with open('6_input.txt') as f:
    for line in f:
        input.append(line.replace('\n', ''))

#input = [   '1, 1',
#            '1, 6',
#            '8, 3',
#            '3, 4',
#            '5, 5',
#            '8, 9' ]

def inputToDict(input):
    input_dict = {}
    for i in range(len(input)):
        y = input[i].replace(',', '').split()[1]
        x = input[i].replace(',', '').split()[0]
        input_dict[i] = [int(y),int(x)]
    return input_dict


def generateGrid(input):
    grid = []
    y_values = []
    x_values = []
    for coords in input.values():
        y_values.append(int(coords[0]))
        x_values.append(int(coords[1]))
    max_y = int(max(y_values)) + 2
    max_x = int(max(x_values)) + 2
    for y in range(max_y):
        grid.append(['.'] * max_x)
    return grid

def initialPopulate(grid, input_dict):
    for key in input_dict:
        y = int(input_dict[key][0])
        x = int(input_dict[key][1])
        grid[y][x] = key
    return grid

def propagateGrid(grid, input_dict):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            coords = [y, x]
            if grid[y][x] != '.':
                continue
            else:
                grid[y][x] = getManhattan(grid, coords, input_dict)
                continue
    return grid

def getManhattan(grid, coords, candidates):
    choices = {}
    for candidate in candidates:
        manhattan_distance = abs(candidates[candidate][1] - coords[1]) + abs(candidates[candidate][0] - coords[0])
        choices[candidate] = manhattan_distance
    res = minimums(choices)
    if len(res) == 1:
        return res[0]
    else:
        return '.'


def minimums(some_dict):
    positions = [] # output variable
    min_value = float("inf")
    for k, v in some_dict.items():
        if v == min_value:
            positions.append(k)
        if v < min_value:
            min_value = v
            positions = [] # output variable
            positions.append(k)
    return positions

def populateGrid(grid, input_dict):
    grid = initialPopulate(grid, input_dict)
    grid = propagateGrid(grid, input_dict)
    return grid

def calcArea(grid, input_dict):
    # remove candidates with infinite area
    # top
    infinite_ids = [x for x in grid[0] if x != '.']
    # bottom
    infinite_ids = infinite_ids + [x for x in grid[-1] if x != '.']
    #left
    infinite_ids = infinite_ids + [grid[i][0] for i in range(len(grid)) if grid[i][0] != '.']
    # right
    infinite_ids = infinite_ids + [grid[i][-1] for i in range(len(grid)) if grid[i][-1] != '.']
    count = []
    for key in input_dict:
        count.append(0)
        if key in infinite_ids:
            continue
        else:
            for y in grid:
                count[key] = count[key] + y.count(key)
    res = [ count.index(max(count)), max(count) ]
    return res

if __name__ == '__main__':
    input_dict = inputToDict(input)
    grid = generateGrid(input_dict)
    grid = populateGrid(grid, input_dict)
    res = calcArea(grid, input_dict)
    print(res[1])
    #pprint(grid)
