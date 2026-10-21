#IMPORTAR LIBRERIAS 
import numpy as np
import matplotlib.pyplot as plt

#DEFINIR LAS FUNCIONES
x = np.array([0, 5, 10])
y1 = (18 - 3*x)/2
y2 = (2 + 1*x)/2

#GRAFICA
plt.figure()
plt.style.use('seaborn')
plt.plot(x, y1, label='Ecuacion 1')
plt.plot(x, y2, label='Ecuacion 2')
plt.legend()
plt.show()