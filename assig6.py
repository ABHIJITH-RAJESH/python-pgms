# display even, odd numbers in a list 
list1 = (2,3,4,5,7)
b= list(filter(lambda x:x%2==0,list1))   
print(b)
c= list(filter(lambda x:x%2!=0,list1))   
print(c)
# print square of elements in a list
d= list(map(lambda x:x*x,list1))   
print(d)



# print a list of even numbers from another list 
e=list(filter(lambda x:x%2==0,list1))
f=list(map(lambda x:x*x,e))
print(f)
# create a string list print string of length > 5 in a list form 
list3=("adsd","dsdadsfa","dsafasfsfaf","Assd")
list4= list(filter(lambda x:len(x)>5,list3))
print(list4)

