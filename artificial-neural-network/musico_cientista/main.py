# Deixando a entrada ordenada os pesos serão sempre os mesmo sendo 0 1 0
# e todas as vezes tive um mínimo de 12 interações.
# Com a ordem de entrada randomica e o peso em 1 as iterações variam entre
# 8 a 20, mas ele sempre chega no resultado esperado.
# Quanto a taxa de Aprendizagem ao diminuir ela, eu obtive entre 8 e 20 iterações com ordem randomica
# e 12 iterações com a lista ordenada. Mesmo com os pesos fracionados a rede é capaz de obter
# o resultado esperado.

import random

bias = 1
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
saidas = [0, 0, 1, 1]
pesos = [0, 0, 0]
escolhas = [0, 1, 2, 3]
taxaAprendizado = 0.1

def stepFunction(soma):
    if soma > 0:
        return 1
    elif soma <= 0:
        return 0

def calcSaida(entradas, bias, pesos):
    soma = (bias * pesos[0]) + (entradas[0] * pesos[1]) + (entradas[1] * pesos[2])
    return stepFunction(soma)

def aprendeAtualiza():
    cont = 0
    iterações = 0
    while (cont != 4):
        cont = 0
        random.shuffle(escolhas)
        for i in range(len(saidas)):
            iterações += 1
            index = escolhas[i]
            saidaObtida = calcSaida(entradas[index], bias, pesos)
            if saidaObtida == saidas[index]:
                cont = cont + 1
            else:
                print("Erro, atualizando pesos")
                erro = saidas[index] - saidaObtida
                for j in range(len(pesos)):
                    if j == 0:
                        pesos[j] = pesos[j] + (erro * taxaAprendizado * bias)
                    else:
                        pesos[j] = pesos[j] + (erro * taxaAprendizado * entradas[index][j-1])
                    #print('Pesos Atualizados> ' + str(pesos[j]))

            #print(('Erro: ' + str(erro)))
    print('Iterações: ' + str(iterações))
    print(pesos[0], pesos[1], pesos[2])

aprendeAtualiza()