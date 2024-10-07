name =" My name, is{} abhijith"
print(name)
print(len(name))#length of string
print(type(name))#data type of variable 
print("is" in name)
print("helo" in name)
print("hello" not in name)
for i in name: #print string in sequence
    print(i)  
print(name[4])   #print char at pos 4


#positive indexing 
print(name[4:7])#last index is not printed
print(name[5:])#print from starting till end of string 
print(name[:5])#print from starting til end pos

#negative indexing 
print(name[-1])#print last character 
print(name[-5:-3])#prints from pos - 5 from last to end pos - 1
print(name[-5:])#prints from pos - 5 to end of string 
 
 
#String methods 
print(name.upper())#converts string to upper case 
print(name.lower())# converts string to lower case 
y = "    hello world   "
print(y)
print(y.strip())#removes whitespace fromm begining and end of string
print(name.replace("abhijith","rajesh"))#replace string 
print(name.split(","))#splits string with seperater 
print(name.count("a"))#counts the given string 
print(name+y)# concat two string 
num =5
print(name.format(num))#add number to the string where the number is positioned using curly braces
nam = "my name is \"abhijith\""#\ is used for print characters like " ;: , ' etc
print (nam)

#list data type (sqeunce type datatype) are ordered mutable can input duplicate elements 



