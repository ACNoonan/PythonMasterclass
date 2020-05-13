# Modify the code inside this loop to stop when i is exactly divisible by 11
# for i in range(0, 100, 7):
#     print(i)
#     if (i != 0) and not (i % 11):
#         break

for i in range(0, 20):
    if not i:
        continue
    elif not i % 3:
        continue
    elif not i % 5:
        continue
    else:
        print(i)
