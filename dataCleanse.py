import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('train.csv')

dfMulher = df[df['Sex'] == 'female']
total  = dfMulher[dfMulher['Survived'] == 1]
print(len(total))
print(len(dfMulher))

def regressaoLogistica(x):
    exp = np.exp(x)
    return (exp/(1 + exp))

print(regressaoLogistica(-0.48))