import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def menu():
    while True:
        print('Para sair digite nome = 0')
        try:
            nome = str(input('Digite o nome do embarcado: '))
            if nome == '0':
                break
            idade = int(input('Digite a idade da pessoa embarcada: '))
            if(idade < 0 ):
                continue
            classe = int(input('Digite a classe: '))
            if classe not in [1, 2, 3]:
                continue
            sexo = int(input('Digite o genêro:\n'
                             '1- mulher\n'
                             '2- homem \n'))
            if sexo not in [1, 2]:
                continue
            data = {'sexo': sexo, 'classe': classe, 'idade': idade}
            series_data = pd.Series(data)
            valor = regressaoLogistica(series_data)
            print(valor)
            if(valor >= 0.5):
                print(f"O passageiro {nome} sobreviveu ao Titanic!!!!!!")
            else:
                print(f"O passageiro {nome} infelizmente morreu :(")
        except:
            continue

def logistica(series):
    X = -1.33
    #Sexo
    if(series.iloc[0] == 1):
        X += 2.55
    #2 Classe
    if(series.iloc[1]== 2):
        X += 1.27
    #1 Classe
    if(series.iloc[1] == 1):
        X += 2.58
    X -= (0.04 * series.iloc[2])
    return X

def regressaoLogistica(series):
    exp = np.exp(logistica(series))
    return (exp/(1 + exp))

menu()
