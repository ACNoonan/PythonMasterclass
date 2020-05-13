#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"
emptyLetters = ""

# 1. Reverse letters
print(letters[::-1])

# 2. Print last 4 letters
print(letters[-4:])

# 3. Print first 4 letters
print(letters[:4])

# 4. Get the first letter, and retrieve nothing if string is empty, since
#    print(letters[0]) <- Fails for an empty string
print(letters[:1])
