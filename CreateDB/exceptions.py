def factorial(n):
    # n! can also be defined as n * (n-a)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        # print( n / 0)
        return n * factorial(n-1)

try:
    print(factorial(900))
except (RecursionError, ZeroDivisionError):
    print("This program cannot calculate factorials that large")

print("Program Terminating")