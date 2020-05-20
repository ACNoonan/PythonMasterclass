fruit = {'orange': 'a sweet, orange, citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a sour, yellow, citrus fruit',
         'grape': 'a small, sweet fruit grown in bunches',
         'lime': 'a sour, green citrus fruit'}
print(fruit)
print(fruit['lemon'])

# Can't call 2 values at once
#print(fruit['lemon', 'lime'])


# Adding** (NOT APPENDING) to the dictionary
fruit['pear'] = 'an odd shaped apple'
print(fruit['pear'])

# Deleting from a dictionary (Will remove entire dictionary if key not specified)
# del fruit['lemon']
# print(fruit)

# Clearing a dictionary, while still retaining it's name
# fruit.clear()
# print(fruit)

# Processing input to search the dictionary
# Method 1: No Catching unfound keys
# while True:
#     dict_key = input('Please enter a fruit: ')
#     if dict_key == 'quit':
#         break
#     elif dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print('Sorry, no {} here!'.format(dict_key))

# Method 2:
while True:
    dict_key = input('Please enter a fruit: ')
    if dict_key == 'quit':
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)
