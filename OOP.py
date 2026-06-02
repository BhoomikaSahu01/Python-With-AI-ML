# class

# class ThisIsMyFirstClass:
#     name = "Bhoomika"  #properties define
#     age = 20
    
#     def getName(self):  #Method
#         print(self.name)# self app kis object ke baarkare ho
        
        
# firstObject = ThisIsMyFirstClass()
# print(firstObject)

# firstObject.getName()
# print(firstObject.name)

# class Student:
#         def _init_(self):  # intit is constructor
#             self.name = ""
#             self.gender = ""
#             self.grade = ""
# mayur = Student()
# print(mayur)
        
# mayur.name = "Mayur Valvi"
# mayur.age = 20
# mayur.gender = "Male"
# mayur.grade = "10th"

# print(mayur.name)
# print(mayur.age)
# print(mayur.gender)
# print(mayur.grade)

# class Student:     
#     def __init__(self, name, age, gender, grade):  # intit is constructor
#         self.grade = grade
#         self.name = name
#         self.age = age
#         self.gender = gender
        
#     def printDetails(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Gender:", self.gender)
#         print("Grade:", self.grade)
        
# mayur = Student("Mayur Valvi", 20, "Male", "10th")
# print(mayur)

# mayur.printDetails()
        

# class ExampleClass:
#     def __init__(self,val=1):
#         self.first = val
#     def set_second(self,val):
#         self.second = val

# object_1=ExampleClass()
# object_2=ExampleClass(2)
# object_2.set_second(3)
# object_3=ExampleClass(4)
# object_3.third = 5

# print(object_1.__dict__)
# print(object_2.__dict__)
# print(object_3.__dict__)  
        
# class Classy:
#     def method(self, par):
#         print("method", par)
        
# obj = Classy()
# obj.method(1)

# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)
# obj = Classy()
# obj.var = 3
# obj.method()

# class star:
#     def __init__(self, name, galazy):
#         self.name = name
#         self.galazy = galazy
        
# sun = star("sun", "Milky way")
# print(sun)

# class star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galazy = galaxy
#     def __str__(self):
#         return self.name + ' in ' + self.galazy
    
# sun = star("sun", "Milky Way")
# print(sun)
     
        

# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# class Vehicle:
#     pass
# class LandVehicle(Vehicle):
#     pass
# class TrackedVehicle(LandVehicle):
#     pass
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end = '\t')
#     print()

# class super:
#     supVar = 1
    
# class sub(super):
#     subVar = 2
    
# obj = sub()
# print(obj.subVar)
# print(obj.supVar)

# class super:
#     def __init__(self):
#         super().__init__()
#         self.subVar = 11
        
# class Sub(super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)

''' super is a keyword'''
''' multilevel inheritance'''
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101
    def fun_1(self):
        return 102
    
class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super(). __init__()
        self.var_2 = 201
    def fun_2(self):
        return 202

class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super(). __init__()
        self.var_3 = 301
    def fun_3(self):
        return 302

obj = Level3()
print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
    
    