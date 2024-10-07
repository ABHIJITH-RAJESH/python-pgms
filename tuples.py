tuples=("red","blue", "green " , "yellow")
print(tuples)
print(type(tuples))
print(len(tuples))
print("red" in tuples)
print("red  " in tuples)
print("red  " not in tuples)
for i in tuples:
    print(i)

print(tuples[2])
print(tuples[-1])
print(tuples[1:3])
print(tuples[:-3])
print(tuples[-3:])
print(tuples[-4:-2])


a =list(tuples)
print(a)

a[1]="cyan"
print(a)
# tuples are immutable to perform operations convert it to list data type
a.append("pink")
print(a)
tuples=tuple(a)
print(tuples)
tuple2 = (6,12,5,6)
print(tuple2)
# join 2 tuple 
tuple3= tuples + tuple2
print(tuple3)
# duplicate elements in tuple 
tuple3 = tuple3*2 #duplicate it 2 times 
print(tuple3)
print(tuple3.count("cyan"))
