import pandas as pd
import seaborn as srn
import statistics as sts


#importar dados
dataset = pd.read_csv("Churn.csv", sep=";")
#visulizar
print(dataset.head())


#tamanho
print(dataset.shape)


#primeiro problema é dar nomes as colunas
dataset.columns = ["Id","Score","Estado","Genero","Idade","Patrimonio","Saldo","Produtos","TemCartCredito",
                    "Ativo","Salario","Saiu"]


#visulizar
dataset.head()


#explorar dados categoricos
#estado
agrupado = dataset.groupby(['Estado']).size()
print(agrupado)

agrupado.plot.bar(color='gray')

#genero
agrupado = dataset.groupby(['Genero']).size()
print(agrupado)
agrupado.plot.bar(color='gray')

#explorar colunas numéricas
#score
dataset['Score'].describe()
srn.boxplot(dataset['Score']).set_title('Score')
srn.distplot(dataset['Score']).set_title('Score')

#idade
dataset['Idade'].describe()
srn.boxplot(dataset['Idade']).set_title('Idade')
srn.distplot(dataset['Idade']).set_title('Idade')

#saldo
dataset['Saldo'].describe()
srn.boxplot(dataset['Saldo']).set_title('Saldo')
srn.distplot(dataset['Saldo']).set_title('Saldo')

#salário
dataset['Salario'].describe()
srn.boxplot(dataset['Salario']).set_title('Salario')
srn.distplot(dataset['Salario']).set_title('Salario')

#contamos valores NAN
#genero e salário
dataset.isnull().sum()

#salarios
#remover nas e substiutir pela mediana
dataset['Salario'].describe()
mediana = sts.median(dataset['Salario'])
print(mediana)

#substituir NAN por mediana
dataset['Salario'].fillna(mediana, inplace=True)

#Verificamos se NAN não existem mais
dataset['Salario'].isnull().sum()

#genero, falta de padronização e NAs
agrupado = dataset.groupby(['Genero']).size()
print(agrupado)

#total de Nas
dataset['Genero'].isnull().sum()

#preenche NAs com Masculino (moda)
dataset['Genero'].fillna('Masculino', inplace=True)

#verificamos novamente NANs
dataset['Genero'].isnull().sum()

#padroniza de acordo com o dominio
dataset.loc[dataset['Genero'] == 'M', 'Genero'] = "Masculino"
dataset.loc[dataset['Genero'].isin(['Fem', 'F']), 'Genero'] = "Feminino"
#visualiza o resultado
agrupado = dataset.groupby(['Genero']).size()
print(agrupado)

#idades fora do dominio
dataset['Idade'].describe()

#visualizar
dataset.loc[(dataset['Idade'] <  0 )  | ( dataset['Idade'] >  120) ]

#calular a mediana
mediana = sts.median(dataset['Idade'])
print(mediana)

#substituir
dataset.loc[(dataset['Idade'] < 0) | (dataset['Idade'] > 120), 'Idade'] = mediana

#verificamos se ainda existem idades fora do domínio
dataset.loc[(dataset['Idade'] <  0 )  | (dataset['Idadprint(agrupado)'] >  120) ]

#dados duplicados, buscamos pelo ID
dataset[dataset.duplicated(['Id'],keep=False)]

#excluimso pelo ID
dataset.drop_duplicates(subset="Id", keep='first',inplace=True)
#buscamos duplicados
dataset[dataset.duplicated(['Id'], keep=False)]
print()

#estado foram do domínio
agrupado = dataset.groupby(['Estado']).size()
print(agrupado)

#atribuomos RS (moda)
dataset.loc[dataset['Estado'].isin( ['RP','SP','TD']), 'Estado'] = "RS"
agrupado = dataset.groupby(['Estado']).size()
#verificamos o resultado
print(agrupado)

#outliers em salário, vamos considerar 2 desvios padrão
desv = sts.stdev(dataset['Salario'])
print(desv)

#definir padrão como maior que 2 desvios padrão
#checamos se algum atende critério
dataset.loc[dataset['Salario'] >= 2 * desv]


#vamos atualiar salarios para mediana, calculamos
mediana = sts.median(dataset['Salario'])
print(mediana)

#atribumos
dataset.loc[dataset['Salario'] >=  2 * desv, 'Salario'] = mediana
#checamos se algum atende critério
dataset.loc[dataset['Salario'] >=  2 * desv ]
print(dataset.head())
print(dataset.shape)
