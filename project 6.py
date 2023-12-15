print()


print("======================================== Project No: 6 ==================================================")

print()

print(">> This is a contract application")

print()


contract = { }

choicelist = """1. Add a new contract \n
2. Search  the contract number \n
3. Create a new Contract Number \n
4. Edit the Contract Number \n
5. Delete the Contract Number \n

"""

while True:
    choice = input(choicelist, ">> Enter Your Choice :  ")

    if choice == "1":
        name = input("# Write the Name : ")
        print()
        number = input("# Write the Number :  ")
        print()

        contract[name] = number

    elif choice == "2":
        searchname = input("# Write the Contract Name : ")
        print()
        if searchname in contract:
            print()
            print(searchname, "'s contract number is : ", contract[searchname])
            print()

        else:
            print()
            print(">> This Contract is not Found.")
            print()
    elif choice == "3":
        

print()
    





















