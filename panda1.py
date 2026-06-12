import pandas as pd

data = {
    'name': ['harshi','isha','bhoomika','harshika'],
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