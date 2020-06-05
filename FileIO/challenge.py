# Write a program to append a times table to the jabberwocky poem
# in sample.txt.


with open('sample.txt', 'a') as tables:
    for n in range(1, 13):
        print('{0:2} times {1:1} is {2:<2}'.format(n, 2, (n * 2)), file=tables)
    print('~' * 20, file=tables)