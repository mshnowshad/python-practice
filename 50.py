""" Python loops """

print("#> 50 = python loops")

print()
"""Python has two primitive loop commands:

   > "while" loops
   > "for" loops
"""



print("#> 'while ' loops")
print()

hablu = 0

while hablu < 5:
  print("Yes, hablu is not greter than - ", hablu)

  if hablu == 3:
    break  # means stop koro '3' the asle

  hablu += 1  # hablu = hablu + 1 #> and "Break" this continue

print()
print()





print("#'for ' loop ")

fruits = ["apple", "banana", "cherry"]

for x in fruits:

  if x == "banana":
    break

  print("Used 'break' method :",x)  # return "apple,banana" because condition deu a ase j " x == 'cherry' and "beak" ei jonno

print()

for i in fruits:
  
  if i == "apple":
    continue #> "apple " print na kore jump kore cole jabe "after value " jeta ase ou gula print korbe
  
  print("Used 'continue' method : ",i)
  
print()
print()







print("#> Exercise ; 1 ")

#> Loop through the items in the fruits list.


fruits1 = ["apple", "banana", "cherry"]
for  x in fruits1:
  print(x)


print()





print("#Exercise : 2")


#>>In the loop, when the item value is "banana", jump directly to the next item.


fruits2 = ["apple", "banana", "cherry"]

for x in fruits2:
  
  if x == "banana":
    continue   #> ei ta deyar mean hocce giya "banana" value the jokon asbe thokon eita print na kore "After value" print korbe

  print(x)
print()





print("#Exercise : 3")

#> Use the "range" function to loop through a code set "6" times.


for x in range(6):
  
  print("i love code",x) #> "i love code " 6 times print hobe karon "range" er bithor "6" deu a oise.

print()



print("# Exercise : 4")




#>Exit the loop when x is "banana".


fruits4 = ["apple", "banana", "cherry"]
for x in fruits4:
  
  if x == "banana":
    break

  print(x)


print()


print("#> Exercise : 5 ")

#>> Stop the loop if i is 3.


i = 0
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
print()



print("#>Exercise : 6 ")


#>>In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue

  print(i)


print()




print("#> Exercise : 7")

#>> Print a message once the condition is false.


i = 1
while i < 6:
  print(i)
  i += 1
print()

else:
  print("i is no longer less than 6")


















