#DEFINIR LA FUNCION PARA EL DETERMINANTE:

def Determinante(M):
    if len(M) != len(M[0]):
        det = 'La matriz no es cuadrada'
        return det
    det = 0
    if len(M) == 2:
        det = M[0][0]*M[1][1] - M[1][0]*M[0][1]
        return det
    else:
        for i in range(len(M)):
            M2 = [f[:] for f in M]
            M2.remove(M[0])
            for j in range(len(M2)):
                M2[j] = M2[j][0:i] + M2[j][i+1:]
            det += (-1)**(i) * M[0][i] * Determinante(M2)
        return det

#FUNCION METODO DE CRAMER:

def METODO_CRAMER(A, B):
    
    DetA = Determinante(A)

    if len(A) != len(A[0]):
        S = 'La matriz  de coeficientes no es cuadrada.'
    elif len(A) != len(B):
        S = 'Las matrices de coeficeintes y contantes no coinciden.'
    elif len(A) == 1:
        S = 'El sistema debe ser minimo de dos ecuacion es y dos incognitas.'
    elif DetA == 0:
        S = 'El determinante de la matriz es cero.'
    
    else:
        S = []
        for j in range(len(A)):
            A2 = [f[:] for f in A]
            for i in range(len(A)):
                A2[i][j] = B[i]
            S += [Determinante(A2)/DetA]

    SP = print('La solucion del sistema es: \n', S)
    return SP

#EJEMPLO:

A1 = [[-1, -1,  6,  9],
      [-5,  5, -3,  6],
      [ 7, -3,  5, -6],
      [ 3, -3, -2,  3]]

B1 = [-29, -54, 38, 41]

METODO_CRAMER(A1, B1)