""" Python DateTime """


print("#65 Python Date and Time .")


#>> 
r"""

a.strftime(%a)  =	  Weekday, short version                                        return =>	Wed 	

a.strftime(%A)  = 	Weekday, full version 	                                      return => Wednesday 	

a.strftime(%w) 	=   Weekday as a number 0-6, 0 is Sunday                           return => 	3 	

a.strftime(%d)  =  	Day of month 01-31 	                                            return => 31 	

a.strftime(%b) 	=   Month name, short version 	                                 return => Dec 	

a.strftime(%B)  = 	Month name, full version 	                                   return => December 	

a.strftime(%m)  = 	Month as a number 01-12 	                                 return => 12 	

a.strftime(%y)   = 	Year, short version, without century 	                      return => 18 	

a.strftime(%Y)   =   	Year, full version 	                                      return => 2018 	

a.strftime(%H)   =    	Hour 00-23                                                return => 	17 	

a.strftime%I     =  	Hour 00-12 	                                               return => 05 	

a.strftime(%p)   = 	AM/PM 	                                                      return => PM 	

a.strftime(%M)   =  	Minute 00-59 	                                            return => 41 	

a.strftime(%S)   =  	Second 00-59 	                                           return => 08 	

a.strftime(%f)   =  	Microsecond 000000-999999 	                               return => 548513 	

a.strftime(%z)   = 	UTC offset 	                                                 return => +0100 	

a.strftime(%Z)   =  	Timezone 	                                                     return => CST 	

a.strftime(%j)   = 	Day number of year 001-366 	                                     return => 365 	

a.strftime(%U)  = 	Week number of year, Sunday as the first day of week, 00-53 	    return => 52 	

a.strftime(%c) 	 = Local version of date and time 	Mon Dec 31 17:41:00                 return => 2018 	

a.strftime(%C0  =  	Century 	                                                          return => 20 	

a.strftime(%x)  =  	Local version of date 	                                             return => 12/31/18 	
  
a.strftime(%X)  =  	Local version of time 	                                            return => 17:41:00 	

a.strftime(%%)  = 	A % character 	                                                     return => % 	

a.strftime(%G)  = 	ISO 8601 year 	                                                    return => 2018 	

a.strftime(%u)  =>  	ISO 8601 weekday (1-7) 	                                           return => 1 	

a.strftime(%V)  =   ISO 8601 weeknumber (01-53) 	                                       return => 01




"""

import datetime

a = datetime.datetime.now()
print(a)

print()






print("# this a 'strftime()' method")

print('this week is :',a.strftime("%A")) #> Weekday, full version

print('your date is :', a.strftime("%x"))























