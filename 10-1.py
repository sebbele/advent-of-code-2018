#!/usr/bin/env python

import re
from time import sleep
import matplotlib.pyplot as plt


INPUT = []
with open('10_input.txt') as f:
#with open('10_input_example.txt') as f:
    for line in f:
        INPUT.append(line[:-1])

def inputToList(input):
    input_list = []
    regex = re.compile(r'position=<([^,]+),([^>]+)> velocity=<([^,]+),([^>]+)>')
    for entry in input:
        match = regex.findall(entry)[0]
        pos_x, pos_y, vel_x, vel_y = [int(i) for i in match]
        input_list.append([pos_x, pos_y, vel_x, vel_y])
    return input_list

def generateGrid(data):
    min_x = min([i[0] for i in data])
    max_x = max([i[0] for i in data])
    max_y = max([i[1] for i in data])
    min_y = min([i[1] for i in data])
    len_x = abs(min_x - max_x)
    len_y = abs(min_y - max_y)

    # generate empty grid
    grid = []
    for y in range(len_y + 1):
        grid.append(['.'] * (len_x + 1))
    # populate grid
    # offset = pos - min
    for pos in data:
        pos_y = abs(pos[1] - min_y)
        pos_x = abs(pos[0] - min_x)
        grid[pos_y][pos_x] = '#'
    return grid

def tick(data, time, speed=1):
    for id in range(len(data)):
        data[id][0] += data[id][2] * speed
        data[id][1] += data[id][3] * speed
    time = time + speed
    return data, time

def graph(data):
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    foo = plt.plot(x, y, 'o')
    plt.clf()
# 10681
if __name__ == '__main__':
    data = inputToList(INPUT)
    sec = 0
    data, sec = tick(data, sec, 10681)
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(111)
    li, = ax.plot(x, y, 's')
#    fig.canvas.draw()
    #plt.show(block=False)

#    li.set_xdata(x)
#    li.set_ydata(y)
#    ax.relim()
#    ax.autoscale_view(True,True,True)
    fig.canvas.draw()

    li.set_xdata(x)
    li.set_ydata(y)
    ax.relim()
    ax.autoscale_view(True,True,True)
    fig.canvas.draw()
    plt.show()
    sleep(600000)
#    while True:
#        x = [i[0] for i in data]
#        y = [i[1] for i in data]
#        #plt.plot(x, y, 'o')
#        li.set_xdata(x)
#        li.set_ydata(y)
#        ax.relim()
#        ax.autoscale_view(True,True,True)
#        fig.canvas.draw()
#        print(sec)
#        data, sec = tick(data, sec, 0)

#    grid = generateGrid(data)
#    button = ''
#    second = 0
#    print(second)
#    graph(data)
#    for y in grid:
#        print(''.join(y))
#    while button != 'q':    
#        button = input()
#    for i in range(4):
#        tick(data)
#        grid = generateGrid(data)
#        second += 1
#        print(second)
#        graph(data)
#        for y in grid:
#            print(''.join(y))
