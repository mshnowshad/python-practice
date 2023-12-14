

""" Python Conditions and If statements """

print("#> 49 = Python IF Else Condition . ")
print()
"""

>> These conditions can be used in several ways, most commonly in "if statements" and loops.

>> An "if statement" is written by using the 'if' keyword."""


print("Python supports the usual logical conditions from mathematics:")

"""

=> Equals: "a == b"

=> Not Equals: " a != b" 

=> Less than: "a < b"

=> Less than or equal to:  "a <= b"

=> Greater than: "a > b "

=> Greater than or equal to: "a >= b"

"""

print()


print("# If statement : ")


#>> If statement:

a = 200
b = 30

if b < a: #return  true because "b" value "a" value theke chutu
  
  print("'a' is greater than 'b'")

if a < b: 
  print("'a' is less than 'b'") #return not show because "a"  greater than "b"



print()


print("Elif statement :")


#>> The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 101
b = 101.101

if a < b :
  print("'a' less than 'b'")


elif a == b :
  print("'a' is equal to 'b'")

elif a > b :
  print("'a' greater than 'b'")


print()




print("Else Statement:")


#>>> The "else" keyword catches anything which isn't caught by the preceding conditions.

#>> exemple:

x = 20

y = 99


if x > y :  #return not show 
  print("'x' greater than 'y'")

elif x == y : #return not show
  print("'x' is equal to 'y'")


else : #return "show " because this condition is True
  print("'x' less than 'y'")
print()

print()



print("# Exercise : 1")



#>Print "Hello World" if a is greater than b.


a = 50
b = 10
if a > b :
  print("Hello World")

print()



print("# Exercise : 2")


#> Print "Hello World" if a is not equal to b.


a = 50
b = 10
if a !=  b:   #>return printed because this condition is True.
  print("Hello World")

print()



print("# Exercise : 2")

#>Print "Yes" if a is equal to b, otherwise print "No".


a = 50
b = 10
if a == b :  #> return not printed because this conditon is False.
  print("Yes")
else:
  print("No")

print()



print("# Exercise : 3")

#>Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".


a = 50
b = 10

if a == b:
  print("1")

elif a > b :
  print("2")

else:
  print("3")

print()



print("# Exercise : 4")


a = 101
b = 101
c = 101
d = 101

#>>Print "Hello User, Welcome to python" if a is equal to b, "and" c is equal to d.


if a == b and c == d: # return printed because all condition is True.  #>>> 1 ta false oile sob gula false dekay 
  print("Hello User, Welcome to python")

print()



print("#Exercise :  5")



#>Print "Hello" if a is equal to b, "or" if c is equal to d.


a = 101
b = 101
c = 101
d = 101.1

if a == b or c == d: #> return printed because any one condition is True. #> akta condition jodi true hoy thahole sob gula True
  print("Hello")

print()


print("#Exercise : 6")


#>>Complete the code block, >print "YES" if 5 is larger than 2.


if 5 > 2:
  print("YES")

print()





print("#Exercise: 7")

#>>Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").


a = 2
b = 5
print("YES") if a == b else print("NO")  # this is new syntex

print()


print("#Exercise ; 8")



#>>Use an if statement to print "YES" if either a or b is equal to c.


a = 2
b = 50
c = 2
if a == c or b == c :
  print("YES")


print()

print()
print()
print()
print()






print("Welcome to calculator  ")
print()

a = float(input("> Enter your first Element :  "))
print()

b = input("> Enter your operator :  ")
print()

c = float(input("> Enter your second Element: "))
print()

if b == "+":
  print("Your '+' number =  ", a + c)
  print()
  print("Thanks for use my calculator")

elif b =="-":
  print("Your '-' number =  ", a - c)
  print()
  print("Thanks for use my calculator")

elif b == "*":
  print("Your '*' number = ", a * c)
  print()
  print("Thanks for use my calculator")

elif b == "/":
  print("Your '/' number = ", a / c)
  print()
  print("Thanks for use my calculator")

elif b == "**":
  print("Your '**' number = ",a ** c)
  print()
  print("Thanks for use my calculator")

elif b == "%":
  print("Your '%' number = ",a % c)
  print()
  print("Thanks for use my calculator")


else:
  print("invaild operator, Thanks for your come")


