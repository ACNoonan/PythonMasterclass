#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])  # Nre (Up to not including 6, steps of 2)
print(parrot[0:6:3])  # Nw  (Up to not including 6, steps of 3)

number = "9,223;372:036 854,775;807"
#print(number[1::4])  #starts at ',' & goes to the end, steps of 4
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])



#print(parrot[0:6])    # Norweg (Up to but not including!!)
#print(parrot[-14:-8]) # Norweg (Up to but not including!!)
#
#print(parrot[-4:2])   # Fails (Up to but not including!!)
#print(parrot[-4:-2])  #Bl    (Up to but not including!!)
#print(parrot[-4:12])  #Bl    (Up to but not including!!)





#print(parrot[3:5])  #we
#print(parrot[0:9])  #Norwegian
#print(parrot[:9])   #Norwegian
#print(parrot[10:14])  #Blue
#print(parrot[10:])
#
#print(parrot[:6] + parrot[6:])
#print(parrot[:])


#print(parrot)
#
#print(parrot[3])
#print(parrot[4])
#print(parrot[9])
#print(parrot[3])
#print(parrot[6])
#print(parrot[8])
#
#print()
#
#print(parrot[-11])
#print(parrot[-10])
#print(parrot[-5])
#print(parrot[-11])
#print(parrot[-8])
#print(parrot[-6])
#
#print()
#
#print(parrot[3 - 14])
#print(parrot[4 - 14])
#print(parrot[9 - 14])
#print(parrot[3 - 14])
#print(parrot[6 - 14])
#print(parrot[8 - 14])
