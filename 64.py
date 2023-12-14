""" Python Scope """

print("#64 Python Scope ")

#> Python scope is 2 type . > global and local
#> পাইথন স্কোপ নির্ধারণ করে যে আপনার প্রোগ্রামে একটি নাম কোথায় দৃশ্যমান হবে। পাইথন স্কোপগুলি অভিধান হিসাবে প্রয়োগ করা হয় যা বস্তুর নাম ম্যাপ করে। এই অভিধানগুলোকে সাধারণত নামস্থান বলা হয়।
print()






print("# Local Scope .")
print()



def mylocalarea(a1):
  a = a1       #> this is a "local variable"
  b = 'Loncgat'
  print(a)

mylocalarea("i am local area boy")
print()
print()









print("#Global Scope .")
print()


a = "this is Global variable "
def myglobalscope():
  print(a)

myglobalscope()

































