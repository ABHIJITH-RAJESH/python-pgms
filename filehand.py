# open function for handling file 2 parameters - filename,mod 
# 4 mods - x(create ),w(write overwite ),a(append continuw with old file ),r(read)
#f1=open("helo.txt","x") #create file syntax
# f1=open("helo.txt","w")
# f1.write("sjh fabdfb fdafjhdbsmcxvsdvb,b ,kfa fa d,kf k ba \ndahdsjhgaf asfsb msfa \nkfsha fb sfa fflagk b")
# f1.close()
# f1=open("helo.txt","a")
# f1.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
# f1.close()
# f1=open("helo.txt","r")
# c=f1.read()
# print(c)
# f1.close()
# # read constraints
# f1=open("helo.txt","r")
# c=f1.read(7)
# print(c)

# read line by line 
# f1=open("helo.txt","r")
# c=f1.readline()
# print(c)
# d=f1.readline()
# print(d) 
# # read line by line using loop 
# for i in f1:
#     print(i)

# f1=open("del.txt","x")

# to delete a file or to do a sysstem baased operation os module is used 
import os
# os.remove("del.txt")
os.rmdir("fcreate") #delete folder
