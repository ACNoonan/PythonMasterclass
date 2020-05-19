# This script was provided to show why you still can't rely
# on  Python to keep the order of a Dictionary, even w/ 3.6

numbers = {
    1: 'one',
    3: 'three',
    5: 'five',
    7: 'seven',
    9: 'nine',
}

print("I can count odd numbers in order")
for key in numbers:
    print(numbers[key])

numbers[8] = 'eight'
numbers[2] = 'two'
numbers[6] = 'six'
numbers[4] = 'four'

print()
print("I can count to 9 in order")
for key in numbers:
    print(numbers[key])

# If your code relies on the keys being sorted, sort them first
print()
print("I really can")
for key in sorted(numbers):
    print(numbers[key])