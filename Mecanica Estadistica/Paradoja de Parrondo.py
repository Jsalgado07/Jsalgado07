import random
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc


def Juego(n, e):

    Cap_init1 = 0 #Capital inicial
    Cap_init2 = 0 #Capital inicial
    Cap_init3 = 0 #Capital inicial

    Cap1 = []
    Cap2 = []
    Cap3 = []
    N = []

    for i in range(0,n):
      
        # JUEGO 1 SOLO
        l = random.random()
        if l < ((1/2)- e):
            Cap_init1 = Cap_init1 + 1
        else:
            Cap_init1 = Cap_init1 - 1
        
        Cap1 += [Cap_init1]


        # JUEGO 2 SOLO
        if (Cap_init2 % 3) == 0:
            l = random.random()
            if l < ((1/10)- e):
                Cap_init2 = Cap_init2 + 1
            else:
                Cap_init2 = Cap_init2 - 1
        else:
            l = random.random()
            if l < ((3/4)- e):
              Cap_init2 = Cap_init2 + 1
            else:
              Cap_init2 = Cap_init2 - 1
        
        Cap2 += [Cap_init2]
      
      
        # JUEGO 1 Y 2:
        if i%4 == 0 or i%4 == 1:
            l = random.random()
            if l < ((1/2)- e):
                Cap_init3 = Cap_init3 + 1
            else:
                Cap_init3 = Cap_init3 - 1
            
            Cap3 += [Cap_init3]      
      
        else:
            if (Cap_init3 % 3) == 0:
                l = random.random()
                if l < ((1/10)- e):
                    Cap_init3 = Cap_init3 + 1
                else:
                    Cap_init3 = Cap_init3 - 1
            else:
                l = random.random()
                if l < ((3/4)- e):
                  Cap_init3 = Cap_init3 + 1
                else:
                  Cap_init3 = Cap_init3 - 1
        
            Cap3 += [Cap_init3]

        N += [i]    

    return N, Cap1, Cap2, Cap3 


e = 0.005 #Epsilon
n = 1000 #Cantidad de iteraciones

C1  = np.zeros(n)
C2  = np.zeros(n)
C3  = np.zeros(n)

for j in range(0, 100):

    N, Cap1, Cap2, Cap3 = Juego(n, e) 
    
    for k in range(0, n):

        C1[k] += [Cap1[k]] 
        C2[k] += [Cap2[k]] 
        C3[k] += [Cap3[k]] 


for k in range(0, n):
    C1[k] = C1[k]/10
    C2[k] = C2[k]/10
    C3[k] = C3[k]/10


rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)   

plt.figure(frameon= False, edgecolor='c')
plt.title(r'\textbf{$Paradoja\ de\ Parrondo$\\}', fontsize= 14)
plt.plot(N, C1,color= '#f79324', label = 'Juego 1', lw = 2)
plt.plot(N, C2,color= '#b23263', label = 'Juego 2', lw = 2)
plt.plot(N, C3,color= '#0e1d3a', label = 'Juego 1 y 2', lw = 2)
plt.ylabel(r'\textbf{$Ganancia$}', fontsize = 12)
plt.xlabel(r'\textbf{$Intentos$}', fontsize = 12)
plt.legend(fontsize = 12)
plt.show()