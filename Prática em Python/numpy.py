import numpy as np

#criar uma matriz unidimensional
mt = np.array([12,34,26,18,10])
print(mt)
print(type(mt))
print("---------")

#criar o array com tipo especifico
#criar o array como float de 64 bits
mtfloat = np.array([1,2,3], dtype = np.float64)
print(mtfloat)
print(type(mtfloat))
mtint = np.array([1,2,3], dtype=np.int32)
print(mtint)
print(type(mtint))
print("---------")

#mudar o tipo do array
mtnew = np.array([1.4, 3.6, -5.1, 9.42, 4.999999])
print(mtnew)
#quando transforma de float para int os valores são truncados
mtnewint = (mtnew.astype(np.int32))
print(mtnewint)
print("---------")

#pode ser feito o inverso tambem
mt5 = np.array([1, 2, 3, 4])
print(mt5)
mt6 = mt5.astype(float)
print(mt6)
print("---------")

#mais de uma dimensão
#criar uma matriz bidimensional
mt7 = np.array([[7, 2, 23], [12, 27, 4], [5, 34, 23]])
print(mt7)
print("---------")

#criar arrays vazias tipificadas
#empty significa que não são inicializados, não que são vazios
vazio = np.empty([3, 2], dtype=int)
print(vazio)
print("---------")
#cria uma matriz 4x3 com valores zero
zeros = np.zeros([4, 3])
print(zeros)
print("---------")
#com valores igual a um
um = np.ones([5, 7])
print(um)
print("---------")
#criar matriz quadrada com diagonal principal com valores 1 e outros valres zero
diagonal = np.eye(5)
print(diagonal)
print("---------")

#valores aleatorios entre 0 e 1
ale = np.random.random((5))
print(ale)
print("---------")
#valores aleatorios distr. normal contando negativos
ale2 = np.random.randn((5))
print(ale2)
print("---------")
#valores aleatorios 3x4
ale3 = (10*np.random.random((3, 4)))
print(ale3)

#outra forma de gerar aleatorios
#uso de semente

gnr = np.random.default_rng(1)
ale5 = gnr.random(3)
print(ale5)

#gerar inteiros
print("---------")
ale6 = gnr.integers(10, size=(3, 4))
print(ale6)

#unique remove repetições
print("---------")
j = np.array([11, 12, 13,14, 15, 16, 17, 18, 19, 20])
j = np.unique(j)
print(j)
print("---------")

#funções específicas
#criar a matriz bidimencional k
k = np.array([[17, 22, 43], [27, 25, 14,], [15, 24, 32]])
print(k)
#mostra um elemento específico da matriz
print(k[0][1])
#mostra o tamanho das dimensões da matriz k
print(k.shape)
print("---------")

#Funções Matemáticas
#Mostra o maior valor da matriz k
print(k.max())
#Mostra o menor valor da matriz k
print(k.min())
#Mostra a soma dos valores da matriz k
print(k.sum())
#Mostra o valor da média dos valores da matriz k
print(k.mean())
#Mostra o maior valor do desvio padrão dos valores da matriz k
print(k.std())
print("---------")

#funções universais, aplicadas a todos os elementos
#Mostra o valor da raiz quadrada de todos elementos
k1 = np.array([1, 4, 9, 16, 25, 36])
print(np.sqrt(k1))
#Mostra o valor da exponencial de todos elementos
print(np.exp(k1))
print("---------")

#Extração de elementos
m = np.array([1, 2, 3, 4, 5, 6])
#mostra o elemento da posição 2
print(m[1])
print("---------")
#Mostra o array criado a partir da posição 0, dois elementos
print(m[0:2])
print("---------")
#Mostra o array criado a partir da segunda posição
#até o todo o restante do array
print(m[1:])
print("---------")
#Mostra o array criado a partir da antepenúltima posição até o final
print(m[-3:])
print("---------")

#Extração de linhas e colunas
l = np.array([[4, 5], [6, 1], [7, 4]])
print(l)
print("---------")
#primeira linha, todas as colunas
l_linha_1 = l[0, :]
print(l_linha_1)
print("---------")
#segunda linha
l_linha_2 = l[1, :]
print(l_linha_2)
print("---------")
#terceira linha
l_linha_3 = l[2, :]
print(l_linha_3)
print("---------")
#todas as linhas, primeira colunas
l_linha_1 = l[:, 0]
print(l_linha_1)
print("---------")
#todas as linhas, segunda coluna
l_linha_2 = l[:, 1]
print(l_linha_2)
print("---------")

#adição e multiplicação de matrizes
n = np.array([[1, 2], [3, 4]])
o = np.array([[1, 1], [1, 1]])
res1 = n+o
print(res1)
print("---------")
res2 = n*o
print(res2)
print("---------")
p = np.array([[1, 2], [3, 4], [5, 6]])
q = np.array([[2,1]])
print(p+q)
print("---------")

#transposição, rearranja um conjunto de 15 elementos de 0 a 14 em 3 linhas e 5 colunas
f = np.arange(15).reshape((3,5))
#mostra a matriz transposta entre linha e coluna
print(f)
print("---------")
s = f.T
print(s)
print("---------")

#expressões lógicas
#usando where
#criando matriz com valores aleatórios positivos e negativos
v = np.random.randn(4,4)
print(v)
#criando matriz com valores booleanos baseados no array v
x = (v > 0)
print(x)
#criando matriz com valores -1 e 1 baseados nos valores do array x
z = np.where(x > 0, 1, -1)
print(z)