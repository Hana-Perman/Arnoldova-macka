import numpy as np
import matplotlib.pyplot as plt
import copy
from PIL import Image
from PIL import Image, ImageDraw, ImageFont

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
    """ta funkcija potencira matriko in rezultate zračuna po modulu stranice mreže"""
    m_A=[[0,0],[0,0]]
    m_A[0][0]= A[0][0] % n
    m_A[1][0] = A[1][0] % n
    m_A[0][1]= A[0][1] % n
    m_A[1][1]= A[1][1] % n
    return m_A


def identiteta_optimal(n, A):
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
        
def potenciraj_matriko(A,potenca,n):
    B = copy.deepcopy(A)
    for i in range (potenca-1):
        A=modul(multiply_matrices(A, B),n)
        print('A^',i+2,' = ',A)
    return A
    

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
    filename = f'{image_name}'  # Construct the filename using the provided image_name parameter
    with Image.open(filename) as im:
        slika = im
        n=im.size[0]
        A=potenciraj_matriko(A,index,n)
        potem = preslikava(slika, A, n)
        display_image(potem,5)
        #potem.save('s{}.png'.format(k), 'PNG')

pokaži_iterat('s12.png',[[3,1],[2,1]],5)



print("Pozdravljen, dobil si sliko z mojim skritim sporočilom")
print("Navodilo: ta program in slika morata obvezno biti v isti mapi")
image_name=input("Prosim vnesi ime slike brez končnice: ")
a, b, c, d = map(int, input("Prosim vnesi komponente matrike, ločene z vejicami: ").split(','))



A=[[a,b,],[c,d]]
#pokaži_sporočilo(image_name,A)
