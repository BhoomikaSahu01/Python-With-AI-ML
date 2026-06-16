'''import pandas as pd

data = {
    'Name': ['harshi','isha','bhoomika','harshika'],
    'age':  [22, 21, 23, 21],
    'Marks': [85, 55, 66,59],
    'city': ['Bhopal', 'Indore', 'Betul', 'sagar'],
}
df = pd.DataFrame(data)
print(df)
# Explore the data
print(df.shape)
print(df.head(3))
print(df.dtypes)
print(df.describe())

#select coloums
print("df['Name']: \n", df['Name'])
print(df[['Name', 'Marks']])

## Filter rows
print(df[df['Marks'] >= 85])
print(df[df['city'] == 'Bhopal'])
print( df[ (df['Marks']>=80) & (df['city'] == 'Indore') ] )

def get_grade(x):
    if x >=90:
        return 'A'
    elif x >= 75:
        return 'B'
    else:
        return 'c'
df['Grade'] = df['Marks'].apply(get_grade)
print(df['Grade'])
print('---------------')
print(df)

# GroupBY - like excel pivot
city_avg = df.groupby('city')['Marks'].mean()
print(city_avg)

print(df.groupby('city')['Marks'].mean())

df.groupby('city')['Marks'].mean()

#Read real CSV file
df2 = pd.read_csv('students.csv')
print(df2)
# cleaning
df2['Name'] = df2['Name'].str.strip()
print(df2)
df2['Marks'] = df2['Marks'].str.replace('#', '')
df2['City'] = df2['City'].str.replace('__', '')
print(df)
df2.to_csv('clean_output.csv', index=False) #save'''

# Matplotlib

import matplotlib .pyplot as plt
import numpy as np

months = ['jan', 'Feb', 'Mar', 'Apr', 'May', 'jun', 'jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [45,52,48,61,58,72,69,75,68,82,90,95]

# line chart
plt.figure(figsize=(12,5))
plt.plot(months,sales,marker='o',color='steelblue',linewidth=2,markersize=8)
plt.fill_between(months, sales, alpha=0.15, color='steelblue')
plt.title('Monthly Sales 2024 (Rs. Thousands)', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Sales (Rs. K)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

