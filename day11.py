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
print(list_sum(2))'''

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.append(i+1)
        
    return strange_list
print(strange_list_fun(5))






