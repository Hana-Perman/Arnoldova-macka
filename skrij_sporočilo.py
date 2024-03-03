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
    plt.pause(time)  # Display image for 2 seconds
    plt.close()  # Close the current image


def napiši_sporočilo(image, message, color):
    '''Draws on the provided image and returns the modified image'''
    n = image.size[0]
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 35)  # Adjust font and size as needed
    text_bbox = draw.textbbox((0, 0), message, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (n - text_width) // 2
    y = (n - text_height) // 2
    draw.text((x, y), message, fill=color, font=font)
    return image

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


            

n=124
A=[[3,1],[2,1]]
index=5

print(identiteta_optimal(700,A))
skrij_sporočilo('Kvadratki.png', A, 5,'SPOROČILO','black')
skrij_sporočilo('s12.png', A, 6,'JE SKRITO','black')
skrij_sporočilo('s12.png', A, 7,'NA VEČ','black')
skrij_sporočilo('s12.png', A, 8,'KOT ENEM','black')
skrij_sporočilo('s12.png', A, 9,'ITERATU','black')






