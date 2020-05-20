# # # 2 Ways to Create Sets:
# #
# # farm_animals = {'sheep', 'cow', 'hen'}
# # print(farm_animals)
# #
# # for animal in farm_animals:
# #     print(animal)
# #
# # print('-' * 40)
# #
# # wild_animals = set(['lion', 'tiger', 'panther',
# #                     'elephant', 'hare'])
# # print(wild_animals)
# #
# # for animal in wild_animals:
# #     print(animal)
#
# # How to Create an Empty Set:
# empty_set = set()
# empty_set.add('a')
#
# # Doesn't work, adds dict
# #empty_set2 = {}
# #empty_set2.add('a')
#
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(squares_tuple)
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print('-' * 40)

# Playing with intersection() and &'s
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# Creating a set from a range & a tuple
# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# .difference() = minus for sets
# print('even minus squares:')
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
# print('squares minus even')
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# print('-' * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

# Symmetric difference is the opposite of intercept
# print('symmetric minus squares')
# print(sorted(even.symmetric_difference(squares)))
#
# print('symmetric squares minus even')
# print(squares.symmetric_difference((even)))

# .discard = .remove
# squares.discard(4)
# squares.remove(16)
# squares.discard(8) # Doesn't throw an error even though there is no 8 in squares
# print(squares)
# # The following will throw an error:
# try:
#     squares.remove(8)
# except KeyError:
#     # print('The item 8 is not a member of this set')

even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(squares)

if squares.issubset(even):
    print('squares is subset of even')
if even.issuperset(squares):
    print('even is a superset of squares')


# Frozen sets are immutabele tooo
print('-' * 40)
even = frozenset(range(0, 100, 2))

print(even)
even.add(3)