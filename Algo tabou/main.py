from tabou import *
from damier import *

if __name__ == '__main__':
    n = 8

    tables_values = []
    # echequier = np.zeros((n, n))  # creation d'une matrice nxn remplie de zeros

    # initialisation
    T = initialize(n) #une solution initiale

    X0 = T
    Xc = T
    list_tabou = []
    critere_arret = 100
    best_voisin =[]
    while critere_arret >= 0 :

        best_voisin = regeneration_s(Xc)
        print(conflits(best_voisin))
        if best_voisin not in list_tabou:
            if conflits(best_voisin) < conflits(X0):
                X0 = best_voisin

                Xc = best_voisin
            tables_values.append(best_voisin)
        critere_arret -=1


    
    print(conflits(best_voisin))
        
    can.pack(side = TOP, padx = 5, pady = 5)
    damier()
    for i in range(len(best_voisin)):
        pion(best_voisin[i],i)
    fen.mainloop()