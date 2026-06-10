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
'''class Level1:
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
print(obj.variable_3, obj.var_3, obj.fun_3())'''

'''class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        #self.__first = val
        ExampleClass.counter +=1
        if val % 2 !=0:
            self.a = 1
        else:
            self.b = 1
            
example_object = ExampleClass(2)
try:
    print(example_object.a)
except AttributeError:
    try:
        print(example_object.b)
    except AttributeError:
        print("the error has occured! slietly passing it!")
        
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)'''

'''class ExampleClass:
    counter = 0
    def __init__(self, val =1):
        ExampleClass.counter += 1
        if val % 2 != 0:
            self.a = 1
            
example.object = ExampleClass(1)

if hasattr(example_object, 'a'):
    print("a =", example_object.a)
    
if hasattr(example_object, 'b'):
    print("b =", example_object.b)
    
print(hasattr(ExampleClass, "b"))
print(hasattr(ExampleClass, 'a'))'''

'''class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False
        
myObj = Python()
print("myObj.population:", myObj.population)
print("myObj.victims:", myObj.victims)
print("myObj.length_ft:", myObj.length_ft)
print("myObj.__venomous:", myObj.__venomous)
print("myObj.venomous:", myObj.venomous)

#print(hasattr(version_2, 'constructor'))
#name mangling in methods
class Classy:
    def visible(self):
        print("visible")
        
    def __hidden(self):
        print("hidden")
        
obj = Classy()
obj.visible()
try:
    obj.__hidden()
except:
    print("failed")
obj._Classy__hidden()

obj = Classy()
print(type(obj))
print(type(obj).__name__)

# isinstance() Function

class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

my_vehicle =Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle,my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end = "\t")
    print()
    
# IS OPERATER

class SampleClass:
    def __init__(self, val):
        self.val = val
        
object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Marry had a little "
string_2 = "Marry had a little lamb"
string_1 += "lamb"

print(string_1 == string_2,string_1 is string_2)

#Basic method inheritance
class Super:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return "My name is"+ self.name + "."
    
class Sub(Super):
    def __init__(self, name):
        pass
        Super. __init__(self, name)
    
obj = Sub(" Andy")
print(obj)

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
    
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
    
class Sub(SuperA, SuperB):
    pass

obj = Sub()
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())'''

# multilevel inheritance

'''class Level1:
    var = 100
    def fun(self):
        return  101
    
class Level2:
    var = 200
    def fun(self):
        return 201
    
class Level3(Level2):
    pass

obj = Level3()
print(obj.var, obj.fun())
    
    
# multiple inheritance conflicts
class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"
class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"
class Sub(Left, Right):
    pass
obj = Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())'''





    
    
    