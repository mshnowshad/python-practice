



"""37 Python Set """ # used "{}" this bracket >> second bracket use korth hoy
#Sets are used to store multiple items in a single variable.  >> "Sets cannot have two items with the same value".  >>"Set items are unchangeable but you can remove items and add new items with use method"


print("#37 Python Set ")
print()



print("Python all method:")


#> x.add()	= Adds an element to the set >># exemple line "111"

#> x.update()	 = Update the set with the union of this set and others >># exemple line "125"

#> x.copy()	  = Returns a copy of the set  >>#exemple line "148"

#> x.remove()	  =  Removes the specified value name  >># exemple line "136"

print()
print()


myset = {"apple", "banana", "cherry"}
print("Python Set:",myset)
print("set type:",type(myset))



#>>> Duplicate values will be ignored:

myset1 = {"apple","apple", "banana", "cherry", }

print("#ignored same value:",myset1)

print()


#Unordered set
print("Unordered set:")

#>> True and 1 is considered the same value:

unordered1 = {"apple", "banana", "cherry", 1, 2, False}

print("Unordered set:",unordered1) #>> 1,2 value age ashe nai so unordered set

print()





print("# Get the Length of a Set:")
#>>> To determine how many items a set has, use the len() function.


lenset1 = {"apple","apple", "banana", "cherry", }
print("length set: ",len(lenset1))
print()




# Set Items - Data Types
#>>Set items can be of any data type:
#>> A set with strings, integers and boolean values:

typeset1 = {"abc", 34, True, 40, "male",101.100}

print(" Set Items Data Types:",type(typeset1))
print()





print("The set() Casting :")
#>> It is also possible to use the set() constructor to make a set.
print()


#>> Using the "set()" constructor to make a set:

constructor1 = set(("apple", "banana", "cherry")) # note the double round-brackets

print("Using Casting:" ,constructor1)

print()





print("38 > Python - Access set items:")

## >> You cannot access items in a set by referring to an index or a key.   >>> But you can loop through the set items using a "for" loop, or ask if a specified value is present in a set, by using the "in" keyword.
print()


print("Access set with 'for' loop:")

accessset1= {"apple", "banana", "cherry"}
for a in accessset1:
  print("access my set :",a)

print()


#>> Check if ""apple"" is present in the set:
print("Check if \"apple\" is present in the set:", "apple" in accessset1)

#print(accessset1[0]) >> error because this is not method in set data
print()




print("39 = Python 'Add' set item:")
print()

addset1 = {"pineapple", "mango", "papaya",22,101}

addset1.add("hi")
print(">> We used add method:",addset1)

print()



print('UPDATE 2 set in one set')
#>> Add elements from anotherset into addset2:


sett = {"apple", "banana", "cherry"}
addset2 = {"pineapple", "mango", "papaya"}

addset2.update(sett)
print(">> update set",addset2)
print()



print("40 = Remove set item:")

remoset1 = {"apple", "banana", "cherry","pineapple", "mango", "papaya"}


remoset1.remove("apple")
print(">> Using remove method:",remoset1)
print()


remoset2= remoset1.copy() 

remoset2.clear()
print(">> using clear method:",remoset2)

print()



print("#>  Python for loop in set:")

loop1 = remoset1.copy()

for a in loop1:
  print(">> useing for loop: ",a)

print()



























































































































