# function
'''def message():
    print(" enter a value:")
    
message()
a = int(input())  #invocation // calling a function

message()
b = int(input())

message()
c = int(input())

def message():
    print("enter a value")
    
message = 1

print("we start here.")
print(message)
message()
print("we end here.")

def message():
    print("enter a value")
    temp = int(input())
    return temp

print("step 1")
a =message()
 #invocation // calling a function
print("step 2")
b  =message()

print("step 3")
c = message()

print("a:", a)
print("b:", b)
print("c:", c)

# type error
def hi():
    print("hi")
hi(5)

def hello (n): #defining a function
    print("Hello,",n)# body of the function
    
name = input("enter your name:")
hello(name) #calling the function

#parameterized functions

def message(number):
    print("enter a number:", number)
    
number = 1234
message(1)
print(number)

def message(what, number):
    print("enter",what, "number", number)
    
message("telephone", 11)
message(11, "telephone")
message("price", 5)
message("number", "number")

# possitional parameter passing
 
def introduction(first_name, last_name):
    print("Hwllo, my name is", first_name, last_name)
    
introduction("Like","skywaller")
introduction("jesse", "Quick")
introduction("clark","kent")

# key word argument

def introduction(first_name, last_name):
    print("Hwllo, my name is", first_name, last_name)
    
introduction("Like","skywaller")
introduction("jesse", "Quick")
introduction("clark","kent")

introduction(first_name= "james", last_name= "Bond")
introduction(first_name="skywaller", last_name = "luke")

# mixing positional and keyword arguments
def adding(a, b, c):
    print(a, "+", b, "+", c, "+", a*b+c)
    
adding(1, 2, 3)
adding(c=1, a=2, b=3)
adding(3, c=1, b=2)
adding(3, a=1, b=2)

def happy_new_year(wishes = True):
    print("Three..")
    print("Two..")
    print("one..")
    if not wishes:
        return
    print("happy new year !")
happy_new_year(False)

# Effects and result

def boring_function():
    print("Boredan Mode ON")
    return 123

print("This lesson is interesting !")
boring_function()
print("This lesson is boring ....")

#None keyword

def checkMyVar(variable):
    if(variable == 10):
        print("variable is 10")
        return 2
    else:
        print("variable is not up to the mark")
        
print(checkMyVar(5))

def list_sum(list):
    s = 0
    
    for elem in list:
        s += elem
        
    return s
print(list_sum([5, 4, 3]))
print(list_sum(2))

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.append(i+1)
        
    return strange_list
print(strange_list_fun(5))'''






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
print("This lesson is boring __")

#functions and scope
def scope_test():
    x = 123
scope_test()
print(x)



# Function and Scope
# '''def scope_test():
#     x = 123
# scope_test()
# print(x)

# def my_function():
#     print("do i know the variable", var)

# var = 1
# my_function()
# print(var)

# def mult(x):
#     var = 7
#     return x *var
# var = 3
# print(mult(7))

# def my_function():
#     global var 
#     var = 2
#     print("Do I know that variable ",var)
    
#     var = 1
#     my_function()
#     print(var)
    
# var = 2
# print(var)

# def return_var():
#     global var
#     var = 5
#     return var

# print(return_var())
# print(var)

# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)
    
# var = 1
# my_function(var)
# print(var)

# def my_function(my_list_1):
#     print("print #1:", my_list_1)
#     print("print #2:", my_list_2)
#     my_list_1 =[0, 1]
#     print("print #3:", my_list_1)
#     print("print #4:", my_list_2)
    
#     my_list_2 = [2, 3]
#     my_function(my_list_2)
#     print("print #5;", my_list_2)
    
# def my_function(my_list_1):
#     print("print #1:", my_list_1)
#     print("print #2:", my_list_2)
#     del my_list_1[0]
#     print("print #3:", my_list_1)
#     print("print #4:", my_list_2)
    
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("print #5:", my_list_2)


# # Recursion
# def countDown(number):
#     print(number)
#     if number == 0:
#         return
#     else:
#         print("Going in rec:", number)
#         countDown(number - 1)
#         print("out of rec", number)
# print("Starting Recursion")       
# countDown(5)
# print("completed recurssion")

# def factorial(number):
#     if number <= 0:
#         return 1
#     else:
#         return number * factorial(number -1)
    
# print(factorial(5))   

# #Tuples
# my_tuple = (1, 10, 100)

# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3


# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)'''
    
    


    