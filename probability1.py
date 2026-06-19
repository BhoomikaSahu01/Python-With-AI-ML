import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm #normal distribution claculator

'''mean_h, std_h = 165, 7

#probability of being talller than 175 cm
prob = 1- norm.cdf(175, mean_h, std_h)#camulative distribution function
print(f'P(height > 175cm)= {prob: .4f} = {prob*100:.1f}%')

#The 68-95-99
print(f'68% of people: {mean_h-std_h :.0f}cm to {mean_h+std_h: .0f}cm')
print(f'95% of people: {mean_h-2*std_h: 0f}cm to {+2*std_h: .0f}cm')
print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h: .0f}')'''

'''from sklearn.model_selection import train_test_split, cross_val_score

np.random.seed(42)
x = np.random.randn(500, 5)
y = np.random.randint(0, 2, 500)

x_train,x_test,y_train,y_test = train_test_split(
  x,y, test_size = 0.2, random_state=42, stratify=y
  )

print(f'Training samples: {len(x_train)} | Test samples: {len(x_test)}')

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=50 , random_state=42)
cv_scores = cross_val_score(model, x, y, cv = 5, scoring = 'accuracy')
print(f'cv score each fold:{cv_scores,round(3)}')
print(f'mean: {cv_scores.mean(): .4f} = {cv_scores.std():.4f}')'''

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#data
n_A, conv_A = 1000, 52
n_B, conv_B = 1000, 68
rate_A = conv_A/ n_A
rate_B = conv_B/ n_B

print(f'version A conversion rate: {rate_A*100: .1f}%')
print(f'version B conversion rate: {rate_B*100: .1f}%')
print(f'Improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')

#chi square test for statistical significant
table = [[conv_A, n_A-conv_A],[conv_B, n_B-conv_B]]
chi2,p_value,dof,expected =stats.chi2_contingency(table)

print(f'chi-square: {chi2:.4f}')
print(f'P_value: {p_value:.4f}')

print('Result:', 'SIGNIFICANT - B is better!'if p_value<0.05 else 'Not significant -could be random')

