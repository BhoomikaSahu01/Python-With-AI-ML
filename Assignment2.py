'''
There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
Your task is to:
write a line of code that prints the length of the existing list (Step 1).
write a line of code that removes the last element from the list (Step 2)
write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 3)
'''
'''numbers = [1, 2, 3, 4, 5]
print(len(numbers))
# Remove the last element
numbers.pop()
# Replace the middle number with user input
numbers[len(numbers) // 2] = int(input("enter a new number"))
print(numbers)'''

''' The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.'''

# #steo 1L create an empty list
# beatles = []

# #step2 : add john lennon, paul McCartney, and George horrision
# beatles.append("john Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")

# #step3 : add Stu Sutcliffe and Pete Best using a Loop
# for member in["Stu Sutcliffe", "pete Best"]:
#     beatles.append(member)
    
# #step4 remove stu sutcliffe and pete Best using a loop
# del beatles[3]
# del beatles[4]

# #step5: add Ringo starr at the beginning
# beatles.insert(0, "Ringo Starr")

# #Display the final list
# print("The Beatles members are")
# print(beatles)

''' Practice Questions Loops'''
''' Write a program to print numbers from 1 to 50 in this pattern'''

# result = []

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         result.append("FizBuzz")
#     elif i % 3 == 0:
#         result.append("Fiz")
#     elif i % 5 == 0:
#         result.append("Buzz")
#     else:
#         result.append("i")
        
# print(result)
        
    
''' Count Numbers of Digit in a String'''

# string = "Mindcoders password2 is : 1234"

# count = 0

# for ch in string:
#     if ch.isdigit():
#         count += 1
        
# print("Total numbers of Digits =", count)

'''string = "U r a a n s 0 f t s k i l l 1 s 1234"

count = 0
for ch in string:
    if ch.isdigit():
        count += 1
        
print("Total number of Digits =", count)'''

''' Count Occurrence of 's' or 'S' in a string'''

'''# string = "MindCoders"

# count = 0
# for ch in string:
#     if ch == 's' or ch == 'S':
#         count += 1
        
# print("Count of s or S =",count)'''