import sys


# His answer:
def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number")
        except EOFError:
            sys.exit(1)
        finally:
            print("This will always execute")


first_number = getint("Please enter the first number: ")
second_number = getint("Please enter the second number: ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero.")
    sys.exit(2)
else:
    print("Division performed successfully")








# MY ANSWER::
# def game():
#     x = int(input("Heyya Georgie! What's your first number?"))
#     y = int(input("Heyya Georgie! What's your second number?"))
#     z = x / y
#     return z
#
#
# try:
#     game()
# except (ZeroDivisionError, RecursionError, MemoryError, ValueError):
#     print("Not failing on my watch!")
