# Function and Scope
'''def scope_test():
    x = 123
scope_test()
print(x)

def my_function():
    print("do i know the variable", var)

var = 1
my_function()
print(var)

def mult(x):
    var = 7
    return x *var
var = 3
print(mult(7))

def my_function():
    global var 
    var = 2
    print("Do I know that variable ",var)
    
    var = 1
    my_function()
    print(var)
    
var = 2
print(var)

def return_var():
    global var
    var = 5
    return var

print(return_var())
print(var)

def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)
    
var = 1
my_function(var)
print(var)

def my_function(my_list_1):
    print("print #1:", my_list_1)
    print("print #2:", my_list_2)
    my_list_1 =[0, 1]
    print("print #3:", my_list_1)
    print("print #4:", my_list_2)
    
    my_list_2 = [2, 3]
    my_function(my_list_2)
    print("print #5;", my_list_2)
    
def my_function(my_list_1):
    print("print #1:", my_list_1)
    print("print #2:", my_list_2)
    del my_list_1[0]
    print("print #3:", my_list_1)
    print("print #4:", my_list_2)
    
my_list_2 = [2, 3]
my_function(my_list_2)
print("print #5:", my_list_2)


# Recursion
def countDown(number):
    print(number)
    if number == 0:
        return
    else:
        print("Going in rec:", number)
        countDown(number - 1)
        print("out of rec", number)
print("Starting Recursion")       
countDown(5)
print("completed recurssion")

def factorial(number):
    if number <= 0:
        return 1
    else:
        return number * factorial(number -1)
    
print(factorial(5))   

#Tuples
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3


print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)'''
    
    


    