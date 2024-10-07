# regex re module is used functions findall , split ,search,sub 
import re
v="the rain in spain"
x=re.search("^the.*spain$",v)
if x:
    print("matching")
else:
    print("not matching")
z=re.findall("ai",v)
print(z.count("ai"))
n=re.split("\s",v)
print(n)
k=re.sub("\s",",",v)
print(k)