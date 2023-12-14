""" 43 = Python dictionaries"""
print("43 = Python dictionaries:")

"""
>># Dictionaries are used to store data values in key : value pairs.

>>> "{}" this bracket used for dictionarie.

>># A dictionary is a collection which is "ordered", "changeable" and "do not allow duplicates".

"""


print()




print("#> Dictionaries All Method : ")

#Python has a set of built-in methods that you can use on dictionaries.

r"""
dict.get()	     =    # Returns the value of the specified key    #> "line : 101 "

dict.keys()	     =    #Returns a list containing the dictionary's keys   #> "line : 110 "

dict.update()	   =    Updates the dictionary with the specified key-value pairs    #> "line : 141 "

dict.copy()	     =    # Returns a copy the another dictionary #> "line : 149" 

dict.pop()	     =>    #Removes the element with the specified key   #> "line : 170 "

dict.clear()	   =>   # Removes all the elements from the dictionary #> "line : 172"

dict.values()	   =>    Returns a list of all the values in the dictionary     #> "line : 212 "


dict.fromkeys()  =>    Returns a dictionary with the specified keys and value

dict.items()	   =>    # Returns a list containing  for each "key and value pair"  #> key ar value pair akloge print kore    #>> "line  : 224 "


dict.popitem()	 =    Removes the last inserted key-value pair

dict.setdefault()  =>   Returns the value of the specified key. If the key does not exist: insert the key, with the specified value


"""




#Exemple:

print("dictionarie in dictionaries:")  #>>  this dictionaries called "Nested Dictionarie "

studentsinformations = {
    "nowshad": {
        "name": "Nowshad",
        "roll": "59",
        "shift": "Morning",
        "class": "9th",
        "age": '18',
        "gender": "Male",
        "location": "Sunamganj"
    },
    "nabil": {
        "name": "Nabil Al Hasan",
        "roll": "36",
        "shift": "Morning",
        "class": "9th",
        "age": "16",
        "gender": "Male",
        "location": "Sunamganj"
    }
}
print()

print("> Used len method:", len(studentsinformations))
print(" Used len method for studentsinfo:",len(studentsinformations["nabil"]))

print()

print("> Nowshad information:", studentsinformations["nowshad"])
print()

print(" > Type of dictionarie : ", type(studentsinformations))  # return <class 'dict'>

print()





print("# 44 = Dictionaries - Access item")

print("=> Your output:  ", studentsinformations["nabil"]["roll"])  #> return value of key roll . "roll " is the 'key' and "36" is the value 'pairs'



print()

print("# Used '.get' method for Access items:")
print()

a1 = studentsinformations.get("nabil")
a2 = studentsinformations["nabil"]  # same as "a1"

print("=> Nabil information", a1)

print()

print("# used '.keys' method;")
#The keys() method will return a list of "all the keys" in the dictionary.

#exemple:
a2 = studentsinformations.keys()
print("=> all the keys of dictionary:", a2)

print()







print("#45 = Dictionaries 'Change' \ 'Add' Item ")
#>>> You can change the value of a specific item by referring to its key name:

studentsinformations["nabil"]["roll"] = 37
print("change the nabil rolls:", studentsinformations["nabil"]["roll"])

print()



print("# Update Dictionary")
#>> The update() method will update the dictionary with the items from the given argument. >> added new item in dict value

changedic1 = {
    "brand": "Ford",
    "model": 1964,
    "new": {
        "brand new": "Forder",
        "color": "Black"
    }
}

changedic1["colour"] = "white"
print("> Added new item in this dict: ",changedic1["colour"])
print()



changedic1.update({"new": 2020})  # same as like
print(">> Used '.update()' method for change \ add dict item :", changedic1["new"])  #return "new" : 2020

print()



c1= changedic1.copy()
print("#> copy item", c1) #return "new : 2020" because " line = 140 "

print()






print("#46  Dictionarie = remove item ")
#>>>

print()

print("# Used '.pop' method:- ")
#>> "pop()" method used for remove item with 'value key '
print()

remove1 = {
    "brand":
    "Ford",  #>> "band" is the value 'key' and "Ford" is the  value 'pairs'
    "model": "Mustang",
    "year": 1964
}
remove1.pop("model")
print(">> My dict:   ", remove1)

#remove1.remove("model")
#print("used 'remove' method : " , remove1)  #>> return error because this is not in dict method

print()





print("# Used 'clear' method for remove all items in the dict:")

remove1.clear()
print(">> Used 'clear' method : ", remove1)
print()











print("# 47 = Dictonaries loops item:- ")

\

loops1 = {
    "brand":
    "Ford",  #>> "band" is the value 'key' and "Ford" is the  value 'pairs'
    "model": "Mustang",
    "year": 1964
}

#>>> Printed all key names in the dictionary, one by one:
for k in loops1.keys():
  print("> Printed all 'key' name =>  ", k)

print()



#>> Printed all "value pairs " in the dictionary, one by one:

for i in loops1.values():
  print("> printed all 'value pairs' =>  ", i)

print()






#>> Loop through both "keys and values pairs ", by using the ".items()" method: :
loops2 = {
    "'brand : ":
    "Ford",  #>> "band" is the value 'key' and "Ford" is the  value 'pairs'
    "'model : ": "Mustang",
    "'year  : ": 1964
}

for x, y in loops2.items():
  print("> printed all 'item' =>  ", x, y)  # return => brand : Ford etc.



print()
print()




print("#48 = Dictionary all exercise: ")

print()



print("# Exercise: 1 ")

#>> Use the ".get() method" to print the value of the "model" key of the car dictionary.


car1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("> Printed car's model name: ",car1.get("model"))
print()


print("# Exercise : 2 ")
#>>Change the "year" 'value pairs' from 1964 to 2020.


car2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car2["year"] = 2020
print("> Printed car's year name: ", car2["year"] )

print()

print("# Exercise ; 3")
#>>Add the key/value pair "color" : "red" to the car dictionar

car3 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car3["color"] = "red"
print("> printed car's color name: ",car3["color"])


print()

print("#Exercise ; 4")

#>Use the ".pop() method" to remove "model" from the 'car4' dictionary

car4 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car4.pop("model")
#print("Remove the car's model name : " , ecar4["model"])    #>> return error because |"this item removed the dict"
print("removed the car's model name ")

print()


print("#Exercise; 5")


#>> Use the ".clear() method" to empty the car5 dictionary.
car5 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car5.clear()
print("Empty this car's dict: ", car5) # return {} because this dict is cleared














































