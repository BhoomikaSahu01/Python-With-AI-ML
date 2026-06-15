import pandas as pd

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


