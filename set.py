set1 = {"red","blue", "green " , "yellow"}
# set are unordered , unindexed , unmutable  except for adding and removing items ,duplicate values cant be stored 
print(set1)
print(type(set1))
print(len(set1))
print("red" in set1)
print("red " not in set1)
print("red " in set1)
for i in set1:
    print(i)

print(set1)
# add item
set1.add("cyan")
print(set1)
set2={6,12,5,6}
# add 2 set 
set1.update(set2)
print(set1)
set1.remove("red")
print(set1)
# removie item with no error 
set1.discard("cyan")
print(set1)
# remove a random item from list 
set1.pop()
print(set1)
# if there is multiple sets added ad giving set2 , set3 etc\
# set operations
set3=set1.union(set2)
print(set3)
set5={"yellow"}
set4=set3.intersection(set5)
print(set4)
# set3-set5 
set4=set3.difference(set5)
print(set4)
set4.clear()
print(set4)
del set4 