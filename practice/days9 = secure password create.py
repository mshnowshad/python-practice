print()


print("================================I create secure password using Python ========================")
print()


 
SECURE = (("S", "$"), ("and", "&"), ("A", "@"), ("i", "1"), ("o", "0"), ("E", "3"), ("N", "n"))   #> ei jay gay jekono character use korthe parbo
 

def securepassword(password):
    user = password  # এখানে user ভ্যারিয়েবলটিকে সংজ্ঞায়িত করা হলো
    
    for a,b in SECURE:  #> ফাংশনের ভেতরে for a, b in SECURE: লাইনটি দিয়ে SECURE তালিকার প্রতিটি অক্ষরের জোড়ার উপরে কাজ করা হচ্ছে।
        user = user.replace(a,b)   #>> user = user.replace(a, b) লাইনটি দিয়ে পাসওয়ার্ডের ভেতরে থাকা a অক্ষরগুলোকে b অক্ষর দিয়ে বদলে দেওয়া হচ্ছে।
    return user  #> return user লাইনটি দিয়ে পরিবর্তিত পাসওয়ার্ডটি ফেরত দেওয়া হচ্ছে।
    # pass
    






if __name__ == '__main__':
    # pass
    user = input(">Enter your password: ")
    user = securepassword(user)
    print(f"#>> Your secure password is '{user}'")












print()


# print("==================CodeWithHarry=======================")



# print()



# SECURE = (('s', '$'), ('and', '&'), 
#             ('a', '@'), ('o', '0'), ('i', '1'),
#             ('I', '|'))

# def securePassword(password):
#     for a,b in SECURE:
#         password = password.replace(a, b)
#     return password

# if __name__ == "__main__":
#     password = input("Enter your password : ")
#     password = securePassword(password)
#     print(f"Your secure password is > {password} <")





















print()
