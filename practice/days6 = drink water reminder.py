print()



print("====================I Created a Drink Water Notification Reminder app in Python ===================")
print()



import time   #> প্রথম লাইনে import time লাইব্রেরি ইম্পোর্ট করা হয়েছে, এটি সময়ের সাথে সম্পর্কিত কাজের জন্য ব্যবহৃত হয়।

from plyer import notification #> from plyer import notification লাইব্রেরি থেকে notification মডিউল ইম্পোর্ট করা হয়েছে, এটি ডেস্কটপ নোটিফিকেশন তৈরি করার জন্য ব্যবহৃত হয়





if __name__ == "__main__":   #>  লাইন নিশ্চিত করে যে কোডটি সরাসরি চালানো হলেই শুধুমাত্র চলবে, অন্য স্ক্রিপ্ট থেকে ইম্পোর্ট করা হলে চলবে না।

    while True:    #> while True: লাইন একটি অসীম লুপ তৈরি করে, এর মানে হল কোডটি বারবার চলতে থাকবে।

        notification.notify(  #> notification.notify(...) লাইন একটি ডেস্কটপ নোটিফিকেশন তৈরি করে। এর মধ্যে কয়েকটি প্যারামিটার আছে

        title = "Please Drink Water Now! Talk of Your Caring Person!.",   #title: "Please Drink Water !" - নোটিফিকেশনের শিরোনাম।
        message = "Drink is vary helpfull for Human body 'i reminde you' . Thank you so much",    #message:  নোটিফিকেশনের বার্তা।
        app_icon = "F:\Python Folder\Hablu Programmer\practice\Iconpath\icon2.ico",   # app_icon: - নোটিফিকেশনে প্রদর্শিত হবে এমন আইকনের ফাইলের পথ। (আপনার নির্দিষ্ট পথ ব্যবহার করুন)
        timeout = 10,   #timeout: 1 - কতক্ষণ পর নোটিফিকেশন স্বয়ংক্রিয়ভাবে বন্ধ হবে (সেকেন্ডে)।
        
	    ) 
        
        time.sleep(60*10)   #>> time.sleep(60*5) লাইন কোডের কার্যক্রম 5 মিনিট (60 সেকেন্ড x 10) বিরতি দেয়। এর মানে হল প্রতি 5 মিনিটে পর পর একটি নোটিফিকেশন তৈরি হবে।
                              #>>> এই কোডটি প্রতি 5 মিনিটে একটি ডেস্কটপ নোটিফিকেশন দেখাবে যাতে আপনাকে পানি পান করার কথা মনে করিয়ে দেয়। 

    
    
#> how run python in the background   > open the folder of your this code   >open terminal and enter the "pythonw .\<Pythonfilename.py>"





print()



print(" #  Congratulation! You complete this Notification Reminder Project. ")

























print()

























print()


