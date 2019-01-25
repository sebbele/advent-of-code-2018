#!/usr/bin/env python
from pprint import pprint

input = []
with open('3_input.txt') as f:
    for line in f:
        input.append(line)

#input = [ '#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2' ]

def cleanSpecialChars(input):
    for i in range(len(input)):
        input[i] = input[i].replace('@ ', '')
        input[i] = input[i].replace('#', '')
        input[i] = input[i].replace(':', '')
    return input

def enterId(id, grid, y, x):
    global res
    global res_list
    global unique_id
    if grid[y][x] == 'X':
        try:
            unique_id.remove(str(id))
        except ValueError:
            pass
        return 'X'
    elif grid[y][x] != '.':
        try:
            unique_id.remove(str(grid[y][x]))
        except ValueError:
            pass
        try:
            unique_id.remove(str(id))
        except ValueError:
            pass
        res_list.append([y, x])
        res += 1
        return 'X'
    else:
        return id

def handleInput(input, grid):
    global unique_id
    input_list = input.split(' ')
    id = input_list[0]
    unique_id.append(str(id))
    start_x = int(input_list[1].split(',')[0])
    start_y = int(input_list[1].split(',')[1])
    len_x = int(input_list[2].split('x')[0])
    len_y = int(input_list[2].split('x')[1])

    curr_x = start_x
    curr_y = start_y

    for y in range(len_y):
        for x in range(len_x):
            grid[curr_y][curr_x] = enterId(id, grid, curr_y, curr_x)
            curr_x += 1
        curr_x = start_x
        curr_y += 1

    return grid

if __name__ == '__main__':
    input = cleanSpecialChars(input)
    res_list = []
    res = 0
    grid = []
    unique_id = []
    for i in range(1000):
        grid.append(['.'] * 1000)
    for i in input:
        grid = handleInput(i, grid)
    #pprint(grid)
    #print(len(res_list))
    #print(res)
    print(unique_id)
