def imprime():
    print("esta é uma função")
imprime()

#com parametro
def imprime(n):
    print(n)
imprime("Impressão desse texto")

#com retorno
def potencia(n):
    return n*n
x = potencia(3)
print(f'\na potencia é igual a {x}\n')

def intervalo(inic=1,fim=10):
    for inic in range(1, fim+1):
        print(inic)
x = intervalo(1, 10)
print(f'\n{intervalo()}')