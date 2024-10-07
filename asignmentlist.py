#create list 
course = ["datascience" , "python" , "java"]
price =[10000,8000 , 12000 , 7000]
#print list and its type 
print("Courses " )
print(course)
print(type(course))
print("Course price")
print(price)
print(type(price))
#number of courses 
print("number of courses")
print(len(course))
#last course name
print("last course")
print(course[-1])
#1st course 
print("first course")
print(course[0])
#check if java is in course 
print("java" in course)
#check if javascript not in course
print("javascript" not in course)
#print 2 nd item in course
print( course[1])
#add new course to list and add price 
print("new list of courses")
course.append("flutter")
print(course)
price.append(15000)
print("new list of prices of courses")
print(price)
#print price of first three courses
print("price of first three courses")
print(price[0:3])
#print price of last three courses
print("price of last three courses")
print(price[-3:])
#delete last course
course.pop()
print("new list of courses")
print(course)
#delete price of last course 
del course[-1]
print(course)
#sort course list 
course.sort()
#sort list  in descending order 
course.sort(reverse=True)
print(course)