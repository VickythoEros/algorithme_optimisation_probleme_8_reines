# MY IMPORTS
import math

# import numpy as np
import random as rd


# MY FUNCTIONS


def initialize(n):
    """
    cette fonction permet de placer les reines de façon aleatoire
    :param n: le nombre de reine
    :return: la position des reine dans un tableau
    """
    return [rd.randint(0, n - 1) for i in range(n)]


def conflits(T):
    """
    Attend en parametre un tableau des emplacements des 8 REINES
    dans la matrice
    :param T:
    :return: S
    """
    S = 0
    n = len(T)
    for i in range(n):
        m = 0
        for j in range(n):
            if T[i] == T[j] or abs(i - j) == abs(T[i] - T[j]):
                m += 1
        S += m - 1
    return S

def generation_voisin(element):
    _copyElement = element.copy()
    listElement = []
    for i in range(20):
        _copyElement = element.copy()
        v = rd.randint(0,7)
        v1 = rd.randint(0,7)
        _copyElement[v] = v1
        listElement.append(_copyElement)
    listConflit = [conflits(element) for element in listElement]
    indiceMin = listConflit.index(min(listConflit))
         
    return listElement[indiceMin]
