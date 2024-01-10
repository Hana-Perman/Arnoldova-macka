import matplotlib.pyplot as plt

#VPRAŠANJA
#kaj se definira znotraj funkcije identiteta in česa ne?
#a ta stvar razume da je n celo število??????

#RAZLAGE
#funkcija PRESLIKAVA je uporabljena v funkciji IDENTITETA
#funkcija IDENTITETA je uporabljena v funkciji GRAF 


    
#FUNKCIJE
def preslikava (x1,x2,n):
        list_1 = [2,1]
        list_2 = [1,1]
        y1 = ((list_1 [0] * x1) + (list_1[1]*x2)) % n
        y2 = ((list_2[0] * x1 ) + (list_2[1]*x2)) % n
        return y1, y2
   
def identiteta (n):
    #DEFINICIJE
    #tri tabele, ki imajo povsod ničle
    bazna_mreža = [[0 for _ in range(n)] for _ in range(n)]
    mreža = [[0 for _ in range(n)] for _ in range(n)]
    nova_mreža = [[0 for _ in range(n)] for _ in range(n)]
    a=0
    števec=0

    #vpišem vrednosti v tabelo mreža in bazna mreža, ki sta v izhodišču enake
    for i in range (n):
        for j in range (n):
            bazna_mreža[i][j]  = a
            mreža[i][j] = a
            a+=1
    
    #IZVAJANJE PROGRAMA
    while True:
        števec+=1  
        for i in range (n):
            for j in range (n):
                vrednost = mreža[i][j] #vsako mesto v tabeli ima vrednost, ki jo shranim
                y1,y2= preslikava(i, j,n) #točko preslikam; točka SPREMENI KOORDINATE ampak OHRANI VREDNOST 
                nova_mreža [y1][y2] = vrednost #mreža po preslikavi
        if nova_mreža == bazna_mreža:#če je preslikana mreža enaka bazni končam
            break
        else: #če ni enaka bazni 
            for g in range (n):
                for h in range (n):
                    mreža[g][h] = nova_mreža[g][h] #če ne nadaljujem preslikovanje

    return števec

def graf(največja_mreža):
    n_values = [i for i in range(največja_mreža)] #stranica mreže   
    m_values = [identiteta(x) for x in n_values] # eksponent identitete

    plt.scatter(n_values, m_values, marker='o', s=10  )
    for x, y in zip(n_values, m_values):
        plt.vlines(x, 0, y, linestyle='dotted', color='gray')

    plt.xlabel('velikost mreže')
    plt.ylabel('serija preslikave =identiteta')
    plt.title('identiteta v odvisnosti od mreže')

    plt.legend()
    plt.show()
    
#IZVAJANJE PROGRAMA    
največja_mreža= int(input('Vpiši največjo mrežo: '))
graf(največja_mreža)