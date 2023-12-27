print()

print("#2  Python Number Guessing Game Bangla Project ")
print()


import random

randomnumber1 = random.randrange(1,100)



print("=> Use random number is 1 to 100")
print()



usernumber1 = int(input("#>> Enter the number : "))
print()




if usernumber1 > randomnumber1:
    
    print("> Your number is to higher")
    print()
    print(f"## Random number is - {randomnumber1}")  #> eita use na korle dekthe partham na j kunta random number .. thai use korthe holo
    print()
    print("please Try Again")





elif usernumber1 < randomnumber1:
    print("> Your number is to lower")
    print()
    print(f"## Random number is - {randomnumber1}") #> eita use na korle dekthe partham na j kunta random number .. thai use korthe holo

    print()
    print('Please Try Again ')

elif usernumber1 == randomnumber1:
    print(">>> Congratulations! , You win!")
    print()
    print(f"## Random number is : {randomnumber1}") #> eita use na korle dekthe partham na j kunta random number .. thai use korthe holo

    print()

    print("Please Try Again ")




else:
    print("> your number is invalid")
    print()
    print(f"## Random number is - {randomnumber1}") #> eita use na korle dekthe partham na j kunta random number .. thai use korthe holo
    print()

    print("Please Try Again ")





print()



