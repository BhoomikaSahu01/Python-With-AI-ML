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

class Student:     
    def __init__(self, name, age, gender, grade):  # intit is constructor
        self.grade = grade
        self.name = name
        self.age = age
        self.gender = gender
        
    def printDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Grade:", self.grade)
        
mayur = Student("Mayur Valvi", 20, "Male", "10th")
print(mayur)

mayur.printDetails()
        

       
        



