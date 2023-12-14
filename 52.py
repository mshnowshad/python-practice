
""" Break and Continue """

print("#> 52 = Break and Continue .")


""""""

print()





print("# Break :")


break1 = ["hablu","tablu","Mango ", 101 , 0.111, "hi"]

for i in break1:
  if i == 101 :
    break
  print("Used 'break' method :",i) # '101' not printed because '101' condition er bithor raka. >> "continue" kethre ei rokom hobe na. 

print()



print("#> Continue : ")



continu1 = break1.copy()

#print(continue1)

for x in continu1 : 
  if x == "tablu":
    continue
  print("Used 'continue ' method : ", x) #> 'tablu' not printed because 'tablu ' in the condition .>> 'tablu ' sara sob kisu print hobe. 

print()








































































