name = str(input("Como te llamas?"))
age = int(input("Y Cuantos anos?"))

if 31 > age > 18:
    print("Congratulations {}, here's your ticket!".format(name))
else:
    print("You are the wrong age loser!")