print()



print("========================== I Created an Automatic Folder Cleaner in Python ====================")

print()


import os

files1 = os.listdir()  #> এই লাইনটি একটি নির্দিষ্ট ফোল্ডারের মধ্যে থাকা সকল ফাইল এবং ফোল্ডারের নামের তালিকা সংগ্রহ করে।



def createIfnotexist(filename): #> এই লাইনটি createIfnotexist নামে একটি ফাংশন তৈরি করে। এই ফাংশনটি একটি আর্গুমেন্ট গ্রহণ করে, যেটা ফোল্ডারের নাম।

    if not os.path.exists(filename):  #> এই লাইনটি পরীক্ষা করে যে নির্দিষ্ট ফোল্ডারটি ইতিমধ্যেই আছে কি না।
        os.makedirs(filename)  #> এই ফাংশনটি ফোল্ডার তৈরি করার জন্য ব্যবহৃত হয়। 'os.makedirs'  ... 'filename' is argument line no: 33 to 36 showed


def move(folderName,files1):

    for file in files1:  #> এই লাইনটি ফাইলের তালিকায় থাকা প্রতিটি ফাইলের জন্য একটি লুপ শুরু করে। প্রতিটি পুনরাবৃত্তিতে, file ভ্যারিয়েবলটি বর্তমান ফাইলের নাম ধারণ করবে।
        os.replace(file,f"{folderName}/{file}")  #> file: এটি বর্তমান ফাইলের নাম, যা স্থানান্তর করা হবে।
                                                 #>>  f"{folderName}/{file}": এটি নতুন ফাইলের পাথ তৈরি করে, যাতে ফোল্ডারের নাম এবং ফাইলের নাম একত্রিত করা হয়।






createIfnotexist("Images")    
createIfnotexist("Docs")
createIfnotexist("Medias")
createIfnotexist("Others")




imgExts = ['.png','.jpg','jpeg']
# images = [file for file in files1 if os.path.splitext(file)[1].lower() in imgExts]   #> explain in line No: 45 to 48   ### "same as like line: 44 to 50"

images = []     
for file in files1:
    if os.path.splitext(file)[1].lower() in imgExts:   #> os.path.splitext(file): এই ফাংশনটি ফাইলের নামকে দুটি অংশে বিভক্ত করে: মূল নাম এবং এক্সটেনশন।
                                                       #>> [1]: এটি দ্বিতীয় অংশটিকে গ্রহণ করে, যেটা হচ্ছে ফাইলের এক্সটেনশন।
                                                       #>>> .lower(): এটি এক্সটেনশনকে ছোট হাতের অক্ষরে রূপান্তরিত করে, যাতে বড় হাতের ও ছোট হাতের অক্ষরের পার্থক্য না হয়।
                                                       #>>>> in imgExts: এটি পরীক্ষা করে যে এক্সটেনশনটি imgExts তালিকায় আছে কি না, যেটা ছবির ফাইল এক্সটেনশনগুলোর একটি তালিকা।
        images.append(file)





docExts = [".txt",".docx","doc",".pdf"]
docs = [file for file in files1 if os.path.splitext(file)[1].lower() in docExts]   #> explain in line No: 45



mediaExts = [".mp4",".mp3",".flv"]
medias = [file for file in files1 if os.path.splitext(file)[1].lower() in mediaExts]   #> explain in line No: 45

# others  = []
# for file in files1:
#     ext0 = os.path.splitext(file)[1].lower()
#     if (ext0 not in mediaExts) and (ext0 not in docExts) and (ext0 not in imgExts):
#         others.append(file)

pythonfile = [".py"]
python = [file for file in files1 if os.path.splitext(file)[1].lower() in pythonfile]   #> explain in line No: 45




# print(others)


move("Docs",docs)
move("Images",images)
move('Medias',medias)
# move('Others',others)
move("Pythonfile",python)





print("# Congratulation ! , You Done this.")



















































print()
