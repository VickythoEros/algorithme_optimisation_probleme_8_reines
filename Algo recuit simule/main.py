from recuit import *
from damier import *


if __name__ == '__main__':
    n = 8

    tables_values = []
    # echequier = np.zeros((n, n))  # creation d'une matrice nxn remplie de zeros

    temperature_initiale = 80 #compris entre 100 et 1
    temperature_finale = 0.1
    temperature_actuelle = temperature_initiale
    cool = 0.99
    
    
    # initialisation
    valeur_initiale = initialize(n)
    valeur_actuelle = valeur_initiale
    solution = valeur_actuelle
    
    
    
    while temperature_actuelle > temperature_finale :
        
        voisin = generation_voisin(valeur_actuelle)
        
        cout_conflit =  conflits(valeur_actuelle) - conflits(voisin) 
        
        if cout_conflit > 0:
            valeur_actuelle = voisin
        else:
            r = rd.uniform(0,1)
            if r > math.exp(-cout_conflit/temperature_actuelle) :
                valeur_actuelle = voisin

        temperature_actuelle = temperature_actuelle * cool


    print(conflits(valeur_actuelle))
        
    can.pack(side = TOP, padx = 5, pady = 5)
    damier()
    for i in range(len(valeur_actuelle)):
        pion(valeur_actuelle[i],i)
    fen.mainloop()
