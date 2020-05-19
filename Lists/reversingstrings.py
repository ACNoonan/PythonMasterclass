string_1 = str(input("Enter string to be reversed here: "))


# Solution 1; Slicing
def reverse_slicing(s):
    return s[::-1]


if __name__ == "__main__":
    print('Reversing string with slicing: ', reverse_slicing(string_1))


# Solution 2; For-Loop
def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # Appending chars in reverse order
    return s1


if __name__ == "__main__":
    print('Reversing string using For-loop: ', reverse_for_loop(string_1))


# Solution 3; While-Loop
def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1


if __name__ == "__main__":
    print("Reversing string using While-Loop: ", reverse_while_loop(string_1))


# Solution 4: Using join() & reversed()
def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1


if __name__ == "__main__":
    print("Reversing string using join() & reversed(): ", reverse_join_reversed_iter(string_1))


# Solution 5: Using list reverse()
def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)


if __name__ == "__main__":
    print("Reversing string using list.reverse(): ", reverse_list(string_1))


# Solution 6: Using Recursion
def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) +s[0]

if __name__ == "__main__":
    print("Reversing string with Recursion: ", reverse_recursion(string_1))