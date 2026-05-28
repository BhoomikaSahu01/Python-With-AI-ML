# Function
'''
print("enter a value :")
a = int(input())

print("enter a value")
b = int(input())

print("Enter a value :")
c = int(input())

#syntax of a function

def function_name():
    function_body
    
def message():
    print("enter a value :")
    
print("we start here .")
message()
print("we end here .")
def message():
    print("Enter a value:")
    
def message():
    print("Enter a value :")
message()
a = int(input())

message()
b = int(input())

message()
c = int(input())

def message(): #defining a function
    print("Hello")# body of the function
    
message() # calling the function

def hello(n): #defining a function
    print("Hello,", n)# body of the function
 
name = input("Enter your name :")
hello(name)# Calling the function

def message(number):
    print("Enter a number :",number)
    
# Parameterized function

def message(what, number):
    print("Enter", what, "number", number)
    
message("telephone", 11)
message("price", 5)
message("number", "number") 

# positional parameter passing

def introduction(first_name, last_name):
    print("Hello, my name is",
first_name, last_name)   
    
introduction("luke", "skywalker")
introduction("jese", "Quick")
introduction("clark", "kent")

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
    
introduction("skywalker", "luke")
introduction("Quick", "Jesse")
introduction("kent", "clark")

# keyword argument passing

def introduction(first_name, last_name):
   print("Hello, my name is", first_name, last_name)
 
introduction(first_name = "james", last_name = "Bond") 
introduction(last_name = "skywalker", first_name = "luke")

# Mixing positional and keyword arguments

def adding(a, b, c):
    print(a, "+", b, "+", c,"=", a+b+c)
    
adding(1, 2, 3)
or
adding(c=1, a=2, b=3)
or
adding(3, c=1, b=2)

# effects and results: the result instruction

def happy_new_year(wishes = True):
 print("Three..")
 print("two__")
 print("one ...")
 if not wishes:
    return
    print("Happy New Year")
    
happy_new_year()

def boring_function():
    return 123

x = boring_function()
print("The boring_function has returned its result. It's :",x)

# Funtion returns a value but it is ignored
def boring_function():
    print("'Boredom Mode' ON.")
    return 123
print("This lesson is interesting!")
boring_function()
print("This lesson is boring __")'''

#functions and scope
def scope_test():
    x = 123
scope_test()
print(x)


