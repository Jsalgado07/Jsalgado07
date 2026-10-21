
def factorial(n):
    """Add docs here"""
    result = 1.0
    for ii in range(1,n+1):
        result *= ii
    return result


# use fout.write(f"...") to save the data 
def exp_expansion_new(x, N, fname):
  
    # METODO 1:
    # total = 0.0
    # for n in range(N):
    #     term = (-1)**n*x**n/factorial(n) 
    #     total += term

    # METODO 2:
    a_i = 1.0
    total2 = 1.0
    for n in range(N):
        a_i = a_i*(-x/(n+1)) 
        total2 += a_i
    
    fout = open(fname, "w")
    fout.write(str(total2))
    
    
    return
    fout.close()

# Call the NEW function  
exp_expansion_new(x=1.8766, N=10000, fname="sumdatanew.txt")


#matplotlib notebook
# Plot the data

import matplotlib.pyplot as plt
import numpy as np
x, y, z = np.loadtxt('sumdatanew.txt', unpack = True)
plt.plot(x, y, 'ro')
plt.plot(x, z, 'b-')