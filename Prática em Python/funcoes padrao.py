#funções internas
import random

print((abs(-200)))
lst = [1,2,3,20,40,2]
print("Maior valor:", max(lst))
print("Menor valor:", min(lst))
print("Soma:", sum(lst))
print("Arredondamento:", round(2.34567, 2))

from statistics import *
print("Media:", mean(lst))
print("Mediana:", median(lst))
print("Moda:", mode(lst))

#Desvio padrão da amostra
print("Desvio padrão:", stdev(lst))
#Variancia da amostra
print("Variância:", variance(lst))

from numpy import *
a = random.random((8,8))
print(type(a))
print(a)
