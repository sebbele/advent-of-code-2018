#!/usr/bin/env python

def getLayout(input):
    layout = input.split('\n')
    for y in range(len(layout)):
        layout[y] = layout[y].replace('>', '-')
        layout[y] = layout[y].replace('<', '-')
        layout[y] = layout[y].replace('v', '|')
        layout[y] = layout[y].replace('^', '|')
    return layout

def getCarts(input):
    carts = {}
    cart_id = 0
    cart = [ 'v', '^', '<', '>']
    input = input.split('\n')
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] in cart:
                carts[cart_id] = { "pos_x" : x, "pos_y" : y, "turn" : "left", "facing" : input[y][x]  }
                cart_id += 1
    return carts

def getCartOrder(carts):
    cart_vals = {}
    for cart in carts:
        cart_vals[cart] = int(str(carts[cart]['pos_y']) + str(carts[cart]['pos_x']))
    sorted_ids = sorted(cart_vals.items(), key=lambda kv: kv[1])
    order = []
    for i in sorted_ids:
        order.append(i[0])
    return order

def tick(carts, layout):
    cart_order = getCartOrder(carts)
    to_remove = []
    for cart in cart_order:
        y = carts[cart]['pos_y']
        x = carts[cart]['pos_x']
        if x == -1 or y == -1:
            continue
        facing = carts[cart]['facing']
        if facing == '^':
            new_y = y - 1
            new_x = x
        elif facing == '>':
            new_y = y
            new_x = x + 1
        elif facing == 'v':
            new_y = y + 1
            new_x = x
        elif facing == '<':
            new_y = y
            new_x = x - 1
        for other_cart in carts:
            if carts[other_cart]['pos_y'] == new_y and carts[other_cart]['pos_x'] == new_x and cart != other_cart:
                to_remove.append(other_cart)
                to_remove.append(cart)
                carts[cart]['pos_x'] = -1
                carts[other_cart]['pos_x'] = -1
                carts[cart]['pos_y'] = -1
                carts[other_cart]['pos_y'] = -1
                continue
        track = layout[new_y][new_x]
        new_facing = facing
        if track == '/':
            if facing == '<':
                new_facing = 'v'
            elif facing == '>':
                new_facing = '^'
            elif facing == '^':
                new_facing = '>'
            elif facing == 'v':
                new_facing = '<'
        elif track == '\\':
            if facing == '<':
                new_facing = '^'
            elif facing == '>':
                new_facing = 'v'
            elif facing == '^':
                new_facing = '<'
            elif facing == 'v':
                new_facing = '>'
        elif track == '+':
            turn = carts[cart]['turn']
            if turn == 'straight':
                carts[cart]['turn'] = 'right'
            elif turn == 'left':
                if facing == '<':
                    new_facing = 'v'
                elif facing == '>':
                    new_facing = '^'
                elif facing == '^':
                    new_facing = '<'
                elif facing == 'v':
                    new_facing = '>'
                carts[cart]['turn'] = 'straight'
            elif turn == 'right':
                if facing == '<':
                    new_facing = '^'
                elif facing == '>':
                    new_facing = 'v'
                elif facing == '^':
                    new_facing = '>'
                elif facing == 'v':
                    new_facing = '<'
                carts[cart]['turn'] = 'left'
        carts[cart]['pos_x'] = new_x
        carts[cart]['pos_y'] = new_y
        carts[cart]['facing'] = new_facing
    for id in to_remove:
        carts.pop(id)
    if len(carts) == 1:
        print(carts)
        exit()
    return carts

def main():
    with open('13_input.txt', 'r') as f:
        input = f.read()
    layout = getLayout(input)
    carts = getCarts(input)
    carts = tick(carts, layout)
    while True:
        carts = tick(carts,layout)

if __name__ == "__main__":
    main()
