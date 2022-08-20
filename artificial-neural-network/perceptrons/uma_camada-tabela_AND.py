#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 13:14:45 2022

@author: jan
@description: Este algoritmo tem como objetivo treinar uma rede neural
simples(uma camada) para aprender o mecanismo lógico de uma tabela 
verdade.
"""

import numpy as np

"""

    Attributes
    -----------    

    entradas : Array of int 
        Contem os valores da tabela verdade.
    saidas : Array of int 
        Contem as saidas reais da tabela.
    pesos : Array of int
        São os valores que serão multiplicados pelas entradas.
    taxaAprendizado : float 
        Define o valor com o qual o peso será atualizado.
"""
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])

taxaAprendizado = 0.5

def Soma(e, p):
    """
    
    Parameters
    ----------
    e : Array of int
        São os valores de entrada.
    p : Array of float
        São os valores do peso.

    Returns
    -------
    Array of float
        Retorna a soma da multiplicações dos valores atribuidos.

    """
    return e.dot(p)

s = Soma(entradas, pesos)

def stepFunction(soma):
    """
    

    Parameters
    ----------
    soma : TYPE
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    """
    if (soma >= 1):
        return 1
    return 0

def calculoSaida(reg):
    """
    

    Parameters
    ----------
    reg : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    s = reg.dot(pesos)
    return stepFunction(s)

def aprendeAtualiza():
    """
    

    Returns
    -------
    None.

    """
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            calcSaida = calculoSaida(np.array(entradas[i]))
            erro = abs(saidas[i] - calcSaida)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizado * entradas[i][j] * erro)
                print('Pesos Atualizados> ' + str(pesos[j]))
            print('Total de Erros: ' + str(erroTotal))

aprendeAtualiza()