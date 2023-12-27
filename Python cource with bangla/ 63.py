""" Python Iterator """

print("#63  = Python Iterator")

#> পাইথনে, Iterator হলো একটি অবজেক্ট যা ডেটা স্ট্রীম প্রতিরূপ করে এবং ঐ ডেটা উপর ইটারেশন করার সুযোগ সৃষ্টি করে।   
#>>  এটি দুটি মেথড, "iter()" এবং "next()" ইমপ্লিমেন্ট করে

print()






list1 = ['harry','busta rhymes',1000 ,211121,3212,521212,612,7111,822,101] #> this is a base 



#> Example with loop
"""
for i in list1:
  print(i)  #> return 'list er sob item access kore che / "iterate" kore  che
"""





iter1 = iter(list1)

#print(iter1)          #> return "<list_iterator object at 0x7f0f0f0f0f0f>"  because we can't use "next()" method on the print


print("> your 1 st item : ",next(iter1))  #> jotho bar ei rokom print korbo , thotho bar ei rokom 1 tar por 1 ta item print korbe
print("> Your 2nd item is : ",next(iter1))

#> same as
print("> use another type : ",iter1.__next__()) #> ei vabe  o iter use kora jay.. but "line : 21" is the best
print()

#>Bangla rules:
print(">Bangla rules  : ",list1[0])  #> aktu hard



































































