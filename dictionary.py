# key value pairs items are accesed using key (key,value)
# ordered, changeable,2 items cannot have same key values
dict1 ={"1":1, "2":"ads" , "3":"dfa", "4":34}
print(dict1)
print(type(dict1))
print(len(dict1))
print(dict1["2"])
print("3" in dict1)
print("3 " in dict1)
print("3 " not in dict1)
# fetch value of key "3" 
print(dict1.get("3"))
# get key values
print(dict1.keys())
# get key values
print(dict1.values())
# fetch items key value pair 
print(dict1.items())
# fetch values 
for i in dict1:
    print(dict1.get(i))

for i in dict1:
    print(dict1[i])   

for i in dict1.keys():
    print(i)
for i in dict1.values():
    print(i)

# fetch items using loop 

for i in dict1.items():
    print(i)


# change value  at index at key 

dict1["1"]=23
print(dict1)


# make sure to {} inside update

dict1.update({"1":46})
print(dict1)


# update or add item 

dict1["23"]=450
print(dict1)

dict1.update({"12":446})
print(dict1)

# copy dict 
dict2=dict1.copy()
print(dict1)

dict2=dict(dict1)
print(dict1)

# remove item
dict1.pop("12")
print(dict1)

del dict1["3"]
print(dict1)

dict1.clear()
print(dict1)
del dict1 
# nested dictionary
family = {"child1":{"ram":12},"child2":{"raj":23},"child3" : {"eren":24}}
print(family)
print(family["child2"])
print(family["child2"]["raj"])