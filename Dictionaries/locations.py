locations = {0: 'You are at home learning Python.',
             1: 'You are standing at the end of the road before a small brick building',
             2: 'You are at the top of a hill',
             3: 'You are inside a building, a well house for a small stream',
             4: 'You are in a valley beside a stream',
             5: 'You are in the forest'}

exits = [{'Q': 0},
         {'W': 2, 'E': 3, 'N': 5, 'Q': 0},
         {'N': 5, 'Q': 0},
         {'W': 1, 'Q': 0},
         {'N': 1, 'W': 2, 'Q': 0},
         {'W': 2, 'S': 1, 'Q': 0}]

print(exits[1])
print('E' in exits[1])
print(exits[1].keys())
print(2 in exits[1].values())

print('-' * 40)


loc = 1
while True:
    available_exits = ', '.join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input('Available exists are ' + available_exits + ' ').upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print('You cannot go in that direction')