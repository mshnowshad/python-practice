
"""Python function"""


print("#51 = python function ")

r"""
> A function is a block of code which only runs when it is called.

> You can pass data, known as parameters, into a function.

> A function can return data as a result.

>> 4 type of function
>Built-in Functions, User-defined Functions, Recursive Functions, Lambda Function.

> function syntex holo "def"
"""

#>> "def function " use na kore "lambda use " kora aro shohoj hoy. "# 56 = Python lambda" number lesson


print()





print("User-defined Function")

def my_function(): #>> eita value change kora jabe na . because brecket er bithor kunu "variable \ চলক" nei
  print("Hei , welcome")

my_function() #>> ei function use na korle kunu kisui output dekave na. this is my function.

print()

print()




def my_new(a,b): #> "a , b" ei argument use na korle different number use kora jay na . means different "value" use korthe parbo nay
  
  print("Your sum : ",a + b) #"a" called a "parameter"

my_new(100 , 99)
 
my_new(1872, 2677)


print()

print()






print("### This another type of function ")
#> eita niya pain nithe hobe na. uprer gula mathay raklei colbe. 
print()



print("#>. Arbitrary Arguments, *args")
print()
#> conditions: If the number of arguments is unknown, add a * before the parameter name:


def my_function(*kids):
  print(">>The youngest child is " + kids[2])

my_function("Emil", "Tobias", "'Linus'") #return printed 'linus' because line:'67' a "kids[2]" deu a  ase. er jonno

print()




print("#> Keyword Argument")

"""

>You can also send arguments with the key = value syntax.

> This way the order of the arguments does not matter.

 """
print()



def my_functions(child3, child2, child1):
  print(">> The youngest child is " + child2)

my_functions(child1 = "Emil", child2 = "'Tobias'", child3 = "Linus")


print()


print("#>> Passing a List as an Argument:")





"""

>> You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

>> E.g. if you send a List as an argument, it will still be a List when it reaches the function:

"""

print()



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print()
print("end this section")




print()



print("#Exercise : 1")


#>>Create a function named my_function1.


def my_function1():
  print("Hello from a function")

print()



print("#>> Exercise : 2")



#>>Execute  a function named my_function2.


def my_function2():
  print("Hello from a function2")

my_function2()


print()



print("#>> Exercise : 3")


##>>Inside a function with two parameters, print the first parameter.


def my_function(fname, lname): #> "fname " is a 'parameter' 
  print(fname)

print()



print("#Exercise : 4")

#> Let the function return the x parameter + 5.


def my_function4(x):
  return x + 5
print()


print("#> Exercise : 5")


#>>If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?


def my_function(*kids):
  print("The youngest child is " + kids[2])
print()



print("#> Exercise : 6")



#>> If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?


def my_function(**kid):
  print("His last name is " + kid["lname"])

print()

print() 
print("hello world")








































