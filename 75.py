"""#75 Python Introducing All About Method """

print("#75 Python Introducing All About Method :")


print()


print()



class personalme:   #> 'personalme' is a class 'object'
  
  def __init__(self,name):
    print(f"> hello i am {name}")


  
  @classmethod  #> "@classmethod" this is not changeable . eita poriborthe onno ta dile 'error' dibe 
  
  def personality(name): #> "name " is parameter . this is changeable but ei jaygay parameter na dile "error" dibe
    print(">> this is a 'personality' method.")


all1 = personalme("Nowshad")
personalme.personality()
  


print()
print()




print("#>Another Example:")
print()

class method1:
  def InstanceMethod(self):
    print("hello Instance method.")

  
  @classmethod
  
  def classmethod(cls,name): #> "cls" na diye onno jekunu parameter use kora jay, but na dile error dibe . Another way "line : 76 ,77"

    
    print(f">> this is a mension '{name}' :")




exam1 = method1()#> "method1()" is the class 'object'



exam1.InstanceMethod() #> "exam1" na dile ei object a 'error' dibe
print()

method1.classmethod("classMethod")  #> '"method1"' ja object dore call korar por o 'error ' dibe na because "line : 39 to 40"
print()


print()
print()
print()

print("#> this is a 'staticmethod' :")
print()




class method3:
  def Method3(name):
    print(f"> My name is {name}")

  @staticmethod
  def StaticMethod(name2):  #> "@staticmethod" use korle kunu parameter use na korle o chole
    
    print(f"> My name is a Duo, > This is a {name2}, ")





stat = method3()
method3.StaticMethod("Static Method")
print()











































