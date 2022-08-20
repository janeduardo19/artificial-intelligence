#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:30:44 2022

@author: Jan Eduardo
"""

import numpy as np

entradas = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])
saidas = np.array([[0], [1], [1], [0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358, -0.577, -0.469]])
pesos1 = np.array([[-0.017], [-0.893], [0.148]])

ntreinos = 1000000
taxaAprendizado = 0.3
momentum = 1

def sigmoid(soma):
    """
    Função de ativação utilizada no luga da função degrau. 
    A principal função dela é retornar valores intermediarios entre 0 e 1
    desta forma podemos verificar a probabilidade de uma dado valor 
    se aproximar de 0 ou de 1.

    Parameters
    ----------
    soma : Integer
        Uma váriavel temporária que representa a soma de uma sinapse.

    Returns
    -------
    Float
        Probabilidade de um valor se aproximar de 0 ou de 1.

    """
    return 1 / (1 + np.exp(-soma))


def sigmoideDerivada(sig):
    return sig * (1-sig)

sigDerivada = sigmoid(0.5)
sigDerivada1 = sigmoideDerivada(sigDerivada)

for i in range(ntreinos):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))

    derivadaSaida = sigmoideDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    pesos1Transposta = pesos1.T
    deltaSaidaXpesos = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXpesos * sigmoideDerivada(camadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T
    pesos3 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momentum) + (pesos3 * taxaAprendizado)
    
    camadaEntradaTransposta = camadaEntrada.T
    pesos4 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momentum) + (pesos4 * taxaAprendizado)

    print('Margem de Erro: ' +str(mediaAbsoluta))