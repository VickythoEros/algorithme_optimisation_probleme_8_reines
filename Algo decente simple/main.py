from descente import *
from damier import *






if __name__ == '__main__':
    n = 8
    s = 0
    tables_values = []
    is_ok = False

    # initialisation
    #T = [7, 0, 1, 3, 1, 5, 2, 4]
    #T = [2,5,6,1,4,4,7,3]
    
    T = initialize(n)
    
    s = conflits(T)
    tables_values.append(s)
    valeurFinale = []
    while is_ok == False:
        T1 = regeneration_s(T)
        print(T1)
        s1 = conflits(T1)
        if s1 > tables_values[-1] :
            is_ok = True
            valeurFinale = T1
        else:
            T = T1
            tables_values.append(s1)

    print(conflits(valeurFinale))
    print((valeurFinale))
    
    can.pack(side = TOP, padx = 5, pady = 5)
    damier()
    for i in range(len(valeurFinale)):
        pion(valeurFinale[i],i)
    fen.mainloop()