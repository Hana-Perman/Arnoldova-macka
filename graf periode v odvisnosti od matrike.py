from arnoldova_macka import *

pot_do_mape = r"C:\Users\hanas\OneDrive\Dokumenti\arnoldova mačka\grafi_2"
tabela_matrik = []
tabela_period = []
največja_mreža = 20
števec = 0

'''tukaj naj bi zgenerirala nekaj različnih matrik in jih shranila va tabelo'''
for a in range(1,50):
    for b in range(a,50):
        A = [[1+(a*b), a],
            [b, 1]]
        števec+=1
        tabela_matrik.append(A)
        print(števec,'. matrika:',A)
        
print(števec)     
'''za vsako matriko bi izračunala periodo pri neki velikosti mreže'''        
for i in range (števec):
    tabela_period.append(identiteta(največja_mreža, tabela_matrik[i]))
    
x_values= range(števec)
y_values = tabela_period

plt.scatter(x_values,y_values, marker='o', s=10  )
for x, y in zip(x_values,y_values):
    plt.vlines(x, 0, y, linestyle='dotted', color='gray')

plt.xlabel('matrika')
plt.ylabel('perioda')
plt.title('graf periode v odvisnosti od matrike ')
# plt.savefig(os.path.join(folder_path, 'graf_periode.png'))

    
plt.show()



    