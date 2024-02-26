import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#When we fit a logistic regression model, the intercept term in the model
# output represent the log odds of the response variable occurring when all
# predictor variables are equal to zero.

#criar coluna familia
df = pd.read_csv('train.csv')
#Criando uma coluna nova com o titulo da pessoa
df['Title'] = df['Name'].str.extract(r'\b([A-Za-z]+)\.')
#Master = Homem muito jovem para ser chamado de de Mr
#Mrs = mulher casada
#Miss = mulher não casada
#Mr = Homem seja casado ou não
#Outro = outros titulos
valid_titles = ['Mr', 'Miss', 'Mrs', 'Master']
df['Title'] = df['Title'].replace({title: 'Outro' for title in df['Title'].unique() if title not in valid_titles})

dfmale = df[df['Sex'] == 'male']
dffemale = df[df['Sex'] == 'female']

print(len(dffemale['Survived'] == 1))
def odds(total, acerto):
    probabilidade = acerto / total
    odd = probabilidade/(1-probabilidade)
    return odd

def calculaBetai(odds1, odds2):
   divisao = odds1 / odds2
   return np.log(divisao)

