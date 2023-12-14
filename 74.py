"""Python Constructor"""
print("#74 = Python Constructor")
"""

In Python programming, a constructor is a special method that is automatically called when an object of a class is created. It is used to initialize the attributes of the object. The constructor method is named __init__ (with double underscores on both sides).


পাইথন প্রোগ্রামিংয়ে, কনস্ট্রাক্টর হলো একটি বিশেষ মেথড যা একটি ক্লাসের অবজেক্ট তৈরি হতে সময় স্বয়ংক্রিয়ভাবে কল করা হয়। এটি অবজেক্টের গুণগুলি একত্রিত করতে ব্যবহৃত হয়। কনস্ট্রাক্টর মেথডটির নাম হলো __init__ (উভয় পাশে ডাবল আন্ডারস্কোর)।

https://pynative.com/wp-content/uploads/2021/07/types_of_constructor.png


python constructor

> non parameter
> parameter

"""


print()




print("this is non Constructior")
"""

class parentInfo:
  def eshansF(self,name,age):
    txt = f"my name is {name}, my age is {age}"
    print(txt)
    
  
    
    
b = parentInfo()  #> code ke komiye anar jonno "constructor use korthe pari"

b.eshansF("Nowshad",20)

"""



print()


print("#> Parameterize Constructoor")
print()


class parameter2:
  def __init__(self,res,gpa) :
    print(f"> My result is {res}, My GPA is {gpa}")
    

pa = parameter2("so good", 3.40)

pa = parameter2("so exellent", 5 )


