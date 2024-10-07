# arbitrary arguments *args
def fun(*g):
    print(g[2]+g[1])

fun(2,3,4,56,678,343,43,445,5555)

# keyword arguments  kwargs arguments are passed in key value form 
def kew(x,y):
    print(x)
    print(y)

kew(x=10,y=20)

# arbitrary keyword arguments **args used when no of key value is unknown key are alphabets

def arbkey(**x):
    print(x["a"])
    print(x["b"])

arbkey(a=5,b=1500)

# default arguments

def defau(x=10):
    print(x)

defau()
defau(150)


# return statement

def ret(x):
    c=15+x
    return c

print(ret(10))

# pass statement
def toto(x):
    pass
def lis(x):
    for i in x:
        print(i)

list1 = [2,3,4,5,6,7]
lis(list1)

# lambda function: one line statements many arguments 1 expression small period of time
# lambda argument(s): expresiion

c = lambda x,y,z: x+y
print(c(10,15,30))
# map and filter function are often used in lambda 
fruits =["apple","mango","melon","orange"]
fruit2 = list(map(lambda x:x.upper(),fruits))
print(fruit2)

no =[23,45,65,32,321,455]
no2=list(filter(lambda x:x>200,no))
print(no2)