"""Python Polymorphism"""
print("#> 77 = Python Polymorphism")

#> পলিমরফিজম হল পাইথনে ব্যবহৃত একটি শব্দ যা একটি বস্তুর একাধিক রূপ নেওয়ার ক্ষমতা বোঝায়। শব্দটি দুটি স্বতন্ত্র পদ থেকে উদ্ভূত: Poly, যার অর্থ অসংখ্য, এবং morphs, যার অর্থ রূপ।

#Example:
#>>>> amr baba business korthese abr job o korthe parbe
print()






class vehicles: #> ei 'object' diya inheritance kore many object mananu jabe
  
  def __init__(self,model,brand,color,design):
    self.model = model  #> this is public
    self.brand = brand
    self.color = color
    self.design = design


class car(vehicles):
  pass #> ei 'pass' na dile 'error' dibe

poly1 = car("Mustang","Ford","Black","Sports")

print("> Your cars brand is :", poly1.brand)

print("\n > Your cars Model is :", poly1.model)

print("\n >> Your cars color is :",poly1.color)




print()

print()





print("# Another Example:")


class plane(vehicles):
  pass


pl1 = plane("Lion","Luxury","white","Super Luxuriess ")

print("\n> Your plan model is :",pl1.model)


print("\n >> Your plan brand is :",pl1.brand)





  














