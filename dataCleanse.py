import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('test.csv')

null_counts = df.isnull().sum()

print("Quantidade de valores nulos por coluna:")
print(null_counts)

df = pd.read_csv('train.csv')

null_counts = df.isnull().sum()

print("Quantidade de valores nulos por coluna:")
print(null_counts)