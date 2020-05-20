
# My solution:
#vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
vowels = frozenset('aeiou')
s = input("Please get me letters I'm hungry!: ")
s2 = set()
for c in s:
    if c in vowels:
        pass
    else:
        s2.add(c)
print(sorted(s2))


# His solution:
final_set = set(s).difference(vowels)
print(final_set)

final_set = sorted((final_set))
print(final_set)