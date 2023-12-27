


""" 18 = Python List """
#=> List is mutable \ changeable. => Any type data used.
# => this function is used to Square bracket "[]"



print('This is  a List: ')

list1 = ['Hablu programmer', 99, 100.99]
list1[1] = 101

print(list1[0])
#print(list1)
print()

list2 = ["hi ", "hello", "gd n8"]

list1, list2 = list2, list1  #=> swapping \ exchangeable type

print(list1)
print(list2)

print()







#### 27 = Python List er All Methods
print(" Python List All Methods")

# 'X' akta variable dore
"""
X.append() > => 	Adds an element at the end of the list \ this function add item to last of the List. "line ; 73"

X.insert()	> Adds an element at the specified index position  > "line : 83"

X.extend()	> Add the elements of a list (or any iterable), to the end of the current list \ 'extend()' used for many list join kora.    > "line : 267"

X.remove()	=> Removes the item with the specified value \ remove item from list with value name  > "line : 102

X.pop()	> Removes the element at the specified index position  > "line ; 112 "

X.clear()	> Removes all the elements from the list  > "line : 126 "

X.copy()	> Returns a copy of the list    > "line : 240 "

X.count()	> Returns the number of elements with the specified value

X.index()	> Returns the index of the first element with the specified value





X.reverse()	=> Reverses the order of the list \ List er item gulu ke boro theke chutu krome shajay

X.sort()	=> sorts the list \ serial by serial shajano item gulu ke.

"""

### 20 = Add Item in List
print("this is a Add Item in List: ")

addlis = ["Website", "programmer", "developer"]




print("Add item with 'append' function .:")

addlis.append("101 days of Code")  # => this function add item to last of the List.

print(addlis)





print('Add item with "insert" function :')

addlis.insert(1, "I am Nowshed")  # Any place add item in List.'1' is index number and 'I am Nowshed' is value

print(addlis)
print()






### 21 = Remove item in List
print("Remove item in list.")

removelis = ["App develop", "web develop", "Data science"]





removelis.remove("App develop")  #=> this function remove item from list with value name .

print('Remove item with "remove" method: ', removelis)

print()





removelis.pop(0)  #=> The pop() method removes the specified index.

print("remove item with 'pop()' method: ", removelis)

print()




thislist = ["apple", "banana", "cherry"]

thislist.clear()  #=> this method used remove all item in list.

print(thislist)







### 22 = Loop in List
print("Loop in List :")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for i in range(
    2):  # range er bithoree index jotho diba tho thoi value print korbe

  print(thislist)

print()

whi1 = 0  # variable er bithore index jotho shei number er value theke start korbe
"""while whi1 < len(thislist): # list a jotho index number ase shei ta diye kaj korbe . len(thislist) na diye "3" dithe partham

  print(thislist[whi1])

  whi1 += 1 # while end kore. bar bar 1 add kore condition fill korbe 
"""

# same as:

while whi1 < 3:

  print(thislist[whi1])

  whi1 += 1  # while loop end korar jonno aktar por arek item add korte hoy

print()






### 23 = List Comprehension

# => "comprehension " used list er int value ke multiply kora

print("23 = List Comprehension :")

comprehen = [1, 2, 3, 4, 5]  #=> this is integer list

comprehenout = [
  i * 2 for i in comprehen
]  # =>list er value ke 2 dara multiply kore chi , List er value list er bithor reke

print("List Comprehension:", comprehenout)  #variable ke output printed

for b in comprehen:
  print(b * 3)  #=> list er value multiply korechi but list er motho na.
print()











### 24 = Python Sort list
#=>  "sort" used 'urdho krome shajano'\ serial by serial

print("sort List.")

srt1 = [2, 4, 1, 5, 3, 6, 7, 9, 8]
srt1.sort()

srt2 = ["a", "b", "d", "c"]
srt2.sort()

print(srt1)
print(srt2)


###reverse
#=> List er item gulu ke boro theke chutu krome shajay \ revers kore dey

print("Revers.")

srt1.sort(reverse=True)
print(srt1)









###25 = Copy list
# => Copy List used a list copy

print("Copy List")

copylis1 = [1, 2, 3, 5, 6, 7]

copylis2 = copylis1.copy()  # => List copy korar function.
print(copylis2)














#### 26 Python Join Two List
#> 2list join korar function.

print("Join 2 List")

joinlis1 = [1, 2, 3, 4]
joinlis2 = [5, 6, 7, 8]

join1 = joinlis1 + joinlis2  #> ei ta bangla method
print(join1)

joinlis1.extend(joinlis2)  #> 'extend()' used for 2list join kora hoy.

print("your extend function used:", joinlis1)










#### 28 = Python List Exercise
print("Python List Exercise .")

print("Exercise 1.:- ")

# =>> Print the second item in the fruits list.

fruits1 = ["apple", "banana", "cherry"]
print("Second number is :", fruits1[1])

print("Exercise 2 ")

# =>> Change the value from "apple" to "kiwi", in the fruits list.

fruits2 = ["apple", "banana", "cherry"]
fruits2[0] = "kiwi"
print(fruits2)

print("Exercise 3 ")

# =>> Use the append method to add "orange" to the fruits list.

fruits3 = ["apple", "banana", "cherry"]
fruits3.append("orange")
print(fruits3)

print("Exercise 4")

# =>> Use the insert method to add "lemon" as the second item in the fruits list.

fruits4 = ["apple", "banana", "cherry"]
fruits4.insert(1, "lemon")
print(fruits4)

print("Exercise 5")

# =>> Use the remove method to remove "banana" from the fruits list.

fruits5 = ["apple", "banana", "cherry"]
fruits5.remove("banana")
print(fruits5)

print("Exercise 6")

# =>> Use negative indexing to print the last item in the list.

fruits6 = ["apple", "banana", "cherry"]
print(fruits6[-1])  # reverse -1 theke shuru hoy

print("Exercise 7")

# =>> Use a range of indexes to print the third, fourth, and fifth item in the list.

fruits7 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits7[2:5])

print("Exercise 8")

#=>>> Use the correct syntax to print the number of items in the list.

fruits8 = ["apple", "banana", "cherry"]
print(len(fruits8))

print()

































































































































































































































































































































