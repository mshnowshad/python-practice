
# print()



print('Hello world')

print("")

print()


answer = input("# Are you play the game:[yes or no]: ")

if answer == "yes":
    print("Wellcome to PyGame.")
    print()

    answer1 = input(">>Are you going to jugle or cave [jungle or cave] : ")
    if answer1 == "jungle":
        print("> tiger is coming . killed you.")

    elif answer1 == "cave":
        print("> can you seen the Bear .")

        answer2 = input("> do you fight this Bear or run the way . [fight or run]: ")
        if answer2 == "run":
            print(">> You running the way. You catch the car and run this way")
            print()
            print("Your are so Brave")
            print()

            answer4 = input(">>>> Do You come back home [yes or no] -: ")
            if answer4 =='yes':
                print("you come the house.you are brave.\n  Thanks for play game .")

            elif answer4 =='no':
                print("> Congratulation!. ")
                print()

                print("Hum your so Brave .\n Booyah. \n #\n > Winner Winner chicken Dinner.")
            


        else:
            print(">> Bear is to much strong and killed you.\n Game over")



    else:
        print("> Game over")
    
else:
    print('Try Again The game . This is very wonderfull game')


print()















