#  Without formating
for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}.".format(i, i ** 2, i **3))

print()
print("With Column formatting:")

#  With Column formatting
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i **3))

#  With Left-Align formatting
print()
print("With Left-Align formatting:")
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i **3))

#  With Left & Center-Align formatting
print()
print("With Left & Center-Align formatting:")
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i **3))

print()
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:<62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.55f}".format(22 / 7))


# Without Field Numbers, with Column Formatting
print()
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i **3))