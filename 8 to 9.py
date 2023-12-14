



""" python string"""

print("## Python string:")

print()



""" 9.1 = String formatting"""
print('this is a String formatting')

sf1 = 80
sf2 = 21
user = 'Hablu'

print(f'this is my super number :{sf1 + sf2}') #=> 'f' - is the "string format"


print(f'Your name is {user}')
print()


"""Multiline Strings
#You can assign a multiline string to a variable by using three quotes:
print('multiline string:')"""

multistr1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(multistr1)

print()







print("#> Check String")
#To check 'if' a certain phrase or character is present in a string, we can use the keyword 'in'
print("1 Check String:")

Checktxt = "The best things in life are free!"
print("free" in Checktxt)

print()






print("#> Slicing string")
##>> You can return a range of characters by using the slice syntax.
##>> Specify the start index and the end index, separated by a colon, to return a part of the string.



## >> Get the characters from the start to position 5 (not included):
slicing1 = "Hello World!"
print("your slicing string", slicing1[:5])
print()

#Negative Indexing
#>>> Use negative indexes to start the slice from the end of the string:


slicing2 = "Hello, World!"
print(slicing2[-6:-1])
print()









###   Python - Modify Strings
print("# python modify string:")


#>>> The upper() method returns the string in upper case:

modifystr1 = "Hello, World!"
print("1 .The upper() method: ",modifystr1.upper())

print()

##>> the capitalize() method return the first string is upper : 

txt0 = "hello, and welcome to my world."

x = txt0.capitalize()

print ("> used the 'capitalize()' method : ",x)

 
print()




#>>> The lower() method returns the string in lower case:

modifystr2 = "Hello, World!"
print("The lower() method: ",modifystr2.lower())

print()





#>> The replace() method replaces a string with another string:

modifystr3 = "Hello, World!"
print("The replace() method : ",modifystr3.replace("H", "J"))





#The split() method splits the string into substrings if it finds instances of the separator:

split1 = "Hello, World!"
print(split1.split(",")) # returns ['Hello', ' World!']






## Escape Characters
## Other escape characters used in Python:

r"""
\'  = Single Quote	
\\	= Backslash	
\n	= New Line	#> line : 134
\r	= Carriage Return	#> line : 134
\t  = Tab	 #> line : 143
\b	= Backspace	
\f	= Form Feed	
\ooo	= Octal value	
"\xhh	" = "Hex value  "    """


print()

print("#> New line '\n' :")

print("#Example : ")

txt1 = "Hello\nWorld!"
print(txt1) 

print()


print("#> Tab '\t' :")
print("Exaple = ")

txt2 = "Hello\tWorld!"
print(txt2)  #> return Hello"<space>"World  # this space is the called 'tab  \t'





























































