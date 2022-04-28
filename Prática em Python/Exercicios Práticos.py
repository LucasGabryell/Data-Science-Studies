#  1. Faça um programa que tenha uma função chamada amplitude. A função deve receber uma lista e imprimir a amplitude.
# Crie também um código para testar sua função
# 2. Faça uma função que receba uma string e imprima esta string na forma vertical
# Por exemplo, se receber python, deve imprimir
# р
# y
# t
# h
# O
# n
# Dica: uma string do python funciona como uma lista!
# Crie também um código para testar sua função
# 3. Crie um programa que leia o peso de uma carga em números inteiros. Se o peso for até 10 kg, informe que o valor será
# de R$ 50,00. Entre 11 e 20 kg, informe que o valor será de R$ 80. Se for maior que 20 informe que o transporte não é
# aceito. Teste vários pesos.

# 1
from random import randint


def calc_amplitude(n):
    amplitude = max(n) - min(n)
    return amplitude


numeros = []
for i in range(1, 6):
    x = randint(1, 20)
    numeros.append(x)
print(f'{max(numeros)} - {min(numeros)}')
print(f"Amplitude: {calc_amplitude(numeros)}")


# 2

def vertical(key):
    for n in range(0, len(key)):
        print(key[n])

palavra = str(input("Digite uma palavra"))
vertical(palavra)

# 3

def teste_peso(n):
    if n <= 10:
        print("R$ 50,00")
    elif 11 <= n <= 20:
        print("R$ 80,00")
    elif n > 20:
        print("O transporte não é aceito!")


while True:
    peso = float(input("Digite o peso da carga: "))
    if peso < 0:
        print("Programa finalizado!")
        break
    teste_peso(peso)
