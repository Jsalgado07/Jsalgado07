import numpy as np
from matplotlib import pyplot as plt

def is_pos_def(x): #definisco funzione che accetta matrici positive
    return np.all(np.linalg.eigvals(x) > 0)


def f(nn, x2max, x2min, Emax, Emin, ste, gg=2): #definisco funzione che con i le variabili
#nn=grandezza matrice x^{2} max emin , energia max e min step e g plotta le energie e
#x^{2} in due dimensioni accettate
    n = int(nn)
    g = gg
    steps = int(ste)
    param_x2 = np.linspace(x2min, x2max, steps) #momento x^2{}

    param_E = np.linspace(Emin, Emax, steps) # energia
    x2,Eok = np.meshgrid(param_x2, param_E)
    x4 = (Eok - 2*x2)/(3*g)
    dim = 2*(n - 1) + 1
    seq = np.zeros((steps, steps, dim))
    seq[:, :, 0] = 1 # definisco dei tensori con variabili numero del momento della ricorsione,
    #energia e x^{2}
    seq[:, :, 2] = x2
    seq[:, :, 4] = x4
    
    for i in range(3, dim-3, 2):
        seq[:, :, i+3] = (4*i*Eok*seq[:,:,i-1] + i*(i-1)*(i-2)*seq[:,:,i-3]-
                          +4*(i+1)*seq[:,:,i+1])/ (4*g*(i+2)) #definisco ricorsione
    m = np.zeros((n,n))
    a= plt.figure()
    axes= a.add_axes([0.1,0.1,0.8,0.8])
    axes.set_xlim([Emin,Emax])
    axes.set_ylim([x2min,x2max])
    
    for l in range(steps):
        for i in range(steps):
            for j in range(n):
                for k in range(n):
                    m[j,k] = seq[l,i,j+k]
            if(is_pos_def(m)):
                axes.scatter(Eok[l,i],x2[l,i])
                axes.set_title("g= {}, dimensione matrice {}, step {}".format(gg,nn,ste))
                axes.set_xlabel("E")
                axes.set_ylabel("<$x^2$>")