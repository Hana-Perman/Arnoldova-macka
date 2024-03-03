import numpy as np
import matplotlib.pyplot as plt
import copy
from PIL import Image, ImageDraw, ImageFont

'''RAČUNSKE FUNKCIJE:
-multiply_matrixes
-modul
-potenciraj_matriko
-identiteta'''


def multiply_matrices(A, B):
    """
    Funkcija za množenje dveh matrik.
    """
    # Ustvarimo prazno matriko za rezultat
    result = [[0 for _ in range(2)] for _ in range(2)]
    # Izvedemo množenje matrik
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


def modul(A, n):
    """ta funkcija rezultate zračuna po modulu stranice mreže"""
    m_A=[[0,0],[0,0]]
    m_A[0][0]= A[0][0] % n
    m_A[1][0] = A[1][0] % n
    m_A[0][1]= A[0][1] % n
    m_A[1][1]= A[1][1] % n
    return m_A

def potenciraj_matriko(A,potenca,n):
    '''Funkcija potencira matriko na želeno potenco in
    jo po vsakem potenciranju po modulu zmanjša'''
    B = copy.deepcopy(A)
    for i in range (potenca-1):
        A=modul(multiply_matrices(A, B),n)
        print('A^',i+2,' = ',A)
    return A

def identiteta_optimal(n, A):
    '''Funkcija s potencira (in računa po modulu) matriko dokler ta ni enaka
    matriki identiteta. Potenca=perioda+1'''
    B = copy.deepcopy(A)
    i_A = [[1, 0], [0, 1]]
    m_A = modul(A,n)
    števec = 1
    while True:
        if m_A == i_A:
            return števec
        else:
            m_A= modul(multiply_matrices(m_A, A),n) 
        števec += 1
        # print('števec: ',števec)
        
'''FUNKCIJE, KI DELAJO Z GRAFI
-graf_optimal
-shrani graf
-shrani vrednosti'''

def graf_mreža_perioda(A,največja_mreža):
    '''Funkcija nariše graf periode pri dani matriki.'''
    n_v = []
    m_v = []
    B=copy.deepcopy(A)
    for i in range(2,največja_mreža + 1):
        n_v.append(i)
        perioda=identiteta_optimal(i, A)
        
        m_v.append(perioda)
        print(i, '->', perioda) 
    
    plt.scatter(n_v, m_v, marker='o', s=10)
    for x, y in zip(n_v, m_v):
         plt.vlines(x, 0, y, linestyle='dotted', color='gray')
    plt.xlabel('velikost mreže')
    plt.ylabel('serija preslikave = identiteta')
    
    naslov = f'{B[0][0]}_{B[0][1]}_{B[1][0]}_{B[1][1]}'
    plt.title('graf periode v odvisnosti od matrike ' + naslov)
   #5 plt.show()
    A=B
    return plt.gca(), n_v, m_v


def shrani_graf(B, pot_do_mape, os):
    '''Funkcija shrani grafe v želeno mapo'''
    
    ime_datoteke = f"graf_od_{B[0][0]},{B[0][1]},{B[1][0]},{B[1][1]}.png"
    pot_do_datoteke = pot_do_mape + "\\" + ime_datoteke
    plt.savefig(pot_do_datoteke)
    plt.close()
    
    

def shrani_vrednosti(A, m_v, n_v, pot_do_mape):
    '''Funckija zapiše matriko, velikosti mreže in velikosti period v prazen txt'''
    A_str = "//".join(["_".join(map(str, row)) for row in A])
    n_values_str = ','.join(map(str, n_v))
    m_values_str = ','.join(map(str, m_v))
    file_path = pot_do_mape + "/prazen.txt"
    with open(file_path, 'a') as f:  # Uporabi 'a' za dodajanje k vsebini datoteke
        f.write(f"A: {A_str}:")
        f.write(f"n_values: {n_values_str}\n")
        f.write(f"{m_values_str}\n")
        f.write("\n")  # Dodaj prazno vrstico po vsakem klicu funkcije


def graf_matrika_perioda (a,b, stalna_mreža):
    števec=0
    tabela_matrik=[]
    tabela_period=[]
    for a in range(1,10):
        for b in range(a,10):
            A = [[1+(a*b), a],
                [b, 1]]
            števec+=1
            tabela_matrik.append(A)
            print(števec,'. matrika:',A)
    
    '''za vsako matriko bi izračunala periodo pri neki velikosti mreže,
    to shranim v dve tabeli'''        
    for i in range (števec):
        print("računam periodo ",i)
        tabela_period.append(identiteta_optimal(stalna_mreža, tabela_matrik[i]))
    
    '''narišem graf'''
    x_values= range(števec)
    y_values = tabela_period

    plt.scatter(x_values,y_values, marker='o', s=10  )
    #for x, y in zip(x_values,y_values):
        #plt.vlines(x, 0, y, linestyle='dotted', color='gray')
    plt.xlabel('matrika')
    plt.ylabel('perioda')
    naslov = f'{stalna_mreža}'
    plt.title('graf periode v odvisnosti od matrike '+naslov)
    
    return plt.gca(),tabela_matrik, tabela_period
    
