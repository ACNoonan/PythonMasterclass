# list_1 = []
# list_2 = []
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# # list() constructor CREATES A NEW LIST
# # another_even = even       # ((DOES NOT CREATE A NEW LIST))
# another_even = list(even)
# another_even.sort(reverse=True)
#
# # Comparing lists
# print(even)
# print(another_even)
# # Checking for equivalency
# print(another_even is even)
# print(another_even == even)


#Creates a list of 2 lists
numbers = [even, odd]
print(numbers)

# Iterates through the list of lists, and then the values in each list
for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value)