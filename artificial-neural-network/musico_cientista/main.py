import random

bias = 1
peso_b = 0
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
saidas = [0, 0, 1, 1]
pesos = [0, 0]
escolhas = [0, 1, 2, 3]
taxaAprendizado = 1


def calculoSaida(entrada):
    pass

def aprendeAtualiza():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        random.shuffle(escolhas)
        for i in range(len(saidas)):
            calcSaida = calculoSaida(entradas[escolhas[i]])
