
"""Python Classes and Object """

#>> একটি ক্লাস অবজেক্ট তৈরি করার জন্য একটি কোড টেমপ্লেট। বস্তুর সদস্য ভেরিয়েবল আছে এবং তাদের সাথে যুক্ত আচরণ আছে। পাইথনে কিওয়ার্ড ক্লাস দ্বারা একটি ক্লাস তৈরি করা হয়। ক্লাসের কনস্ট্রাক্টর ব্যবহার করে একটি অবজেক্ট তৈরি করা হয়। এই অবজেক্টটিকে তখন ক্লাসের ইনস্ট্যান্স বলা হবে।
#> "class" is a 'father ' and 'son' is a "object"


print("")


class myclass:  #> line: 11,12,13 is a tamplate
  name = ""
  age = ""
  
a = myclass() #> "myclass()" is a 'class' and "a" is a 'object'  

a.name = "nowshad"  #> "name" is a 'property' 
a.age = 18

b = myclass()
b.name = "Nabil AL Hasan"
b.age = 16

#> jotho ecca thotho data print korthe parbo... only use 'object' 

print("> Your name is ",a.name)
print("> Your age is ",a.age)
print()

print("> Your friend's name is ", b.name)
print(">Your friend's age is ", b.age)
print()
print()




print("#> Exercise : 1")

#>Create a class named MyClass:


class MyClass:
  x = 5
  
print()


print("#> Exercise ; 2")

#>Create an object of MyClass called p1:


class MyClass:
  x = 5

p1 = MyClass() #> p1 is a object
print()



print("#>Exercise : 3")


#>Use the p1 object to print the value of x:


class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)
print()


print("#> Exercise : 4")

#>What is the correct syntax to assign a "__init__" function to a class?






class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age








