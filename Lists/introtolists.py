# ip_address = input("Please enter an IP Address: ")
# print(ip_address.count("."))
parrot_list = ["non pinin", "no more", "a stiff", " bereft of life"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

print("-" * 80)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
# numbers.sort()
print(numbers)

numbers_in_order = sorted(numbers)
print(numbers_in_order)

# Changing sorts
if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")
