print()


print("=====================Create a currency Converter make with own code ===========================")

print()

with open("filenew1.txt") as f:  ##> "open()" korata 'f' variable convert korse
	lines1 = f.readlines() # ফাইলটাকে পড়ে এবং প্রতিটা লাইনকে একটা লিস্টে রাখে, যার নাম lines।
	
# print(lines1)
	


dic0 = {}

for line in lines1:
	parsed = line.split("\t")#> eijay gay "\t" use kora oise koron outa nij theke bujthe hobe . 'Search what is split() in python '
	
	dic0[parsed[0]] = parsed[1]  #> ei jaygay dictionary the convert korse because {"Argentine Peso	","1.115338","0.896589"}  to {"Argentine Peso"	: "1.115338"} the convert korse. >> "Argentina" is a 'key' and  "1.11533" is 'value pairs'


# print(dic0)

amount0 = int(input("> enter YOur rupe : "))

print('Enter the name of th currency you want to covert Your amout to. Available Options : ')
for item in dic0.keys():  #> ei jaygay 'dic0' all 'key' gula upor for loop chalaisi because options dekar jonno
	print(item)




currenccy = input("please enter one of these values : ")
print()
print(f"#>>>>> {amount0} Indian rupe  is equal to {amount0 * float(dic0[currenccy])}")  #> amount *float(currencyDict[currency]) এই গণনা করে যে কতটা বিদেশী মুদ্রা পাওয়া যাবে (ইনপুট অঙ্ক x এক্সচেঞ্জ রেট)।










print()
print()
print('=================================CodewithHarry===========================================')
print()





# with open('create1.txt') as f:   #>  একটা ব্লক তৈরি করে যেটা ফাইলটাকে খুলে কাজ করে, তারপর অটোমেটিক্যালি বন্ধ করে দেয়।
	
# 	lines = f.readlines()   #>  ফাইলটাকে পড়ে এবং প্রতিটা লাইনকে একটা লিস্টে রাখে, যার নাম lines।


# currencyDict = {}
# for line in lines:   #> প্রতিটা লাইনের জন্য একটা লুপ চালায়, লাইনগুলো lines লিস্টে থাকে।
	
# 	parsed = line.split("\t") #>> ফাইলের প্রতিটা লাইনকে ট্যাব (\t) দিয়ে আলাদা করে এবং ফলাফলগুলো parsed নামের লিস্টে রাখে।
	
# 	currencyDict[parsed[0]] = parsed[1]   #> parsed লিস্টের প্রথম এলিমেন্ট (যা মুদ্রা কোড) কে ডিকশনারি currencyDict এর কি হিসেবে যোগ করে এবং দ্বিতীয় এলিমেন্ট (যা এক্সচেঞ্জ রেট) কে ভ্যালু হিসেবে যোগ করে।



# amount = int(input("Enter amount:\n"))   #> ইউজারের কাছ থেকে একটা নাম্বার ইনপুট নেয় এবং তাকে ইন্টেজারে (পূর্ণ সংখ্যা) পরিবর্তিত করে, যার নাম amount।

# print("Enter the name of the currency you want to convert this amount to? Available Options:\n")  #> ইউজারের কাছ থেকে জানতে চায় যে সে কোন মুদ্রায় অঙ্কটি রূপান্তর করতে চায়।

# [print(item) for item in currencyDict.keys()]    #> ডিকশনারি currencyDict এর সব কি তत्वগুলো লিস্টে প্রিন্ট করে, যা উপলব্ধ মুদ্রা অপশনগুলো দেখায়।

# currency = input("Please enter one of these values: \n")  #> ইউজারের কাছ থেকে উপলব্ধ অপশনগুলোর মধ্যে থেকে একটা মুদ্রা কোড ইনপুট নেয়, যার নাম currency।


# print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")  #>> একটা স্ট্রিং প্রিন্ট করে যা দেখায় যে কত ইনভিট রুপি (INR) কতটা অন্য মুদ্রায় রূপান্তর হয়েছে।







print()






 












print()

print("==================explain with AI =====================")

print()


##১. ফাইল পড়া:

##>> with open('currencyData.txt') as f: একটা ব্লক তৈরি করে যেটা ফাইলটাকে খুলে কাজ করে, তারপর অটোমেটিক্যালি বন্ধ করে দেয়।
##>> f.readlines() ফাইলটাকে পড়ে এবং প্রতিটা লাইনকে একটা লিস্টে রাখে, যার নাম lines।




### ২. মুদ্রা ডিকশনারি তৈরি:

##>> currencyDict = {} একটা খালি ডিকশনারি তৈরি করে, যার নাম currencyDict।

##> for line in lines: প্রতিটা লাইনের জন্য একটা লুপ চালায়, লাইনগুলো lines লিস্টে থাকে।

##> parsed = line.split("\t") ফাইলের প্রতিটা লাইনকে ট্যাব (\t) দিয়ে আলাদা করে এবং ফলাফলগুলো parsed নামের লিস্টে রাখে।

#> currencyDict[parsed[0]] = parsed[1] parsed লিস্টের প্রথম এলিমেন্ট (যা মুদ্রা কোড) কে ডিকশনারি currencyDict এর কি হিসেবে যোগ করে এবং দ্বিতীয় এলিমেন্ট (যা এক্সচেঞ্জ রেট) কে ভ্যালু হিসেবে যোগ করে।




##৩. অঙ্ক এবং মুদ্রা গ্রহণ:

#> amount = int(input("অঙ্ক লিখুন:\n")) ইউজারের কাছ থেকে একটা নাম্বার ইনপুট নেয় এবং তাকে ইন্টেজারে (পূর্ণ সংখ্যা) পরিবর্তিত করে, যার নাম amount।

#> print("কিস মুদ্রায় এই অঙ্ক রূপান্তর করতে চান? উপলব্ধ অপশন:\n") ইউজারের কাছ থেকে জানতে চায় যে সে কোন মুদ্রায় অঙ্কটি রূপান্তর করতে চায়।

#> [print(item) for item in currencyDict.keys()] ডিকশনারি currencyDict এর সব কি তत्वগুলো লিস্টে প্রিন্ট করে, যা উপলব্ধ মুদ্রা অপশনগুলো দেখায়।
#> currency = input("দয়া করে এইগুলোর মধ্যে থেকে একটা মূল্য কোড লিখুন:\n") ইউজারের কাছ থেকে উপলব্ধ অপশনগুলোর মধ্যে থেকে একটা মুদ্রা কোড ইনপুট নেয়, যার নাম currency।



#3৪. অঙ্কের রূপান্তর:

##>> print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}") একটা স্ট্রিং প্রিন্ট করে যা দেখায় যে কত ইনভিট রুপি (INR) কতটা অন্য মুদ্রায় রূপান্তর হয়েছে।

#>> f-স্ট্রিং ব্যবহার করে, আমরা অঙ্ক, এক্সচেঞ্জ রেট এবং ফাইনাল অঙ্কটিকে সরাসরি স্ট্রিং এর মধ্যে অন্তর্ভুক্ত করতে পারি।

#> amount *float(currencyDict[currency]) এই গণনা করে যে কতটা বিদেশী মুদ্রা পাওয়া যাবে (ইনপুট অঙ্ক x এক্সচেঞ্জ রেট)।


#  এইভাবে, প্রোগ্রামটি ইউজারের কাছ থেকে তথ্য নেয় এবং উপলব্ধ বিদেশী মুদ্রায় ইনভিট রুপি (INR) এর অঙ্ককে রূপান্তর করে।





































print()