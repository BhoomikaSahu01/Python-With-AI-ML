import csv
records = [
    ['Name', 'Marks', 'City', 'Grade'],
    ['Rahul',85, 'Bhopal', 'B'],
    ['Priya', 92, 'Indore', 'A'],
    ['Amit', 73, 'Jabalpur', 'B'],
]
with open('students.csv', 'w',newline = '') as f:
    csv.writer(f).writerows(records)

with open('students.csv', 'r') as f:
     for row in csv.DictReader(f):
         print(f'{row["Name"]}: {row["Marks"]} marks ({row["city"]})')
         
''' Assignment'''
import csv
records = [
    ['Name', 'Age', 'Marks in Maths', 'Marks in Science', "Marks in English"],
    ['priya', 23, 96, 79, 88 ],
    ['Harshika', 19, 96, 79],
    ['Harsh', 17, 66, 88, 77],
    ['Nancy', 19, 55, 77, 66],
    
]
with open('students.csv', 'w', newline= '')as f:
    csv.writer(f).writerows(records)
    
name = input("enter student name for search:")

found = False

with open('Students.csv', 'r') as f:
    for row in csv.DictReader(f):
        if row['Name'] == name:
            print(f'Found {name}')
            print(f'{row["Name"]}: {row["Marks"]}')
            break
     
if not found:
    print("Student not found")
    
# import pandas as pd

# data = {
#     'name': ['harshi','isha','bhoomika','harshika'],
#     'age':  [22, 21, 23, 21],
#     'Marks': [85, 55, 66,59],
#     'city': ['Bhopal', 'Indore', 'Betul', 'sagar'],
# }
# df = pd.DataFrame(data)
# print(df)
# # Explore the data
# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe())