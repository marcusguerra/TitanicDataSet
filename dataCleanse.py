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
