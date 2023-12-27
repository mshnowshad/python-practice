
""" Python Lambda """

print("#> 56 = Python Lambda .")
print()

"""
> Python প্রোগ্রামিং ভাষায় lambda হলো একটি অ্যাননিমাস ফাংশন, >> যা একটি সিঙ্গল এক্সপ্রেশন দ্বারা সংজ্ঞায়িত হয়। 

>> এটির মূল উদ্দেশ্য হলো একটি ছোট ফাংশন যা অন্য একটি প্রোগ্রামের মধ্যে কোনো নাম দেওয়া ছাড়াই ব্যবহার করা।

এটি ধারাবাহিক স্যান্ট্যাক্সের সাথে কাজ করে এবং এটি একটি এক্সপ্রেশন হিসেবে অব্যবহৃত হয়ে থাকে, যাতে এটি সরাসরি একটি এক্সপ্রেশন হিসেবে কাজ করে এবং কোন নাম প্রয়োজন নেই।  """ 


print()


x = lambda a, b : a + b #>> unlimited "parameter" use korthe parbo  > "a" is a 'parameter'

print("> Used 'lambda' : ",x(5, 6)) #> same as like 'function'
print()



print("Example with 'Function :'")


def myfunction( a , b):
  sum = a + b 
  print("> Example : ",sum)
myfunction(5 , 6)

print()

print()





print("#> Exercise ")

#>Create a lambda function that takes "one parameter (a)" and returns it.


x = lambda a : a
print(x(101),"Days of code , hahaha ")














