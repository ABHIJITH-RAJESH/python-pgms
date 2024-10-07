# # calculate sum of two numbers 
a = int(input("enter the first number "))
b = int(input("enter the second number "))

print(a+b)

# #calculate average of three numbers 

a = int(input("enter the first number "))
b = int(input("enter the second number "))
c = int(input("enter the third number "))
print((a+b+c)/3)

for i in range(1,11):
    print(end="\n")
    for j in range(1,11):
        print(i*j,end="\t")
print("\n")

# simple calculator

def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)
def multi(x,y):
    print(x*y)
def divi(x,y):
    print(x/y)
c = int(input("enter the operation 1 for add, 2 for sub, 3 for mult, 4 for divi"))
if c==1:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    add(a,b)
elif c==2:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    sub(a,b)
elif c==3:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    multi(a,b)
elif c==4:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    divi(a,b)

