#DEFINIR LA FUNCION PARA SOLUCIONAR EL SISTEMA:

def Metodo_gauss_simple(A, B):

    m = len(A)
    Sol = [0]*m

    S = [f[:] for f in A]
    for f in range(m):
        S[f] += [B[f]]

    for k in range(m-1):
        p = S[k][k]
        S1 = [f[:] for f in S]
        for i in range(k+1, m):
            c = -S[i][k]/p
            for j in range(k, m+1):
                S1[i][j] = S[i][j] + c*S[k][j]
        S = S1

    for i in range(1, m+1):
        Sol[m-i] += S[m-i][m]/S[m-i][m-i]
        for j in range(1, i):
            Sol[m-i] += -S[m-i][m-j]*Sol[m-j]/S[m-i][m-i]
   
    return  print('La solucion del sistema es: \n', Sol)

#EJEMPLO:

A = [[ 2,  1, -1,  2],
     [ 4,  5, -3,  6],
     [-2,  5, -2,  6],
     [ 4, 11, -4,  8]]

B = [5, 9, 4, 2]

Metodo_gauss_simple(A, B)