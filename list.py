'''
#append
list = [5, 4, 3, 2, 1]
list.append(6)
print(list)

#insert
list = [5, 4, 3, 2, 1]
list.insert(3,9)
print(list)

# practice problem
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers = [111, 7, 2, 1]
numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#Traversing a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for count in range(len(my_list)):
   print(my_list[count])
   
# write a program to insert 10 numbers starting from 1 to 10 to a list
#list = []
my_list = []
for count in range(1, 11):
 my_list.append(count)
print(my_list) #doubt

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for iterator in range(10):
    my_list[iterator] += 1
print(my_list)

#write a program to calculate sum of all the elements in the list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)

my_list = [10, 1, 8, 3, 5]
total = 0
for i in my_list:
    total += i
print(total)

# copying a variable into another variable

variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2


variable_1, variable_2 = variable_2, variable_1'''

list = [1, 2, 3, 4, 5]
list.insert(1, 6)
 del 1st[0]
  1 st.append(1)
print(1st)
