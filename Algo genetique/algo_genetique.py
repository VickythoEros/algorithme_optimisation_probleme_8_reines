import random as rd
from math import *



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
                m +=1
        S += m -1
    return S


def calculConflits(population):
    return [conflits(individu) for individu in population]


#POPULATION INITIALE

def initializeIndividu(n):
    """
    cette fonction permet de placer les reines de façon aleatoire
    :param n: le nombre de reine
    :return: la position des reine dans un tableau
    """
    return [rd.randint(0,n-1) for i in range(n) ]


def initializePopulation(n):
    return [initializeIndividu(8) for i in range(n)]


#SELECTION

def calculPerformance(individu):
    valeurMesuree = 1
    valeurCalculee = conflits(individu)
    valeurFonctionObjective = (valeurMesuree - valeurCalculee)**2
        
        
    return valeurFonctionObjective


def calculProbReproductionIndividu(population):
    #individu = {indice : [performance,poids,probReproduction]}
    a = 1.3
    _population = population
    taillePopulation = len(_population)
    
    
    listePopulation = {}
    for i in range(taillePopulation):
        table = []
        table.append(calculPerformance(_population[i]))
        listePopulation[i] = table
    
    listePerformancesTriee = {k: v for k, v in sorted(listePopulation.items(), key=lambda item: item[1])}
    
    incremente = 0
    for individu,valeur in listePerformancesTriee.items():
        poidIndividu = (taillePopulation - incremente)**a
        listePerformancesTriee[individu].append(poidIndividu)
        incremente +=1
        
    sommePoids = 0
    for key,valeur in listePerformancesTriee.items():
        sommePoids += listePerformancesTriee[key][0]
    
    for individu,valeur in listePerformancesTriee.items():
        
        probReproduction = (valeur[1])/(sommePoids/taillePopulation)
        listePerformancesTriee[individu].append(floor(probReproduction*100))
        


    return listePerformancesTriee


def selectionIndividus(population):
    _population = population
    taillePopulation = len(_population)
    individuSelectionner={}
    sommeProbReproduction = 0
    
    for individu,valeur in _population.items():
        sommeProbReproduction += valeur[2]
    
    valeurDeSelection = sommeProbReproduction/taillePopulation
    
    for individu,valeur in _population.items():
        if valeur[2] >= valeurDeSelection:
            individuSelectionner[individu] = valeur
    
    return individuSelectionner
    
    

#REPRODUCTION

def adaptationValeurIndividu(individu):
    valeurIndividu = [floor(i)%7 for i in individu]
    return valeurIndividu


def selectMeilleursEnfant(enfant1,enfant2,enfant3):
    listeEnfants = [adaptationValeurIndividu(enfant1),adaptationValeurIndividu(enfant2),adaptationValeurIndividu(enfant3)]
    listeConflits = [conflits(enfant1),conflits(enfant2),conflits(enfant3)]
    listeConflitsSecondaire = listeConflits.copy()
    indiceMinConflitEnfant1 = listeConflitsSecondaire.index(min(listeConflitsSecondaire))
    del listeConflitsSecondaire[indiceMinConflitEnfant1]
    indiceMinConflitEnfant2 = listeConflitsSecondaire.index(min(listeConflitsSecondaire))
    
    return listeEnfants[indiceMinConflitEnfant1],listeEnfants[indiceMinConflitEnfant2]



def calculeProduitValeurList(valeur,listValeur):
    return [i*valeur for i in listValeur]



def additionDeuxListe(liste1,liste2):
    tailleListe = len(liste1)
    sommeListe=[]
    for i in range(tailleListe):
        sommeListe.append(liste1[i] + liste2[i])
    
    return sommeListe
    

def reproductionIndividu(population,initialePopulation):
    _population = population
    _initialePopulation = initialePopulation
    tailleInitialePopulation = len(_initialePopulation)
    listeGenerations = []
    listeIndividuSelmectionner =[]
    listeIndividuSelmectionner =[_initialePopulation[indice] for indice in _population.keys()]
    tailleListeGenerations = len(listeGenerations)
    tailleIndividuSelection = len(listeIndividuSelmectionner)
    
    while tailleListeGenerations < tailleInitialePopulation :
        nombreAleatoire1 = rd.randint(0,tailleIndividuSelection-1)
        nombreAleatoire2 = rd.randint(0,tailleIndividuSelection-1)
        parent1 = listeIndividuSelmectionner[nombreAleatoire1]
        parent2 = listeIndividuSelmectionner[nombreAleatoire2]
        
        enfant1 = additionDeuxListe(calculeProduitValeurList(0.5,parent1) ,calculeProduitValeurList(0.5,parent2))
        enfant2 = additionDeuxListe(calculeProduitValeurList(1.5,parent1), calculeProduitValeurList(-0.5,parent2))
        enfant3 = additionDeuxListe(calculeProduitValeurList(-1.5,parent1), calculeProduitValeurList(0.5,parent2))
     
        gene1 , gene2 = selectMeilleursEnfant(enfant1,enfant2,enfant3)
        listeGenerations.append(gene1)
        listeGenerations.append(gene2)
        tailleListeGenerations = len(listeGenerations)
        
    return listeGenerations
        
        
    
#MUTATION DES INDIVIDU SELECTIONNER

def mutationIndividu(element):  
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
           
    
def regenerationPopulation(population):
    _population = population
    taillePopulation = len(_population)
    
    for individu in _population:
        indiceIndividu = _population.index(individu)
        listeProvisoire = _population.copy()
        del listeProvisoire[indiceIndividu]
        
        if individu in listeProvisoire:
            _population[indiceIndividu] = mutationIndividu(individu)
    
    return _population
            

def verifierConflitPopulation(population):
    
    conflitliste = calculConflits(population)
    indeiceMinimu = conflitliste.index(min(conflitliste))
  
    return population[indeiceMinimu]

def selectionnerMinimuConflitIndividu(population):
    _population = population
    indiceMin = _population.index(min(_population))
    return population[indiceMin]

