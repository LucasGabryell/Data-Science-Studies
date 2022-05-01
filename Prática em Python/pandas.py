import pandas as pd

#carrega arquivo para dataframe Pandas
dados = pd.read_csv("Credit.csv", sep=";")
#formato
dados.shape()
#resumo estatístico de colunas numéricas
dados.describe()
#primeiros registros
dados.head()
#últimos registros, com parâmetros
dados.tail(2)
#filtrar por nome da coluna
dados[["duration"]]
#filtrar linhas por indice
dados.loc[1:3]
#linhas 1 e 3
dados.loc[[1,3]]
#filtro
dados.loc[dados['purpouse'] == "radio/tv"]
#outra condição
dados.loc[dados['credit_amount'] > 18000]
#atribuimos resultado a variável, criando outro df
credito2 = dados.loc[dados['credit_amount'] > 18000]
#definimos só algumas colunas
credito3 = dados[['checking_status', 'duration']].loc[dados['credit_amount'] > 18000]
#séries, única coluno
#pode ser criada a partir de listas, array do numpy ou coluna de dataframe
s1 = pd.Series([4,4,5,664,352,32,12,1])
print(s1)

#serie a partir de um array do numpy
import numpy as np
array1 = np.array([4,4,5,664,352,32,12,1])
s2 = pd.Series(array1)
print(s2)

#series a partir de um dataframe
s3 = dados['purpose']
print(s3)
print(type(s3))

#note a diferença, temos um dataframe
d4 = dados[['purpose']]
print(type(d4))
#renomear
dados.rename(columns={"duration":"duração","purpose": "propósito"})
#porém a alteração não é persistida
dados.head(1)
#para persistir
dados.rename(columns={"duration":"duração","purpose": "propósito"}, inplace=True)
dados.head(1)

#excluir coluna
dados.drop('checking_status',axis=1,inplace=True)
print(dados)
dados.head(1)
#verficar dados nulos
dados.isnull()
#verificar dados nulos
dados.isnull().sum()
#retirar colunas com NaN
dados.dropna()
#preencher dados faltantes
dados['duração'].fillna(0, inplace=True)
#iloc
dados.iloc[0:3,0:5]
dados.iloc[[0,4,6,7,3],0:5]