y = [6,12,5,6]#[] for list {} for set 
print(y)
print(len(y))
print(type(y))
print(5 in y)
print(7 in y)
print(7 not in y)
print(y[2])
print(y[0:3])
print(y[0:])
print(y[:3])
print(y[-3:-1])
print(y[-1])
for i in y:
    print(i)
y[2]= 3 #replace item in pos 2 with item 3 
print(y)
y.append(17)#add item to end of list 
print(y)
y.insert(2,25)#add item 25 at pos 2 of list
print(y)
x=["ac","xada","ksd"]
print(x)
y.extend(x)#add 2 list 
print(y)
y.remove(12)#remove item from list
print(y)
y.pop(3)#remove item from index 3 
print(y)
n=[3,5,6,4,5,6,8]
print(n)
n.pop()#remove last item from list 
print(n)
del n[0]#keyword to remove item from list n 
print(n)
x.sort()#sort string list 
print(x)
x.sort(reverse=True)#sort string list in descending order
print(x)
z=x.copy()#copy items in x to z
print(z)
a=list(z)#copy list in z to a
print(a)
b = a+z 
print(b)
z.clear()#clear list 
print(z)
del z 
print(b.count("xada"))
# tuple is immutable created using ()


