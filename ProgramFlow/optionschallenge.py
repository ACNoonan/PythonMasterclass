option_1 = "1. Blissfully happy the rest of your life "
option_2 = "2. One-time lump sum of a billion USD (taxed) "
option_3 = "3. One-time lump sum of a billion USD to charity (untaxed) "
option_4 = "4. $250,000 every year for the rest of your life (taxed) "
option_5 = "5. The end to all war on Earth, forever "
option_6 = "6. The end to all disease on Earth, forever "
option_7 = "7. Immediately meet the love of your life, live happliy ever after "
option_8 = "8. Ability to control your aging "
option_9 = "9. Can permanently & subtly influence anyone you can see's opinion of you "

choice = "-"

while True:
    if choice == "0":
        break
    elif choice in "123456789":
        print("You chose {}".format(choice))
    else:
        print("Please Select an Option: \n"
              "\t{0}\n"
              "\t{1}\n"
              "\t{2}\n"
              "\t{3}\n"
              "\t{4}\n"
              "\t{5}\n"
              "\t{6}\n"
              "\t{7}\n"
              "\t{8}\n"
              "\t0. Exit \n"
              "".format(option_1, option_2, option_3, option_4,
                        option_5, option_6, option_7, option_8,
                        option_9))

    choice = input("I wish for: ")

# My initial solution:
# while wish:
#     if wish in "123456789":
#         print("Thanks for playing, you chose".format(wish))
#         break
