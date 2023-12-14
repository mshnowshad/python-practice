"""Python File Open"""

print("#> 69 = Python file open")

"""


"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


"""











print("# file create with python code")



file2 = open("create1.txt","w")  

file2.write("hi , are you Nabile?")
print()




print()

#file1 = open("create3.txt","x")      #> RETURN Error because 1 bar create korse abr run korle error dibe.. > line : 30 'rules' follow kora balo

print()




print()
print()



read1 = open("read.txt","r")

print(read1.read())


try:
  print(read1.write())
except:
  print("Error")


print()
print()
print()







"""Python File Write """

print("#> 70 = Python file Write")
print()



print("#> Write file method:")


"""

To create a new file in Python, use the open() method, with one of the following parameters:

"w" - Write - will create a file if the specified file does not exist


"""
print()




write1 = open("write1.txt","w")  #> "w" is a 'parameter'

a = write1.write("hi brooo") #> ja kisu lekvo oita write hobe
print()



write1 = open("write1.txt","r")  #> eita diya file er element gula show hobe
b = write1.read()
print(b)

print()






#> "a" - Append - Opens a file for appending, creates the file if it does not exist

append1 = open("write1.txt","a")

app1 = append1.write(", Append this line. ") #> eita jotho bar lekbo oita 'add ' hobe . but line remove hobe nay

print()
print()
print()






#> Python File Remove 

print("#71 = Python File Remove ")
print()




open("newremovefile.html","w")

import os    #>> 'os' is a "module" for Remove File

os.remove("newremovefile.html")  



#Delete Folder

#> To delete an entire folder, use the "os.rmdir()" method

import os

os.rmdir("maintingfile")  #> 'os.rmdir(<foldername>)'  > return error because folder allready deleted





















































































