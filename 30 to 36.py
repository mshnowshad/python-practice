


"""30 = Tuple type data"""
###>>> tuple type data like a List but this is not changeable/ immutable
#>> tuple er kunu 'Data change ' korthe hole "list()" a casting / convert kore change korthe hoy




### "Python - Tuple Methods"
print("Python - Tuple Methods")
"""
x.count()	Returns the number of times a specified value occurs in a tuple

x.index()	Searches the tuple for a specified value and returns the position of where it was found
"""






print("This is Tuple")

tuple1 = ("a", "b", "d", "c")

#tuple1[0] = 101 #> this immutable
print(type(tuple1))




### Access tuple item

print(" Access tuple : ")

##>>>Print the second item in the tuple:

thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[1])



# Negative indexing >>>Negative indexing means start from the end.
print("Negative Indexing")

accesstup1 = ("hablu", "python", "web")

print("Printed the last item :",accesstup1[-1])  # >  last item theke index count kore




# Range of Indexes
print("Range of Indexes")

#>>> Return the third, fourth, and fifth item

thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print("Tupleaccess type 1",thistuple2[2:5])  #> 2 theke 4 er index er item print korbe

thistuple3 = ("apple", "banana", "cherry", "orange.", "kiwi", "melon", "mango")

print(thistuple3[:4])  #> 0 index theke 3 index porjontho print korbe

thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print("Tupleaccess type 3:",thistuple4[2:])  #>> 2index 2index number theke end item porjonto print korbe





### 31 = Python Update Tuple and delete tuple

#>>> list a convert kore tuple ke update korte hoy , update korar por abar tuple a convert kore output tuple phethe pari.

print("31 .Python Update Tuple and delete tuple")



x = ("apple", "banana", "cherry")

y = list(x)  #> tuple ke list a convert kore

y.append("kiwi")  #> list a item add kore. this item is added last

x = tuple(y)  # > list ke tuple() a convert kore tuple output hoy

print("My update update tuple: ", x)




#>>> tuple ke tuple a reke item add kora jay.
thetuple = ("apple", "banana", "cherry")

y1 = ""

thetuple += 101,  #> tuple ke assingment operator use kore item add kora jay. valuer pashe "," eita dithe hoy

print("your original tuple:", thetuple)
print()




##>> delete tuple

deletetuple = ("apple", "banana", "Hablu", "cherry")

y = list(deletetuple)

y.pop(-1)

deletetuple = tuple(y)

print(deletetuple)

print()






### 32 = Unpack Tuple
#>>> we are also allowed to extract the values back into variables. This is called "unpacking":

print("32 = Unpack tuple")

unpacktuple = ("apple", "banana", "cherry")

print(unpacktuple[0])




#another type

u, n, p = unpacktuple

print("your unpack tuple is :", n)



#Using Asterisk*
#>>> different variable use na kore 1ti variable er samne [" * "] multiply diye full tuple ke unpack kora jay

unpacktuple = ("apple", "banana", "cherry", "python", "lomborgini")
*n, b = unpacktuple

print("Using asterisk:", n)  #>> je tho gula item ase sob gula nibe but last item sara . because last value ta  "b" variable

print(b)
print()
print()





### 33 = Python loop Tuple
print("33 = Python loop Tuple")

# Python For Loops
print("Python For Loops:")


looptuple = ("apple", "banana", "cherry")
for x in looptuple:
  print(x)

print()




#Using a While Loop
print("Using a While Loop:")

whiletuple1 = ("apple", "banana", "cherry", "python", "lomborgini")
i = 0

# list a jotho len number ase shei ta diye kaj korbe . len(thislist) na diye "3" dithe partham
while i < len(whiletuple1):

  print(whiletuple1[i])

  i += 1  # while loop end korar jonno aktar por arek item add korte hoy

print()
# same as
"""
i2 = 0
while i2 < 4:

  print(whiletuple1[i])

  i += 1


print()
"""
print()


#### 34 = Python Join Tuple
print("34 = Python Join Tuple")

#To join two or more tuples you can use the "+" operator

jointuple1 = ("a", "b")
jointuple2 = (1, 2)

jointuple3 = jointuple1 + jointuple2
print("#use '+' operator for join tuple:", jointuple3)



#use the * operator:
jointuple4 = (1, 2)
#jointuple5 = ("apple", "banana", "cherry")
jointuple = jointuple4 * 2

print("#use the '*' operator:", jointuple)
print()



### tuple count \ index number

print("tuple count:")

#Returns the number of times a specified value occurs in a tuple\ j value dibay tar count kore\ koyta ase tha vole dey

counttuple1 = (1, 2, 4, 6, 7, 8, 4, 5, 6, 7, 8, 9)
count1 = counttuple1.count(4)  # j value dibay tar count kore\ koyta ase tha vole dey



print("# count your value tuple:", count1)

#Searches the tuple for a specified value and returns the position of where it was found \ value index position bole dey >>> index sob somoy 0 theke start kore

indx1 = counttuple1.index(9)
print("your value index position is :", indx1)

print()
print()





#### 36 = tuple Exercise:
print("36 = tuple Exercise:")

print("Exercise: 1")

#Use the correct syntax to print the first item in the "fruits" tuple.

Exercise1 = ("apple", "banana", "cherry")
print(Exercise1[0])
print()

print("Exercise : 2")
#Use the correct syntax to print the number of items in the fruits tuple\ koy ta item ase tha print koro

Exercise2 = ("apple", "banana", "cherry")

print(len(Exercise2))
print()

print("Exercise : 3")

#Use negative indexing to print the last item in the tuple.

Exercise3 = ("apple", "banana", "cherry")
print(Exercise3[-1])
print()

print("Exercise : 4")

#Use a range of indexes to print the third, fourth, and fifth item in the tuple.

Exercise4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(Exercise4[2:5])

print()
















































































































































































































































