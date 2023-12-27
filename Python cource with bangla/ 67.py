
"""   Python RegExpression """
"""
> A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. = একটি RegEx অক্ষরের একটি ক্রম যা একটি অনুসন্ধান প্যাটার্ন গঠন করে।

> RegEx can be used to check if a string contains the specified search pattern.  = একটি স্ট্রিং নির্দিষ্ট অনুসন্ধান প্যাটার্ন রয়েছে কিনা তা পরীক্ষা করতে RegEx ব্যবহার করা যেতে পারে।




"""
print("#67 =  Python Regular Expression")
print()


#text = "python is the high level programming language , python used in web dev, data science, AI , Machine learning"
#print("is the 'data' available in text ? Ans : ", "data" in text)

print()
print()





import re

text1 = "The rain in Spain"
print(text1.capitalize())

#Find all lower case characters alphabetically between "a" to 'm' = "a" থেকে 'm' এর মধ্যে বর্ণানুক্রমিকভাবে সমস্ত ছোট হাতের অক্ষর খুঁজুন

a = re.findall('[a-m]',text1) #> return ['h', 'e', 'a', 'i', 'i', 'a', 'i']  #> 're.findall()' is a function and  	"[a-m]" is a 'Metacharacter'

print(a)
print()
print()





print("#> This is a another type but same .")
print()

import re

txt1 = "Hi, i am nowshad. i a, beginner in python programming"
pattern1 = "[a-n]"
b = re.findall(pattern1, txt1 )

print(b)
print()
print()





import re

are1 = "This is a regex tutorial "

pattern2 = '^This'
c = re.findall(pattern2,are1)

if c:
  print("> Yes , 'This' is in the are1 variable ") #return line : 68 . because is the True

else :
  print("> No unvaiable. Thank you ")


print()


















#> Meta Character 
print("#> Meta Character : ")

r"""

[] 	A set of characters 	      =>   "[a-m]"  #example "line : 33 "

^ 	Starts with 	       =>  "^hello" 	   #example 'line ; '

\ 	Signals a special sequence (can also be used to escape special characters) 	  =>  "\d"

. 	Any character (except newline character) 	   =>  "he..o" 	

$ 	Ends with 	        =>   "planet$" 	

* 	Zero or more occurrences       => 	"he.*o" 	

+ 	One or more occurrences 	     =>    "he.+o" 	

? 	Zero or one occurrences 	      => "he.?o" 	

{} 	Exactly the specified number of occurrences 	=>   "he.{2}o" 	

| 	Either or 	           => "falls|stays" 	

() 	Capture and group  

"""
print()
print()























