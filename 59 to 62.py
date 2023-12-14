"""Python Inheritance"""

print("#59 Python Inheritance.")

#>> ইনহেরিট্যান্স হলো একটি অবজেক্ট-অরিয়েন্টেড প্রোগ্রামিং কনসেপ্ট, যা পাইথনের মধ্যে ব্যবহার হয়। ইনহেরিট্যান্সের মাধ্যমে একটি ক্লাস এক বা একাধিক অন্য ক্লাসের গুনগুলি এবং অপারেশনগুলি বৃদ্ধি করতে পারে। এটি অবজেক্ট-অরিয়েন্টেড প্রোগ্রামিং (OOP) এর একটি মৌলিক অংশ, যা কোড রিউজেবিলিটি এবং মডিউল্যারিটি বৃদ্ধি করতে সাহায্য করে।
#> Inheritance means akta dalal . mane thrithio pokko hocce dalal. ba bichar kore dey
#> inheritance menas  akta class er shathe arek ta class er property gular shomporko kore dey... 


print()



class father:  #> this is "parent class / base class"  #> "inherit"
  car = "Ford Mustang"
  house1 = "Calfornia"
  business = "Google"
  tk = "1 crore"

class uncle(father) : #> this is a "child class / derived class" #> "father" class property er shathe "uncle" er shomporko kore dise..
  phone = "broken iphone"
  house = "Broken House"
  pc1 = "Broken Laptop"

u1 = uncle()
print(u1.car)
print()
print()






print("#> 60 = Python Multiple Inheritance. ")
#> এটি স্থানীয় প্রিসিডেন্স অর্ডার বজায় রাখবে এবং ক্লাসের সদস্যদের রেজোলিউশন অর্ডার বজায় রাখবে। মাল্টিলেভেল ইনহেরিট্যান্স ব্যবহার করা হয় কোড পুনরায় ব্যবহারযোগ্যতা অর্জন করতে, ক্লাসগুলির মধ্যে সম্পর্ক বজায় রাখতে এবং অবজেক্ট-অরিয়েন্টেড প্রোগ্রামিং অর্জন করতে।"
#> 


class baba2:
  phone = "Iphone 14"
  ac = "samsung ac"
  tv = "Lenovo"

class baba3:
  bike = "BMW"
  pc2 = "Intel i5 10gen"


class uncle(father,baba2, baba3) : #> this is a "child class / derived class"   #> eita ou multiple inheritance 
  phone2 = "broken iphone"
  house = "Broken House"
  pc1 = "Broken Laptop"
  


u2 = uncle()

print(u2.pc2)
print(u2.phone)
print(u2.tv)

print()
print()





print("#61 = Python Multilevel Inheritance")
#> 


class father:  #> this is "parent class / base class"  #> "inherit"
  car = "Ford Mustang"
  house1 = "Calfornia"
  business = "Google"
  tk = "1 crore"



class son1(father): #>"Intermediate class "     > 'son2' a gived her 'son1' and 'father ' property

  bike = "BMW"
  pc2 = "Intel i5 10gen"

class son3(son1): #> "Subclass"      > 'son3' a gived her 'son2' , 'son1' and 'father ' property . 'son3' is rich
  phone2 = "broken iphone"
  house = "Broken House"
  pc = "Broken Laptop"
  

ason3 = son3()

print(ason3.business)
print(ason3.pc2)

print()
print()








print("# 62  =  Python Hybrid And Hierarchical Inheritance.")






















