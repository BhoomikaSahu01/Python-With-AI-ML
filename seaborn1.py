import matplotlib .pyplot as plt

import seaborn as sns 
import pandas as pd
import numpy as np

np.random.seed(42)
#Data
df = pd.DataFrame({
    'marks':    np.random.randint(40,100,100),
    'study_hours':  np.random.uniform(2,10,100),
    'city':     np.random.choice(['Bhopal', 'Indore', 'Jabalpur'],100),
    'gender':   np.random.choice(['Male', 'Female'],100)})

#histogram with kde - see the distribution
# plt.figure(figsize=(10,4))
# sns.histplot(df['marks'],bins=20,kde=True, color='steelblue')
# plt.title('Distribution of student Marks')
# plt.show()

'''box plot
sns.boxplot(data = df ,x = 'city', y='marks', palette='Set2')
plt.title('Marks distribution by city')
plt.show()'''

'''heatmap (coleration)
plt.figure(figsize=(5,4))
sns.heatmap(df[['marks', 'study_hours']].corr(),annot=True,cmap ='coolwarm', vmin=-1,vmax=1)
plt.title('correlation Matrix')
plt.show()'''

'''pair plot all relation at once
sns.pairplot(df[['marks', 'study_hours']],diag_kind='kde')
plt.show()'''

''''''