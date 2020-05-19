s1 = "1234567890"

my_iterator = iter(s1)
#
# for i in range(1, 10):
#     print(next(my_iterator))
#
# print("-" * 80)
# for char in s1:
#     print(char)
#
# print("-" * 80)
# for char in iter(s1):
#     print(char)
#

# Iterator challenge

for i in range(1, len(s1)):
    print(next(my_iterator))