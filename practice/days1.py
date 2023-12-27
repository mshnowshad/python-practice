print()




print("=========== create an indian kirana store calculator and Receipt Generator  ==========")



print()


#> write a python program which will keep adding a stream of numbers inputted by the user. the adding stop as soon as user presses q key on the keyboard


sum = 0
while True:

    UserInput = input("> Enter the item price or press 'q' for \"Quit\" : \n ")
    print()

    if UserInput != "q":
        sum = sum + int(UserInput)
        print(f">> Order total so far: {sum} ")



    else:
        print()
        print("> thanks for using our calculator.")
        print(f"> Your bill total is {sum}. Thanksfor shopping with us.")
        break



    

























































print()
