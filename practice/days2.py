print()


print("================ Find Factorial and No of Trailing Zeros in a Factorial of a Number ============")  #> 5! = this is '5' factorial


print()


def factorial_(number):
    if number == 0 or number == 1:
        return 1
    else :
        return number * factorial_(number - 1)





# def factorialtrailingzeros(number):
#     pass


if __name__== '__main__':
    number = int(input('enter a number : '))
    print()

    fac = factorial_(number)
    print(f"> your number is : {number}")

    print()

    print(f"# the factorial is {fac}")





































print()




