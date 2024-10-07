# password check 
# user input 
# length >8,small letter ,capital letter , number ,@_,no space 
import re
v=str(input("enter the password"))

flag=0
if len(v)>8 and v.count(" ")==0 :
   if re.search("[a-z]",v):
      if re.search("[A-Z]",v):
         if re.search("[0-9]",v):
            if re.search("[@_]",v):
               flag=1
               print("valid password")
            

      
if flag==0:
      print("invalid password")
    
