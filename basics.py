 
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
print(count)'''

# sort method
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)



