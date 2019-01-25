#!/usr/bin/env python


def getCoordPower(coord, serial):
    x, y = coord
    rack_id = x + 10
    power = rack_id * y
    power = power + serial
    power = power * rack_id
    if power > 99:
        power = int(str(power)[-3])
        power = power - 5
        return power
    else:
        return 0

def biggestNine(serial):
    grid = []
    for y in range(300):
        grid.append([getCoordPower([x, y], serial) for x in range(300)])
    res, sum = findLargestPower(grid, serial)
    return res, sum

def findLargestPower(grid, serial):
    # check every 3x3 area
    pow = {}
    for y in range(len(grid) - 2):
        for x in range(len(grid[0]) - 2):
            pow['{0},{1}'.format(x,y)] = [ grid[y][x1] for x1 in range(x, x + 3) ]
            pow['{0},{1}'.format(x,y)] = pow['{0},{1}'.format(x,y)] + [ grid[y + 1][x1] for x1 in range(x, x + 3) ]
            pow['{0},{1}'.format(x,y)] = pow['{0},{1}'.format(x,y)] + [ grid[y + 2][x1] for x1 in range(x, x + 3) ]
    biggest = {"key" : 0, "sum" : 0}
    for key, val in pow.items():
        tot = sum(val)
        if biggest["sum"] < tot:
            biggest["sum"] = tot
            biggest["key"] = key
        elif biggest["sum"] == tot:
            biggest["key"] += " " + key
    return biggest["key"], biggest["sum"]
            
def main():
    serial = 9424
    res, sum = biggestNine(serial)
    print(res, sum)

if __name__ == "__main__":
    main()
