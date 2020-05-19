fruit = {'orange': 'a sweet, orange, citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a sour, yellow, citrus fruit',
         'grape': 'a small, sweet fruit grown in bunches',
         'lime': 'a sour, reen citrus fruit'}

# Iterating
# for snack in fruit:
#     print(fruit[snack])

# Create list, Ordering & iterating
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + ' - ' + fruit[f])
# print(ordered_keys)

# Ordering while creating list, then iterating
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + ' - ' + fruit[f])
# print(ordered_keys)

# Ordering w/o list
# for f in sorted(fruit.keys()):
#     print(f + ' - ' + fruit[f])

# Dealing with only values (ineffcient lookup)
# for val in fruit.values():
#     print(val)
    
# Getting values w/ key lookup (Much more efficient)
# for key in fruit:
#     print(fruit[key])

# print((fruit.items()))
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + ' is ' + description)