import pandas as pd
import seaborn as srn
import statistics as sts

#importar dados
dataset = pd.read_csv("tempo.csv", sep=";")
#visulizar
print(dataset.head())
print('----------')

agrupadoApar = dataset.groupby(['Aparencia']).size()
print(agrupadoApar)
print('----------')

agrupadoTemp = dataset.groupby(['Temperatura']).size()
print(agrupadoTemp)
print('----------')

agrupadoUmid = dataset.groupby(['Umidade']).size()
print(agrupadoUmid)
print('----------')

agrupadoVento = dataset.groupby(['Vento']).size()
print(agrupadoVento)
print('----------')

agrupadoJogar = dataset.groupby(['Jogar']).size()
print(agrupadoJogar)
print('----------')

#temperatura
print(dataset['Temperatura'].describe())
srn.boxplot(dataset['Temperatura']).set_title('Temperatura')
srn.boxplot(dataset['Temperatura']).set_title('Temperatura')

#Umidade
print(dataset['Umidade'].describe())
srn.boxplot(dataset['Umidade']).set_title('Umidade')
srn.boxplot(dataset['Umidade']).set_title('Umidade')

#aparencia valor invalido
agrupado = dataset.groupby(['Aparencia']).size()
print(agrupado)
dataset.loc[dataset['Aparencia'] == 'menos', 'Aparencia'] = "Sol"
agrupado = dataset.groupby(['Aparencia']).size()
print(agrupado)

#temperatura valor invalido
agrupado = dataset.groupby(['Temperatura']).size()
print(agrupado)
dataset.loc[dataset['Temperatura'] < -100 or dataset['Temperatura'] > 100]
#substituir valores
mediana = sts.median(dataset['Temperatura'])
print(mediana)
dataset.loc[dataset['Temperatura'] < -100 or dataset['Temperatura'] > 100, 'Temperatura'] = mediana

#Umidade valores invalidos
agrupado = dataset.groupby(['Umidade']).size()
print(agrupado)
dataset['Umidade'].isnull().sum()
mediana = sts.median(dataset['Umidade'])
print(mediana)
#Alterando valores nulos para a mediana
dataset['Umidade'].fillna(mediana, inplace=True)
#verificando se ainda restam valores nulos
dataset['Umidade'].isnull().sum()

#para valores acima do normal
#vizualizar valores
dataset.loc[(dataset['Umidade'] <  0 )  | ( dataset['Umidade'] >  100) ]
#atualiza valores com mediana
dataset.loc[(dataset['Umidade'] <  0 )  | ( dataset['Umidade'] >  100), 'Umidade'] = mediana
#visuliza valores para verificar se foram mudados
dataset.loc[(dataset['Umidade'] <  0 )  | ( dataset['Umidade'] >  100) ]

#Ventos valores invalidos
#Vemtos
agrupado = dataset.groupby(['Vento']).size()
print(agrupado)
#verificando total de valores nulos
dataset['Vento'].isnull().sum()
#preenchendo valores nulos com 'FALSOS'
dataset['Vento'].fillna('FALSO', inplace=True)
#verificando se ainda tem valores nulos
dataset['Vento'].isnull().sum()
