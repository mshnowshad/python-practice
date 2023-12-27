print()

print("==================== I Created an Auto Birthday Wisher using Python======================")
print()




import pandas as pd #পান্ডাস লাইব্রেরি আমদানি করা হয়, যা ডেটা বিশ্লেষণ এবং ম্যানিপুলেশনের জন্য ব্যবহৃত হয়।

import datetime    #  তারিখ এবং সময়ের সাথে কাজ করার জন্য datetime লাইব্রেরি আমদানি করা হয়।

import smtplib    #  এসএমটিপি (সিম্পল মেইল ট্রান্সফার প্রোটোকল) লাইব্রেরি আমদানি করা হয়, যা ইমেল পাঠানোর জন্য ব্যবহৃত হয়।

import os    # অপারেটিং সিস্টেমের সাথে ইন্টারঅ্যাক্ট করার জন্য os লাইব্রেরি আমদানি করা হয়।




os.chdir(r"D:\MyData\Business\code playground\Python Practice Programs\birthday wisher")   #এই লাইনটি বর্তমান কাজের ডিরেক্টরিটিকে নির্দিষ্ট ফোল্ডারে সেট করে।
# os.mkdir("testing") 


# Enter your authentication details
GMAIL_ID = ''    #> এই লাইনগুলি আপনার জিমেইল আইডি এবং পাসওয়ার্ড সংরক্ষণ করার জন্য স্থানধারক। আপনার প্রকৃত ইমেল এবং পাসওয়ার্ড দিয়ে এগুলি পূরণ করতে হবে।    
GMAIL_PSWD = ''


def sendEmail(to, sub, msg):   #এই ফাংশনটি ইমেল পাঠানোর জন্য সংজ্ঞায়িত করা হয়। এটি নিম্নোক্ত কাজ করে:
    
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )   #ইমেল পাঠানোর বিষয়বস্তু প্রিন্ট করে।
    s = smtplib.SMTP('smtp.gmail.com', 587)   #> SMTP সার্ভার (জিমেইলের জন্য smtp.gmail.com) এর সাথে সংযোগ স্থাপন করে।
    
    s.starttls()     #>>TLS (Transport Lay er Security) শুরু করে।
    s.login(GMAIL_ID, GMAIL_PSWD)   #>>> আপনার জিমেইল আইডি এবং পাসওয়ার্ড দিয়ে লগইন করে।
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")   #>>>> নির্দিষ্ট ঠিকানা, বিষয় এবং বার্তা সহ ইমেল পাঠায়।
    s.quit()    #>>>> সার্ভার সংযোগ বিচ্ছিন্ন করে।
    





if __name__ == "__main__":    #> এই ব্লকটি নিশ্চিত করে যে কোডটি সরাসরি চালানো হলেই এক্সিকিউট হবে, অন্য কোনো মডিউল থেকে আমদানি করা হলে নয়।
    #just for testing
    # sendEmail(GMAIL_ID, "subject", "test message")
    # exit()

    df = pd.read_excel("data.xlsx")  #>  এই লাইনটি "data.xlsx" নামক এক্সেল ফাইল থেকে ডেটা পড়ে এবং একটি পান্ডাস ডেটাফ্রেম (df) তৈরি করে।
    # print(df)
    
    today = datetime.datetime.now().strftime("%d-%m")  #>  আজকের তারিখ "%d-%m" আকারে (দিন-মাস) সংরক্ষণ করে।
    yearNow = datetime.datetime.now().strftime("%Y")   #>  বর্তমান বছর "%Y" আকারে সংরক্ষণ করে।
    # print(type(today))
    
    writeInd = []   #> একটি খালি তালিকা তৈরি করে যেখানে জন্মদিনের শুভেচ্ছা পাঠানোর পরে আপডেট করার জন্য সূচীগুলি সংরক্ষণ করা হবে।
    for index, item in df.iterrows():   #>  ডেটাফ্রেমের প্রতিটি সারির উপরে লুপ করে
        # print(index, item['Birthday'])
        
        bday = item['Birthday'].strftime("%d-%m")   #> . জন্মদিনের তারিখকে "%d-%m" আকারে বিন্যাস করে।
        # print(bday) 
        
        
        if(today == bday) and yearNow not in str(item['Year']):   #> যদি আজকের তারিখ জন্মদিনের তারিখের সাথে মিলে যায় এবং বর্তমান বছরটি ইতিমধ্যেই 'Year' কলামে না থাকে, তাহলে:
            
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])   #>  জন্মদিনের শুভেচ্ছা ইমেল পাঠায়।
            writeInd.append(index)  #> লিস্টে সূচীটি যোগ করে।



    # print(writeInd)
    for i in writeInd:   #> writeInd লিস্টের প্রতিটি সূচীর উপরে লুপ করে
        
        yr = df.loc[i, 'Year']    #>  ডেটাফ্রেমের নির্দিষ্ট
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)   # এটি একই সারিতে 'Year' কলামের মান আপডেট করে। এটি বিদ্যমান বছর yr কে কমা, একটা স্পেস এবং বর্তমান বছর yearNow এর স্ট্রিং এর সাথে যুক্ত করে।
        # print(df.loc[i, 'Year'])

    # print(df) 
    df.to_excel('data.xlsx', index=False)     # এই লাইনটি df DataFrame-কে আবার data.xlsx নামক এক্সেল ফাইলে লিখে ফেলে।
                                              #> index=False: এটি নিশ্চিত করে যে ফাইলে লেখা হবে না ডেটাফ্রেমের প্রতিটি সারির সীrial নম্বর (index)।















































print()
