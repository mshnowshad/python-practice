


"""Python Encapsulation"""

 #>> Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit. In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only through the methods of their current class.

#> এনক্যাপসুলেশন হল ডেটা (ভেরিয়েবল) এবং কোডগুলিকে একক ইউনিট হিসাবে একসাথে ডেটা (পদ্ধতি) এর উপর কাজ করে মোড়ানোর একটি প্রক্রিয়া। এনক্যাপসুলেশনে, একটি ক্লাসের ভেরিয়েবলগুলি অন্যান্য ক্লাস থেকে "লুকানো থাকবে এবং শুধুমাত্র তাদের বর্তমান ক্লাসের পদ্ধতির মাধ্যমে অ্যাক্সেস করা যেতে পারে।"


print("# 78 = Python Encapsulation")
print()



class vehicles:
  def __init__(self,name,model,cast,color):
    
    self.name = name  #> instance variable and "Public" because this is changeable ba anyone can change this ."line : 28 , 29"
    self.model = model
    self.cast = cast
    self.color = color


class car1(vehicles):
  pass

class car2(vehicles):
  pass

class car3(vehicles):
  pass


cr1 = car1("Supra","SS1","60Million","Red")
cr1.model = "sup101"  #> everything is changeable

print("> Your first car model:", cr1.model)
print()



cr2 = car2("BMW","BB200","101million","Silvar")

print("> Your Second car model:",cr2.model)

print()



print("> this is Encapsulation.")
print()


class student:
  def __init__(self,name,rollno ,fathersname , mothersname,age):
    self.__name = name          #> 'Encapsulate' korthe hole 'double underscore' use korthe hobe
    self.__rollno = rollno
    self.__fathersname = fathersname
    self.__mothersname = mothersname
    self.__age = age
    print(self.__name)  #> return output korbe
    
   
en1 = student("Arithro",55,"Arindro Talukdar","Juna Baby",18)

#print(en1.__age)  #> return 'error because "__age "' is now privete kore felsi

print()

print()





print(">> Example by - 'ChatGPT'")


print()




class Student:
  def __init__(self, name, roll):
      self.name = name
      self.__roll = roll  # এনক্যাপসুলেটেড ভ্যারিয়েবল, এইখানে __("doule underscore") ব্যবহার হয়েছে

  def get_roll(self):
      return self.__roll

  def set_roll(self, roll):
      if roll > 0:
          self.__roll = roll

# ক্লাস বাইরে থেকে ইনস্ট্যান্স(Instance) তৈরি
studentinfo = Student("Harryport", 101)




# এনক্যাপসুলেটেড ডেটা এবং মেথডের ব্যবহার
print(studentinfo.get_roll())  # এনক্যাপসুলেটেড মেথডের মাধ্যমে ডেটা অ্যাক্সেস

studentinfo.set_roll(102)  # এনক্যাপসুলেটেড মেথডের মাধ্যমে ডেটা আপডেট

print(studentinfo.get_roll())  # এনক্যাপসুলেটেড মেথডের মাধ্যমে আপডেট করা ডেটা প্রিন্ট










































