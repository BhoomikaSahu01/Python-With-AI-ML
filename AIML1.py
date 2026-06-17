'''statistics for AI/ML'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


#employee salaries
salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

#central tendency - where is the 'center' of data
mean = np.mean(salaries)
median=np.median(salaries)
mode= stats.mode(salaries,keepdims=True).mode[0] 

print(f'mean (average): Rs.{mean}K')
print(f'median (average): Rs.{median}K')
print(f'mode (most common): Rs.{mode}K')

'''spread-- how varied is data'''
std = np.std(salaries)
var = np.var(salaries)
rng = max(salaries)-min(salaries)
q1 = np.percentile(salaries,25)
q2 = np.percentile(salaries,75)
iqr = q3 = q1
print(f'std daviation:{std: .2f}K (most important spread measure)')
print(f'IQR: {iqr}K (Q1={q1}, Q3={q3})')

#Qutlier detection using IQR
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliers=[x for x in salaries if x<lower or x>upper ]
print(f'outliers: {outliers}')