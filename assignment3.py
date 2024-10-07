#Question 1 

x=45
y=45.234
z=35+7j
print(type(x))
print(type(y))
print(type(z))
#int to float
x=float(x)
print(x)
#float to complex
y=complex(y)
print(y)
#float to int 
k=int(x)
print(x)
#int to complex
k=complex(x)
print(k)

# Question 2 

str = " Welcome to Futura Labs "
print(str)

#length of strinng
print(len(str))

#type
print(type(str))

#membership testing

print("Welcome" in str)
print("heloo" not in str)
print("helloo in str" in str)

#print string in sequence
for i in str:
    print(i)

#print char at a position

print(str[5])

#positive indexing 

print(str[3:7])
print(str[5:])
print(str[:7])

#negative indexing 

print(str[-1])
print(str[-5:])
print(str[-5:-3])
print(str[:-3])

#String methods 

# to upper case 
print(str.upper())
# to lower case
print(str.lower())
#removes whitespace
print(str.strip())
#replace string
print(str.replace("Futura","FUTURE"))
#splits string with seperater 
print(str.split( ))
#counts the given string 
print(str.count("F"))

#add number to the string
str1 ="Kochi {}"
num = 24
print(str1.format(num))
# concat two string
print(str+str1)


#question 3

list1 = ["apple","banana","orange","grapes","melon"]
print(list1)
list2 = ["red","blue","green","yellow","blue","pink"]
print(list2)

#  length of list 
print(len(list1))

# type 
print(type(list1))

#membership testing
print("apple" in list1)
print("apple" not in list2)
print("apple" in list2)

# print list in sequence
for i in list1:
    print(i)

#print item in list

print(list1[2])
# print last item in list 
print(list1[-1])
   

#positive indexing 

print(list1[1:3])
print(list1[2:])
print(list1[:2])

#negative indexing 

print(list1[-1])
print(list1[-2:])
print(list1[-4:-2])
print(list1[:-3])

#replace item in pos 2 with item 3 
list1[2]="pineapple"
print(list1)

#add item to end of list 
list1.append("orange")
print(list1)

#add item lime at pos 2 of list
list1.insert(2, "lime")
print(list1)
#add 2 list 
list1.extend(list2)
print(list1)
#remove item from list
list1.remove("orange")
print(list1)
#remove item from index 3 
list1.pop(3)
print(list1)
#remove last item from list 
list1.pop()
print(list1)
#keyword to remove item from list n 
del list1[8]
print(list1)
#sort string list 
list1.sort()
print(list1)
#sort string list in descending order
list1.sort(reverse=True)
print(list1)
#copy items i
list3=list1.copy()
print(list3)
list4=list(list3)
print(list4)
#clear list 
list4.clear()
print(list4)
# delete list
del list4
# count item
print(list1.count("apple"))




