"""Problema consiste na criação de um algorimo genético. Cromossomos são gerados aleatoriamente e compostos por 44
bits. A partir dele devemos definir x e y com 22 bits cada. Esses números binários devem ser definidos pra decimal. A
partir disso devem ser postos no range denifido que é de -100 até 100, multiplicamos por 200 e divimos cada um por
2²² -1 para colocar os, números dentro do range e por fim movemos 100 casas pra, esquerda subtraindo por 100. Após
isso eles são aplicados na F6 como forma de teste de aptidão. Então são gerados 100 filhos utilizando o método da
roleta pra escolha dos casaia. Deles são pegos 99 filhos aleatórios e o pai mais apto.Esse individuos passam
novamente pelos processos até que seja encontrada a solução ou as gerações acabem. """

import random
import math


# Criar um cromossomo
def gera_cromossomo():
    cromossomo = ""
    for i in range(44):
        cromossomo += str(random.randint(0, 1))
    return cromossomo


# Gerar a primeira populacao
def inicia_populacao():
    p1 = []
    for i in range(100):
        p1.append(gera_cromossomo())
    return p1


# Divide o cromossomo entre x e y
def divide_cromossomo(populacao):
    x = []
    y = []
    for i in range(100):
        temp = populacao[i]
        x.append(temp[:22])
        y.append(temp[22:])
    return x, y


# Converter o x e o y para números reais
def converte_bin_real(x, y):
    binario_x = []
    binario_y = []
    dec_x = []
    dec_y = []
    k = 0
    for i in range(100):
        binario_x.append(int(x[i]))
        binario_y.append(int(y[i]))
    while k < 100:
        aux_dec_x = 0
        aux_dec_y = 0
        n = len(str(binario_x[k]))
        j = 0
        while n >= 0:
            resto_x = binario_x[k] % 10
            resto_y = binario_y[k] % 10
            aux_dec_x = aux_dec_x + (resto_x * (2**j))
            aux_dec_y = aux_dec_y + (resto_y * (2**j))
            n = n - 1
            j = j + 1
            binario_x[k] = binario_x[k] // 10
            binario_y[k] = binario_y[k] // 10
        dec_x.append(aux_dec_x)
        dec_y.append(aux_dec_y)
        k = k + 1
    return dec_x, dec_y


# Ajustar o range do decimal para se enquadrar a formula
def ajusta_range(x, y):
    dec_x, dec_y = converte_bin_real(x, y)
    valor_real_x = []
    valor_real_y = []

    for i in range(100):
        aux_x = ((dec_x[i] * 200)/((2**22) - 1)) - 100
        aux_y = ((dec_y[i] * 200)/((2**22) - 1)) - 100
        valor_real_x.append(aux_x)
        valor_real_y.append(aux_y)

    return valor_real_x, valor_real_y


# Aplica x e y a formula F6
def aplica_F6(x, y):
    x_fim, y_fim = ajusta_range(x, y)
    F6 = []

    for i in range(100):
        soma_xy = (x_fim[i]**2) + (y_fim[i]**2)
        raiz_xy = math.sqrt(soma_xy)
        sen_raiz = math.sin(math.radians(raiz_xy))
        valor_F6 = 0.5 - (((sen_raiz**2) - 0.5) / (1 + (0.001 * soma_xy))**2)
        F6.append(valor_F6)
    return F6


# Seleciona o pai seguindo o metodo da roleta
def selecao_roleta(aptidao_F6):
    aux_soma = 0
    somatoria = 0
    for i in range(100):
        somatoria = somatoria + aptidao_F6[i]
    rand_aptidao = random.uniform(0, somatoria)
    for i in range(100):
        aux_soma = aux_soma + aptidao_F6[i]
        if aux_soma >= rand_aptidao:
            return i


# Seleciona o melhor individuo da geração
def seleciona_melhor(aptidao_F6):
    aux = 0
    index = 0
    for i in range(100):
        if aptidao_F6[i] >= aux or aux == 0:
            aux = aptidao_F6[i]
            index = i

    return index


# Escolhe 2 pais e gera os filhos deles
def proxima_geracao(populacao, aptidao_F6):
    pai1 = populacao[selecao_roleta(aptidao_F6)]
    pai2 = populacao[selecao_roleta(aptidao_F6)]
    primeiro_filho = ''
    segundo_filho = ''

    tax_crossover = random.uniform(0, 1)

    if tax_crossover >= 0.6 and tax_crossover <= 0.9:
        ponto_corte = random.randint(1, 42)
        primeiro_filho = pai1[:ponto_corte] + pai2[ponto_corte:]
        segundo_filho = pai2[:ponto_corte] + pai1[ponto_corte:]
    elif tax_crossover < 0.6 or tax_crossover > 0.9:
        primeiro_filho = pai1
        segundo_filho = pai2

    for i in range(43):
        tax_mutacacao = random.uniform(0, 1)
        if tax_mutacacao >= 0.001 and tax_mutacacao <= 0.05:
            if primeiro_filho[i] == '1':
                aux = list(primeiro_filho)
                aux[i] = '0'
                primeiro_filho = "".join(aux)
            elif primeiro_filho[i] == '0':
                aux = list(primeiro_filho)
                aux[i] = '1'
                primeiro_filho = "".join(aux)
            if segundo_filho[i] == '1':
                aux = list(segundo_filho)
                aux[i] = '0'
                segundo_filho = "".join(aux)
            elif segundo_filho[i] == '0':
                aux = list(segundo_filho)
                aux[i] = '1'
                segundo_filho = "".join(aux)

    return primeiro_filho, segundo_filho

t = 0
populacao = inicia_populacao()
populacao_atual = []
while t < 600:
    t = t + 1
    i = 0
    aptidao = []
    populacao_atual = []
    x, y = divide_cromossomo(populacao)
    x1, y1 = ajusta_range(x, y)
    aptidao = aplica_F6(x, y)
    # Se forem 400 gerações chega no valor binario ideal
    while i < 50:
        filho1, filho2 = proxima_geracao(populacao, aptidao)
        populacao_atual.append(filho1)
        populacao_atual.append(filho2)
        i = i + 1
    mi = seleciona_melhor(aptidao)
    print(f'Geração:',t,'- Bin:',populacao[mi],'- x:',round(x1[mi], 5),'- y:',round(y1[mi], 5),'- Aptidão:',aptidao[mi])
    deleta = random.randint(0, 99)
    populacao_atual[deleta] = populacao[mi]
    populacao = populacao_atual