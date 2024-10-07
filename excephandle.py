# exception handling try except Block ,else , finally

try:
    y="sdsaf"
    x=10
    print(x)
except TypeError:
    print("define variable")
except:
    print("error")
else:
    print("code run successfully")
finally:
    print("code ran ")
    # exception raise user defined errors syntax raise

x=-55
if(x<0):
    raise Exception("enter a positive number ")

         

