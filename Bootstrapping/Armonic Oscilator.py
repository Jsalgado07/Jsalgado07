'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-10-08
'''

'''
Bootstrapping for an armonic oscilator
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid

from matplotlib import rc


# %% Definicion de constantes globales y espacions de memoria:

e_min = 0.1
e_max = 10

de = 0.001


# %% Definición de funciones:

def is_pos_def(x):
    eigvalues, _ = np.linalg.eig(x)
    return np.all(eigvalues >= 0)


def recursion(E,x_4,x_2,k):
    
    A = 2*E*(k-1)*x_2/k + (k-1)*(k-2)*(k-3)*x_4/(4*k)
    
    return A
        

def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        print_end   - Optional  : end character; default is '\r' to overwrite previous line (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print("\n")


# %% Programa principal:
        
energies = np.arange(e_min, e_max, de)


# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)    

Fig = plt.figure(figsize = (10, 5), constrained_layout = True)
Gs  = grid.GridSpec(2, 3, figure = Fig)

Fig.suptitle(f'Armomic Oscilator Energie spectrum with $dE = {de}$', fontsize = 25)

a = 0
b = 0


for dim in range(5, 16, 2):

    seq = np.zeros((len(energies),2*dim+1))
    seq[:,0] = 1
    seq[:,2] = energies

    mat1 = np.zeros((dim,dim))
    # mat2 = np.zeros((dim,dim))

    S = []

    for j in range(len(energies)):

        for i in range(4,len(seq[0,:])):
      
            seq[j,i] = recursion(energies[j],seq[j,i-4],seq[j,i-2],i)

        vec = seq[j,:]

        for p in range(dim):
            for q in range(dim):

                mat1[p,q] = round(vec[p+q], 10)#/(vec[p+1]*vec[1+q])
                #mat2[p,q] = vec[p+q+1]#/(vec[p+2]*vec[2+q])

        if is_pos_def(mat1): #is_pos_def(mat2)):

            S += [1]

        else:

            S += [0]    

    if a == 3:
        b += 1
        a  = 0
        
    ax = Fig.add_subplot(Gs[b, a])
    
    ax.plot(energies, S, '#8e24aa')
    ax.set_xlim(e_min,e_max)
    ax.set_ylim(-0.2, 1.2)
    
    ax.set_ylabel(f'M{dim}x{dim}')
    
    a += 1

    progress_bar(dim, 21)

plt.show()



