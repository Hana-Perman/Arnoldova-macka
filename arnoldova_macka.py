import matplotlib.pyplot as plt

def preslikava(A, x, n):
    '''funkcija vrne sliko vektorja x z matriko A
    po modulu n
    '''
    y1 = (A[0][0] * x[0] + A[0][1] * x[1]) % n
    y2 = (A[1][0] * x[0] + A[1][1] * x[1]) % n
    return (y1, y2)

def mreža_0(n):
    '''Funkcija zgenerira n x n mrežo s samimi ničlami'''
    return [[0 for _ in range(n)] for _ in range(n)]

def mreža_x(n):
    '''funkcija zgenerira mrežo velikosti n x n:
    [[0,1,2],
     [3,4,5],
     [6,7,8]]
     ...
    '''
    return [[i + n*j for i in range(n)] for j in range(n)]

def premešaj(mreža, A):
    '''Funkcija sprejme mrežo n x n in preslikavo A
    vrednost vsakega mesta v mreži prestavi na novo mesto
    točka SPREMENI KOORDINATE ampak OHRANI VREDNOST
    '''
    n = len(mreža)
    nova_mreža = mreža_0(n)
    for i in range (n):
        for j in range (n):
            vrednost = mreža[i][j] #vsako mesto v tabeli ima vrednost, ki jo shranim
            y0,y1 = preslikava(A, (i,j), n) #točko preslikam; točka SPREMENI KOORDINATE ampak OHRANI VREDNOST 
            nova_mreža[y0][y1] = vrednost #mreža po preslikavi
    return nova_mreža
        

def identiteta(n, A):
    '''funkcija sprejme velikost mreže n in preslikavo A
    na mreži n x n meša točke dokler preslikana mreža ni
    enaka bazni mreži.
    funkcija vrne število iteracij do tega A^števec == I
    '''
    števec = 1
    bazna_mreža = mreža_x(n)
    mreža = mreža_x(n)
    while True:
        nova_mreža = premešaj(mreža, A)
        if nova_mreža == bazna_mreža:#če je preslikana mreža enaka bazni končam
            return števec
        else:
            mreža = nova_mreža
        števec += 1
            
def graf(A, največja_mreža):
    '''
    Funkcija sprejme velikost največje mreže in matriko A.
    Za vse mreže, ki so velike med 2 in največja mreža izračuna periodo.
    Vrednost shrani v dve tabeli in nariše graf. Graf shrani v določeno
    mapo na računalniku

    '''
    n_v = [i for i in range(2, največja_mreža)]  # stranica mreže od 2 naprej
    m_v = []
    for i in n_v:
        n = identiteta(i, A)
        print(i, '->', n)  # sproti izpisujemo, ker traja
        m_v.append(n)
              
    #print(m_v)
    
    plt.scatter(n_v, m_v, marker='o', s=10  )
    #for x, y in zip(n_v, m_v):
         #plt.vlines(x, 0, y, linestyle='dotted', color='gray')

    plt.xlabel('velikost mreže')
    plt.ylabel('serija preslikave =identiteta')
    
    naslov = f'{A[0][0]}-{A[0][1]}//{A[1][0]}-{A[1][1]}'
    plt.title('graf periode v odvisnosti od matrike ' + naslov)
    
    #plt.legend()
    #plt.show()
    return plt.gca(),n_v,m_v

def shrani_graf(A,pot_do_mape,os):
    
    ime_datoteke = f"graf_od_{A[0][0]}_{A[0][1]}_{A[1][0]}_{A[1][1]}.png"
    pot_do_datoteke = pot_do_mape + "\\" + ime_datoteke

    plt.savefig(pot_do_datoteke)
    plt.close()
    

def shrani_vrednosti(A, m_v, n_v, pot_do_mape):
    # Format komponentne matrike A
    A_str = "//".join(["_".join(map(str, row)) for row in A])

    # Join m_v and n_v into strings with commas between the values
    n_values_str = ','.join(map(str, n_v))
    m_values_str = ','.join(map(str, m_v))
    
    # Define the file path for writing m and n values
    file_path = pot_do_mape + "/prazen.txt"

    # Write A, m, and n values to a text file
    with open(file_path, 'a') as f:  # Uporabi 'a' za dodajanje k vsebini datoteke
        f.write(f"A: {A_str}:")
        #f.write(f"n_values: {n_values_str}\n")
        f.write(f"{m_values_str}\n")
        #f.write("\n")  # Dodaj prazno vrstico po vsakem klicu funkcije    
    


'''if __name__ == "__main__":
    print(help('arnoldova_macka'))'''
    
A=[[3,1],[2,1]]
x=2,2
for i in range (6):
    print(preslikava(A,x,3))
    x=preslikava(A,x,3)