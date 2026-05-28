 '''single line comment we use hash # '''
# multi line coment out we use triple quotes''' '''

'''print("statement 1")
print("statement 2")
print("statement 3")'''

'''
variable = myOfficialName [camel casing]
Function = myOfficialName()
Class = MyOfficialName
object = myOfficialNameObj
Constants = MY_OFFICIAL_NAME

 

x = ["Maruti", "BMW"]
y = ["Maruti", "BMW"]
z = x
print("+---------+") 
print("|         |")
print("|         |")
print("|         |")
print("|         |")
print("|         |")
print("+---------+")'''

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#for temp in range(1, 7):
  #print(str(temp)*temp)
  
'''my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for iterator in range(len(my_list)):
    print(my_list[iterator])'''
    
'''
iterator 0 1 2 3
output   1 2 3 4
'''

'''my_list = []
no_element = int(input("enter the  value of how many you want to add element in list"))
for iterator in range(1, 11):
    element = int(input("enter the element"))
    my_list.append(element)
print(my_list)'''

'''list = []

for iterator in range(10):
    list.append(iterator+1)
print(list)'''
'''list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for index in range(len(list)):
    list[index] += 1
    
print(list)'''

'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum = 0;
for index in range(len(my_list)):
    sum += my_list[index]
print(sum)'''
    
'''my_list = [10, 1, 8, 3, 5]
total = 0
for element in my_list:
    total += element
print(total)'''

# Copying a variable into another variable

'''variable1 = 1
variable2 = 2

print("variable: ", variable2)
print("variable2:", variable2)

variable1, variable2 = variable2, variable1
print("variable1:",variable1)
print("variable2:",variable2)

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list[4], list[1] = list[1],list[4]

print(list)'''

# Lists <> Sorting 

'''my_list = [1, 2, 3, 4, 5]#[8, 10, 6, 2, 4]
swapped = True
count = 0
while swapped:
    swapped = False #no swaps so for
    for i in range(len(my_list)-1):
        count += 1
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i],my_list[i + 1] = my_list[i + 1],my_list[i]
print(my_list)
print(count)

# sort method
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#list reverse method
my_list = [8, 10, 6, 2, 4]
my_list.reverse()
print(my_list)

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
print(list_1)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
# output emptylist

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-5:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
new_list = my_list[2:]
print(new_list)

#delete
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
new_list = my_list[2:]
print(new_list)
del my_list[1:3]
del my_list
print(my_list)

my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)'''

list_1 = ["A", "B", "c"]
list_2 = list_1
list_3 = list_2
del list_1[0]



