def shrani_graf2(stalna_mreža, pot_do_mape, os):
    '''Funkcija shrani graf periode v odvisnosti od matrike v želeno mapo'''
    ime_datoteke = f"graf_od_{stalna_mreža}.png"
    pot_do_datoteke = pot_do_mape + "\\" + ime_datoteke
    plt.savefig(pot_do_datoteke)
    plt.close()
    #plt.show()
    
def shrani_vrednosti2(stalna_mreza, tabela_matrik, tabela_period, pot_do_mape):
    '''Funcija shrani stalno, tabelo matrik in tabelo period v prazen2.txt'''
    stalna_mreza_str = str(stalna_mreza)
    matrike_str = "||".join(["//".join([",".join(map(str, vrstica)) for vrstica in matrika]) for matrika in tabela_matrik])
    tabela_period_str = ','.join(map(str, tabela_period))
    file_path = pot_do_mape + "/prazen2.txt"
    
    # Odpremo datoteko za pisanje
    with open(file_path, 'w') as file:
        # Zapišemo vrednosti v datoteko
        file.write(stalna_mreza_str + '\n')
        file.write(matrike_str + '\n')
        file.write(tabela_period_str)
        
        
        
'''FUNKCIJE, KI DELAJO S SLIKAMI:
-preslikava
-display_image
-napiši_sporočilo
-skrij_sporočilo
-prikaži_sporočilo
-prikaži iterat'''

def preslikava(slika, A, N):
    '''Funkcija sprejme objekt Image in matriko
        vrne novo sliko ki je rezultat preslikave
        Arnoldove mačke'''
    sl = slika.load() #PixelAccess objekt
    nova = Image.new('RGB', (N,N))
    for i in range(N):
        for j in range(N):#za vse pixle na sliki
            p = sl[j, i] # Spremenjeno i in j za dostopanje do pixela
            t1 = np.array([i,j])
            t2 = (A @ t1) % N  # Spremenjena uporaba matričnega množenja
            nova.putpixel((int(t2[1]), int(t2[0])), tuple(p)) # Spremenjena uporaba tuple() za določitev položaja in barve piksla
    return nova

def display_image(image, time):
    plt.imshow(image)
    plt.axis('off')
    plt.show(block=False)  # Display the image without blocking
    plt.pause(time)  # Display image for the specified time
        
def skrij_sporočilo(image_path, A, index, sporočilo, color):
    '''A je matrika, ki slika; n je stranica mreže, in index pove, kateri iterat želim da se prikaže'''
    with Image.open(image_path) as im:
        prej = im
        n = im.size[0]  # Get the width of the image
        print('Mreža je: ',n)
        for k in range(1, identiteta_optimal(n, A) + 1):
            print('začenjam preslikavo: ')
            potem = preslikava(prej, A, n)
            print('Končal sem')
            if k == index:
                modified_potem = napiši_sporočilo(potem, sporočilo, color)
                modified_potem.save('s{}.png'.format(k), 'PNG')
                print(f"Saved image for index {k}")
                prej = modified_potem
                display_image(prej,5)
            else:
                potem.save('s{}.png'.format(k), 'PNG')
                print(f"Saved image for index {k}")
                prej = potem

def pokaži_sporočilo(image_name, A):
    '''Funkcija ti prevrti vse iterate, med njimi so tudi tisti s sporočilom'''
    filename = f'{image_name}.png'  # Construct the filename using the provided image_name parameter
    with Image.open(filename) as im:
        prej = im
        n=im.size[0]
        display_image(prej,2)
        for k in range(1, identiteta_optimal(n,A)+1):
            potem = preslikava(prej, A, n)
            potem.save('s{}.png'.format(k), 'PNG')
            display_image(potem,1)
            prej = potem
        
def pokaži_iterat(image_name, A, index):
    '''Funkcija pokaže samo želeni iterat. Zaradi potenciranja matrike je časovno učinkovita'''
    filename = f'{image_name}'  # Construct the filename using the provided image_name parameter
    with Image.open(filename) as im:
        slika = im
        n=im.size[0]
        A=potenciraj_matriko(A,index,n)
        potem = preslikava(slika, A, n)
        display_image(potem,5)
        #potem.save('s{}.png'.format(k), 'PNG')

if __name__ == "__main__":
    print(help('arnoldova_macka_optimal'))

