age = int(input("How old are you? "))

if 16 <= age <= 65:
    print("Work will set you free")
else:
    print("enjoy your free time")


print("-" * 80)

if age < 16 or age > 65:
    print("enjoy your free time")
else:
    print("Have a good day at work")


#if age >= 16 and age <= 65:
#    print("Work will set you free")