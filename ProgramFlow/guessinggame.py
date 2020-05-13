import random

highest = 1000
answer = random.randint(1, highest)
guess = 0

0
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess > answer:
        print("Sorry, guess lower!")
        continue
    elif guess < answer:
        print("Sorry, guess higher!")
        continue

print("Congrats, you got it!")


# # Challenge2 solution:
# while guess != answer:
#     if guess > answer:
#         print("Sorry, guess lower!")
#         continue
#     if guess < answer:
#         print("Sorry, guess lower!")
#         continue
# guess = int(input())
# print("Congrats, you got it!")






# Challenge 1 solution:
# if guess == answer:
#     print("You're a genius! Got it in one!")
# elif guess < answer:
#     print("Please guess higher")
# else:
#     print("Please guess lower")
# guess = int(input())
# if guess == answer:
#     print("Great job, you got it!")
# else:
#     print("Sorry, better luck next time!")


