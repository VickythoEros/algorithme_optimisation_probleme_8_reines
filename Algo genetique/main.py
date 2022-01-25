from algo_genetique import *
from damier import *


#PROGRAMME PRINCIPALE

# res = [4, 1, 3, 5, 7, 2, 0, 6] 
nombreGenerationPopulation = 100
iteration = 0
nombreIndividu = 50

populationInitiale = initializePopulation(nombreIndividu)
_populationInit = populationInitiale

a = calculProbReproductionIndividu(populationInitiale)
listeDesEnfants = reproductionIndividu(selectionIndividus(a),populationInitiale)
listeEnfantsApresMutation = regenerationPopulation(listeDesEnfants)

print(f"conflits ini : {calculConflits(populationInitiale)} ")
print(f"nouvaux fin: {calculConflits(listeDesEnfants)} ")
print(f" fin: {calculConflits(listeEnfantsApresMutation)} ")
print(f" =========== \n\n")
finMeilleur = verifierConflitPopulation(populationInitiale)

while iteration <= nombreGenerationPopulation:
    _meilleurIndividu = verifierConflitPopulation(_populationInit)
    finMeilleur = _meilleurIndividu if conflits(_meilleurIndividu) < conflits(finMeilleur) else finMeilleur
    _populationSelectionner = calculProbReproductionIndividu(_populationInit)
    _listeDesEnfants = reproductionIndividu(selectionIndividus(_populationSelectionner),_populationInit)
        
    _populationInit = regenerationPopulation(_listeDesEnfants)  
    
    iteration +=1
    
minIndividu = selectionnerMinimuConflitIndividu(_populationInit)
# print(f" fin: {calculConflits(_populationInit)} ")
# print(f" MIni: {minIndividu}  :: {conflits(minIndividu)} ")
print(f" MIni: {finMeilleur}  :: {conflits(finMeilleur)} ")



can.pack(side = TOP, padx = 5, pady = 5)
damier()
for i in range(len(finMeilleur)):
    pion(finMeilleur[i],i)
fen.mainloop()
