# Challenge: make exits a dictionary (w/ keys being the
# numbers of the locations and values being dictionaries
# holding the exits.

locations = {0: 'You are at home learning Python.',
             1: 'You are standing at the end of the road before a small brick building',
             2: 'You are at the top of a hill',
             3: 'You are inside a building, a well house for a small stream',
             4: 'You are in a valley beside a stream',
             5: 'You are in the forest'}

exits = {0: {'Q': 0}, 1: {'W': 2, 'E':3, 'N': 5, 'Q': 0},
          2: {'N': 5, 'Q': 0},
          3: {'W': 1, 'Q': 0},
          4: {'N': 1, 'W': 2, 'Q': 0},
          5: {'W': 2, 'S': 1, 'Q': 0}}


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