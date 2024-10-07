# class oop:
#     x='hey hello'

# obj=oop()
# print(obj.x)


# oru class initiate cheyane samyath execute cheyune function anu init
# self class instance represent 
# nammal create cheyune clai\sil ula function ne methods anu n aparaya 


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# ob1=person("abhijith","23")
# print(ob1.name,ob1.age)


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def fun(self):
#         print("i am ",self.name)

# ob1 = person("abhijith",23)
# ob1.fun()

#******** inheritance*******

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun(self):
        print("i am ",self.name)

class child(person):
   
    pass
ob1=child("abhijith",23)
ob1.fun()