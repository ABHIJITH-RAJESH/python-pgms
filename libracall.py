import libra
# inbuilt msthematical functions, some common math functions 
import math
# built in matehmatical function min max absolute abosulte converts negative value to positive ,power 
import datetime #to deal with date time 
print(math.pi)
print(math.sqrt(16))
print(math.ceil(2.1))
print(math.floor(2.1))
print(math.factorial(5))
print(pow(5,7)) 
print(abs(-56.76)) 
print(min(5,6,76,23,344)) 
print(max(5,6,76,23,344)) 
print(libra.add(5,4))
print(libra.sub(5,4))
print(libra.multi(5,4))
print(libra.divi(5,4))

# date time 
# display date and time 
c=datetime.datetime.now()

# strftime format date 
print(c.strftime("%A")) #day eg monday tuesday etc
print(c.strftime("%a"))#day short eg mon tue etc
print(c.strftime("%B"))#MONTH EG JULY
print(c.strftime("%b"))#month short
print(c.strftime("%Y"))#year 
print(c.strftime("%y"))#year
print(c.strftime("%H"))#hour
print(c.strftime("%h"))#hour
cd=datetime.datetime(2001,10,27)#custom date 
print(cd)