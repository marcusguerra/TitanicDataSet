import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dfTraincsv = pd.read_csv('test.csv')
dfTraincsv['Title'] = dfTraincsv['Name'].str.extract(r'\b([A-Za-z]+)\.')
#Master = Homem muito jovem para ser chamado de de Mr
#Mrs = mulher casada
#Miss = mulher não casada
#Mr = Homem seja casado ou não
#Outro = outros titulos
valid_titles = ['Mr', 'Miss', 'Mrs', 'Master']
dfTraincsv['Title'] = dfTraincsv['Title'].replace({title: 'Outro' for title in dfTraincsv['Title'].unique() if title not in valid_titles})

title_mapping = {'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Outro': 4}
dfTraincsv['Title'] = dfTraincsv['Title'].map(title_mapping)

embarked_mapping = {'S': 0, 'C': 1, 'Q': 2}
dfTraincsv['Embarked'] = dfTraincsv['Embarked'].map(embarked_mapping)

sex_mapping = {'male': 0, 'female': 1}
dfTraincsv['Sex'] = dfTraincsv['Sex'].map(sex_mapping)

print(dfTraincsv.columns)

dfRegressao, b0, b1, b2, b3, b4, b5, b6, b7 = returnDf(0.9, dfTraincsv, dfTraincsv)
dfTraincsv['Survived'] = dfRegressao['Regressao']
print(dfTraincsv['PassengerId'].head())
print(dfTraincsv['Survived'].head())
